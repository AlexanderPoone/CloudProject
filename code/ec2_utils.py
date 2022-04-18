'''
Cloud Computing Project Flask Web Server
'''

import boto3
import paramiko
from os.path import expanduser
from time import time, sleep
from subprocess import check_output


NUM_WORKERS = 1
KEY_PAIR = 'hk'
REGION_NAME = 'ap-east-1'
'''
Amazon Linux
64-bit (x86)
Deep Learning Base AMI (Amazon Linux 2) Version 52.0 - ami-0d13c25a429da989d
Built with NVIDIA CUDA, cuDNN, NCCL, GPU Drivers, Intel MKL-DNN, Docker, NVIDIA-Docker and EFA support. For a fully managed experience, check: https://aws.amazon.com/sagemaker
Root device type: ebs Virtualization type: hvm ENA Enabled: Yes
'''
DEEP_LEARNING_AMAZON_LINUX = 'ami-0d13c25a429da989d'


tm = time()
# The RSA key is already stored on the Web Server beforehand
key = paramiko.RSAKey.from_private_key_file('hk.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to EC2 Instance
def connect(publicIp, instanceNumber, cctvUrl, retries=5, master_ip=None):
    global tm
    try:
        client.connect(hostname=publicIp, username="ec2-user", pkey=key, timeout=120)

        # Execute a command after connecting to an instance
        if master_ip is None:
            # Assumed that the Web Server has AWS CLI Tool installed and configured properly
            # Get the account secrets using the AWS CLI (for security purposes obviously)
            aws_access_key_id = check_output('aws configure get aws_access_key_id').decode('utf-8').rstrip()
            aws_secret_access_key = check_output('aws configure get aws_secret_access_key').decode('utf-8').rstrip()

            # Log in to ECR
            print('Setting up')
            stdin, stdout, stderr = client.exec_command(f'aws configure set aws_access_key_id {aws_access_key_id}')
            print(stderr.read())
            
            print('Log in to ECR')
            stdin, stdout, stderr = client.exec_command(f'aws configure set aws_secret_access_key {aws_secret_access_key};aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/o1i0p5x6')
            print(stderr.read())

            # Pull Docker Image from ECR
            print('Pull Docker Image from ECR')
            stdin, stdout, stderr = client.exec_command('docker pull public.ecr.aws/o1i0p5x6/new:latest')
            print(stderr.read())

            print(f'Time needed to set up a GPU Instance: {time() - tm} s')

            # Start deep learning by issueing command to the container
            print('Start deep learning by issueing command to the container')
            stdin, stdout, stderr = client.exec_command(f'docker run --gpus=all --runtime=nvidia public.ecr.aws/o1i0p5x6/new bash -c "apt-get update;apt-get install -y libnvidia-ml-dev;/root/anaconda3/bin/conda run -n my-env python demo/demo_mot_vis.py configs/mot/tracktor/my2.py --input {cctvUrl} --output /tbd --fps 5"')    #testsuite/unknown_02.mp4
            print(stderr.read())
        else:
            stdin, stdout, stderr = client.exec_command(f'ping -c 4 {master_ip}')

        print('------------------------------------------------------------')



        # TODO: DynamoDB







        #  Close the client connection once the job is done
        client.close()
    except Exception as e:
        print(f'{e}; Retrying...')
        if retries > 0:
            retries -= 1
            connect(publicIp, instanceNumber, cctvUrl, retries, master_ip)

def createG4Instance(cctvUrl='https://s81.ipcamlive.com/streams/514uqhm5v8lc0z9fj/stream.m3u8'):
    s = boto3.Session(
        region_name=REGION_NAME)
    ec2 = s.resource('ec2')

    ##############################################################################

    m = ec2.create_instances(ImageId=DEEP_LEARNING_AMAZON_LINUX,
        InstanceType='g4dn.xlarge',
        SecurityGroups=['launch-wizard-1'],
        MaxCount=1,
        KeyName=KEY_PAIR, 
        MinCount=1,
        BlockDeviceMappings=[{'DeviceName': '/dev/xvda', 'Ebs': { 'VolumeSize': 200 }}])
    #print(dir(m[0]))
    m[0].wait_until_running()
    m[0].reload()
    print(f'SSH into Master @{m[0].public_ip_address}...')

    connect(m[0].public_ip_address, 0, cctvUrl)

    ##############################################################################
    '''
    w = ec2.create_instances(ImageId='ami-032ac9ac998363686',
        InstanceType='t2.micro',
        SecurityGroups=['launch-wizard-1'],
        MaxCount=NUM_WORKERS,
        KeyName=KEY_PAIR, 
        MinCount=NUM_WORKERS)
    for instance in range(len(w)):
        w[instance].wait_until_running()
        w[instance].reload()

        print(f'SSH into Worker {instance} @{w[instance].public_ip_address}...')

        connect(w[instance].public_ip_address, instance+1, master_ip=m[0].public_ip_address)
    '''
    ##############################################################################

    '''
    #   Work is done
    m[0].terminate()
    # for i in w:
    #     i.terminate()
    m[0].wait_until_terminated()
    # i.wait_until_terminated()
    '''

if __name__ == '__main__':
    createG4Instance()
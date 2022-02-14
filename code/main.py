import boto3
import botocore
import paramiko
from os.path import expanduser
from time import sleep

key = paramiko.RSAKey.from_private_key_file(expanduser('~/Downloads/bruh.pem'))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect(publicIp, instanceNumber, retries=5):
    try:
        client.connect(hostname=publicIp, username="ubuntu", pkey=key, timeout=120)

        # Execute a command(cmd) after connecting/ssh to an instance
        stdin, stdout, stderr = client.exec_command('echo hahaha')
        print(stdout.read())

        # close the client connection once the job is done
        client.close()
    except Exception as e:
        print(e)
        if retries > 0:
            retries -= 1
            connect(publicIp, instanceNumber, retries)

NUM_WORKERS = 3
NUM_INSTANCES = NUM_WORKERS + 1
KEY_PAIR = 'bruh'

s = boto3.Session(
    region_name='us-east-1')
ec2 = s.resource('ec2')

i = ec2.create_instances(ImageId='ami-04505e74c0741db8d',
    InstanceType='t2.micro',
    SecurityGroups=['launch-wizard-1'],
    MaxCount=NUM_INSTANCES,
    KeyName=KEY_PAIR, 
    MinCount=NUM_INSTANCES)


for instance in range(len(i)):
    i[instance].wait_until_running()
    i[instance].reload()

    print(f'SSH into {i[instance].public_ip_address}...')

    connect(i[instance].public_ip_address, instance)
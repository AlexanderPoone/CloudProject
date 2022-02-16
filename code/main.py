'''
EC2 ImageIds:

X ami-09397c199cf1dfdab: Ubuntu w/ Flask X
ami-032ac9ac998363686: Spark-Ipython-preconfigured
'''

import boto3
import botocore
import paramiko
from os.path import expanduser
from time import sleep

##############################################################################

key = paramiko.RSAKey.from_private_key_file(expanduser('~/Downloads/bruh.pem'))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connect(publicIp, instanceNumber, retries=5, master_ip=None):
    try:
        client.connect(hostname=publicIp, username="ubuntu", pkey=key, timeout=120)

        # Execute a command(cmd) after connecting/ssh to an instance
        if master_ip is None:
            stdin, stdout, stderr = client.exec_command('echo ThisIsTheMaster')
        else:
            stdin, stdout, stderr = client.exec_command(f'ping -c 4 {master_ip}')
        print(f'{stdout.read()}; Retrying...')

        # close the client connection once the job is done
        client.close()
    except Exception as e:
        print(e)
        if retries > 0:
            retries -= 1
            connect(publicIp, instanceNumber, retries, master_ip)

NUM_WORKERS = 3
KEY_PAIR = 'bruh'

s = boto3.Session(
    region_name='us-east-1')
ec2 = s.resource('ec2')

##############################################################################

m = ec2.create_instances(ImageId='ami-032ac9ac998363686',
    InstanceType='t2.micro',
    SecurityGroups=['launch-wizard-1'],
    MaxCount=1,
    KeyName=KEY_PAIR, 
    MinCount=1)
m[0].wait_until_running()
m[0].reload()
print(f'SSH into Master @{m[0].public_ip_address}...')

connect(m[0].public_ip_address, 0)

##############################################################################

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
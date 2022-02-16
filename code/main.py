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
KEY_PAIR = 'bruh'

s = boto3.Session(
    region_name='us-east-1')
ec2 = s.resource('ec2')

##############################################################################

i = ec2.create_instances(ImageId='ami-032ac9ac998363686',
    InstanceType='t2.micro',
    SecurityGroups=['launch-wizard-1'],
    MaxCount=1,
    KeyName=KEY_PAIR, 
    MinCount=1)
i[0].wait_until_running()
i[0].reload()
print(f'SSH into Master @{i[0].public_ip_address}...')

connect(i[0].public_ip_address, 0)

##############################################################################

i = ec2.create_instances(ImageId='ami-032ac9ac998363686',
    InstanceType='t2.micro',
    SecurityGroups=['launch-wizard-1'],
    MaxCount=NUM_WORKERS,
    KeyName=KEY_PAIR, 
    MinCount=NUM_WORKERS)
for instance in range(len(i)):
    i[instance].wait_until_running()
    i[instance].reload()

    print(f'SSH into Worker {instance} @{i[instance].public_ip_address}...')

    connect(i[instance].public_ip_address, instance+1)
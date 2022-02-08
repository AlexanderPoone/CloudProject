import boto3
import botocore
import paramiko

ec2 = boto3.resource('ec2')

KEY_PAIR = ''
IMAGE_ID = ''
NUM_INSTANCES = 3

i = ec2.create_instances(ImageId=IMAGE_ID, KeyName=KEY_PAIR, MaxCount=NUM_INSTANCES, MinCount=NUM_INSTANCES)
print(i)

key = paramiko.RSAKey.from_private_key_file('path/to/mykey.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # How to get IP programatically?
    client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    stdin, stdout, stderr = client.exec_command(cmd)
    print stdout.read()

    # close the client connection once the job is done
    client.close()
    break

except Exception, e:
    print e
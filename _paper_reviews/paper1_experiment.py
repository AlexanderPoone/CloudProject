'''
An experiment of divide and conquer using EC2 instances
'''

#   Both client & server
stdin, stdout, stderr = client.exec_command('sudo apt-get update; sudo apt-get install -y unzip wine-stable python3-websocket; wget https://dord.mynetgear.com/rapidlasso.zip;unzip rapidlasso.zip')

#  Start Python script containing socket prog & timer here
python
from time import time
start = time.time()

time.sleep(10)  # or do something more productive

done = time.time()
elapsed = done - start

#  Custom program
stdin, stdout, stderr = client.exec_command('lastile64 -tile_size 500 -i sample.las')
stdin, stdout, stderr = client.exec_command('lasground64 -i sample.las')
stdin, stdout, stderr = client.exec_command('lasmerge64 -i sample.las')
'''
Cloud Computing Project Server REST API
'''
import boto3
import botocore
import paramiko
import websockets
import threading

import docker
from flask import Flask, jsonify, request, send_from_directory, abort, send_file, render_template
from flask_cors import CORS

from hashlib import sha512
from os import urandom
from os.path import expanduser
from time import time, sleep
from subprocess import Popen, call, run, check_output, CREATE_NO_WINDOW, DEVNULL

import asyncio
import websockets
from pickle import loads as ploads

from ec2_utils import createG4Instance

app = Flask(__name__)
CORS(app)


s = boto3.Session(region_name='ap-east-1') # Hong Kong
dynamo_client = s.resource('dynamodb')
tableUsers = dynamo_client.Table("savedcameras")
print(tableUsers.table_status)


# Do we need to store worker IP address in database?
MAX_ALLOWED_INSTANCES = 2
client = docker.APIClient()    # client = docker.from_env()


g_payload = {}
g_selected_camera = None

def stream_template(template_name, **context):
    # http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    #rv.enable_buffering(5)
    return rv

@app.route('/', methods = ['GET'])
def dashboard():
    def forward_g_payload():
        global g_selected_camera
        global g_payload

        while True:
            # print('Hi')
            sleep(0.5)
            if len(g_payload) == 0:
                yield None
            elif g_selected_camera is None:
                first = list(g_payload.items()).pop()
                g_selected_camera = first[0]
                yield first[1]
            else:
                #print(g_payload[g_selected_camera])
                yield g_payload[g_selected_camera]
        
    return app.response_class(stream_template('addcamera.jinja',
        data=forward_g_payload(),
        activeEc2=[{
            'url': 'https://s20.ipcamlive.com/streams/14ubd8f7onwbk5ozv/stream.m3u8',
            'camera_id': 'kai_tak_road',
            'status': 1
        }],
        enteringDict={}
    ))

    # return render_template('addcamera.jinja',
    #     activeEc2=[{
    #         'url': 'https://s20.ipcamlive.com/streams/14ubd8f7onwbk5ozv/stream.m3u8',
    #         'camera_id': 'kai_tak_road',
    #         'status': 1
    #     }],
    #     enteringDict={})

@app.route('/switchCamera', methods = ['POST'])
def switchCamera():
    g_selected_camera = request.json['camera_id']
    return


PRODUCTION = True                      # Use Amazon GPU Instances or Test Locally?

@app.route('/provision', methods = ['POST'])
def deploy_ec2():
    print(request.json)
    
    url = request.json['url']			# 'testsuite/unknown_02.mp4'
    start = time()

    if PRODUCTION:						# Use Amazon GPU Instances
    	createG4Instance(url)
    else:								# Test Locally
	    # Limit the number of running instances
	    if len(client.containers()) >= MAX_ALLOWED_INSTANCES:
	        return {'error': 'Max number of allowed instances reached.'}

	    # Create new container from image
	    output = check_output('docker run --env NVIDIA_DISABLE_REQUIRE=1 --gpus all -t -d cctv-cuda')
	    print('DEBUG: ', client.containers())

	    # Must use BASH instead of SH
	    exe = client.exec_create(container=client.containers()[0], cmd=['/bin/bash', '-c', f'/root/anaconda3/bin/conda run -n my-env python demo/demo_mot_vis.py configs/mot/tracktor/my2.py --input "{url}" --output "/tbd" --fps 5'])
	    res = client.exec_start(exec_id=exe)

    end = time()
    print(f'Time needed for provisioning: {end - start} s')
    return {'url': url, 'camera_id': request.json['camera_id']}

@app.route('/unprovision', methods = ['POST'])
def terminate_ec2():
    print(request.json)
    start = time()

    if PRODUCTION:						# Use Amazon GPU Instances
    	pass
    else:
    	pass
    	# Delete the provisioned container

    end = time()
    print(f'Time needed for unprovisioning: {end - start} s')

    return {'camera_id': request.json['camera_id']}

@app.route('/login', methods = ['POST'])
def login():
    record = tableUsers.get_item(Key={'userid': request.form['username']})
    print(record)
    if 'Item' in record:
        if record['Item']['hash'].value == sha512(bytes(request.form['hash'], encoding='utf-8') + record['Item']['salt'].value).digest():
            sessionid = 'blahblahblah'
            print('=== Success ===')
        else:
            sessionid = False
    else:
        sessionid = False
    return {'sessionid': sessionid}

@app.route('/register', methods = ['POST'])
def register():
    record = tableUsers.get_item(Key={'userid': request.form['username']})
    print(record)
    if 'Item' in record:
        return 'taken'
    else:
        salt = urandom(16)
        print(salt)

        hash = sha512(bytes(request.form['hash'], encoding='utf-8') + salt).digest()
        print({'userid': request.form['username'], 'salt': salt, 'hash': hash})

        tableUsers.put_item(Item={'userid': request.form['username'], 'salt': salt, 'hash': hash})
        
        sessionid = 'blahblahblah'
        return {'sessionid': sessionid}

@app.route('/getFileList', methods = ['POST'])
def getFileList():
    request.form['session']
    return

@app.route('/getFile', methods = ['POST'])
def getFile():
    # Location
    'segmentids'
    # Assemble!
    request.form['session']
    request.form['fileId']
    return

@app.route('/upload', methods = ['POST'])
def upload():
    # Just split file into chunks
    tableDedupSequence.put_item(Item={'userid': '35', 'sequence': 'microsoft'})

@app.route('/logout', methods = ['POST'])
def logout():
    request.form['session']
    return

async def echo(websocket):
    async for message in websocket:
        print('Received') # print(f'Received: {message}')
        # print(ploads(message))
        loaded = ploads(message)
        g_payload[loaded['fn']] = loaded
        try:
            await websocket.send('Received') #websocket.send(f'Received: {message}')
        except:
            pass

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765, max_size=99999999):
        await asyncio.Future()  # run forever

def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
    loop.close()

if __name__ == "__main__":
    x = threading.Thread(target=between_callback)
    x.start()
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'privkey.pem'), port=18888)
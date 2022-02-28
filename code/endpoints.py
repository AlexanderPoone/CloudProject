'''
Cloud Computing Project Client REST API
'''
import boto3
import botocore
import paramiko
import websockets

from flask import Flask, jsonify, request, send_from_directory, abort, send_file, render_template
from flask_cors import CORS

from hashlib import sha512
from os import urandom
from os.path import expanduser
from time import sleep

app = Flask(__name__)
CORS(app)

s = boto3.Session(region_name='us-east-1')
client = s.resource('dynamodb')

tableUsers = client.Table("users")
print(tableUsers.table_status)
tableDedupSequence = client.Table("dedupSequence")
print(tableDedupSequence.table_status)

@app.route('/', methods = ['GET'])
def dashboard():
	return render_template('addcamera.jinja',
		activeEc2=[{
			'url': 'https://s20.ipcamlive.com/streams/14ubd8f7onwbk5ozv/stream.m3u8',
			'camera_id': 'kai_tak_road',
			'status': 1
		}],
		enteringDict={})

# Need to store worker IP address in database

@app.route('/provision', methods = ['POST'])
def deploy_ec2():
	pass

@app.route('/unprovision', methods = ['POST'])
def terminate_ec2():
	pass

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context=('cert.pem', 'privkey.pem'), port=18888)
'''
Cloud Computing Project Client REST API
海洋・湖沼・河川を航行する船舶
ヴァン・ベートーヴェン
'''
import boto3
import botocore
import paramiko

from flask import Flask, jsonify, request, send_from_directory, abort, send_file
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

@app.route('/login', methods = ['POST'])
def login():
	record = tableUsers.get_item(Key={'userid': request.form['username']})
	print(record)
	if 'Item' in record:
		print(record['Item'])

		print(record['Item']['hash'] == request.form['hash'])
		sessionid = 'blahblahblah'
	else:
		sessionid = False
	return {'sessionid': sessionid}

@app.route('/register', methods = ['POST'])
def register():
	
	str(sha512(bytes(salt)).hexdigest())
	sha512(bytes(salt)).hexdigest()
	salt = urandom(16)
	tableUsers.put_item(Item={'userid': request.form['username'], 'salt': salt, 'hash': request.form['hash']})
	return True

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
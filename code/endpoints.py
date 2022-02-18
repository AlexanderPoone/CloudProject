'''
Cloud Computing Project Client REST API
'''

from flask import Flask, jsonify, request, send_from_directory, abort, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods = ['POST'])
def login():
	request.form['username']
	request.form['hash']
	return

@app.route('/getFileList', methods = ['POST'])
def getFileList():
	request.form['session']
	return

@app.route('/getFile', methods = ['POST'])
def getFileList():
	# Location

	# Assemble!
	request.form['session']
	request.form['fileId']
	return


@app.route('/logout', methods = ['POST'])
def getFileList():
	request.form['session']
	return
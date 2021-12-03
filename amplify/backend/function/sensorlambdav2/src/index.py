import awsgi
import json
import logging
import os

from flask_cors import CORS
from flask import Flask, app, jsonify, request


BASE_ROUTE ="/sensorsv2"

app = Flask(__name__)
CORS(app)

@app.route(BASE_ROUTE, methods=['POST'])
def create_customer():
    request_json = request.get_json()
    
    return jsonify(message='POST is sucessful')

@app.route(BASE_ROUTE, methods=['GET'])
def list_customer():
    return jsonify(message='GET is successful')


def handler(event, context):
  print('received event:')
  print(event)
  
  return awsgi.response(app,event,context)

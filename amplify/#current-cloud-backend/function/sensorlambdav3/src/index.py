import awsgi
import json
import logging
import os

from flask_cors import CORS
from flask import Flask, app, jsonify, request


BASE_ROUTE ="/sensorsv3"

app = Flask(__name__)
CORS(app)

@app.route(BASE_ROUTE, methods=['POST'])
def create_customer():
    request_json = request.get_json()
    hex_id = request_json.get('hexid')
    name = request_json.get('name')
    temperature = request_json.get('temperature')
    location = request_json.get('location')
   
    return jsonify(message={
        hex_id,
        name,
        temperature
    })

@app.route(BASE_ROUTE, methods=['GET'])
def list_customer():
    return jsonify(
        hexid='0x123',
        name='Test Sensor',
        location='Surrey',
        temperature= 15
    )


def handler(event, context):
  print('received event:')
  print(event)
  return awsgi.response(app,event,context)


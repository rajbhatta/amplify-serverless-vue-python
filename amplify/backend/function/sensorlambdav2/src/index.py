
from sensorservice import SensorService
from dbhandler import DbHandler
from modal.sensor import Sensor
import awsgi
import json
import logging
import os

from flask_cors import CORS
from flask import Flask, app, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_ROUTE ="/sensors"

app = Flask(__name__)
CORS(app)

@app.route(BASE_ROUTE, methods=['POST'])
def create_customer():
    request_json = request.get_json()
    db_session = provide_database_session()
    sensor_service = SensorService(db_session)
    sensor_service.save_sensor(Sensor(sensor_name='test',model='test',temperature='19', operating_location ='langley'))
    return jsonify(message='POST is sucessful')

@app.route(BASE_ROUTE, methods=['GET'])
def list_customer():
    return jsonify(message ='GET is invoked')


def handler(event, context):
  print(event)
  return awsgi.response(app,event,context)

def provide_database_session():
    
    dbusername = 'postgres'
    dbpassword = 'admin123$'
    dbhost = 'equipmentdb.cmqdxui4uot8.us-west-2.rds.amazonaws.com'
    dbname = 'postgres'

    dbhandler = DbHandler(dbusername, dbpassword, dbhost , dbname)
    return dbhandler.get_orm_db_session()


from modal.sensor import Sensor
from sensorservice import SensorService
from dbhandler import DbHandler

import awsgi
import json
import logging
from os import error

from flask_cors import CORS
from flask import Flask, app, jsonify, request


BASE_ROUTE ="/sensorsv3"

app = Flask(__name__)
CORS(app)

logger = logging.getLogger()

@app.route(BASE_ROUTE, methods=['POST'])
def create_customer():
    try:
        request_json = request.get_json()
        #request_hex_id = request_json.get('hexid')
        #request_name = request_json.get('name')
        #request_temperature = request_json.get('temperature')
        #request_location = request_json.get('location')

        request_hex_id = '0x123'
        request_name = 'test name'
        request_temperature = 15
        request_location = 'Surrey'
    
        db_handler = DbHandler(logger)
        db_session = db_handler.get_orm_db_session();

        sensor_service = SensorService(db_session)
        sensor_service.save_sensor(Sensor(name=request_name,hexid=request_hex_id,temperature=request_temperature, operating_location =request_location))
    
        return jsonify(message='OK')
    except error as e:
         logger.critical(e)
         return jsonify(message='FAILED')
    

@app.route(BASE_ROUTE, methods=['GET'])
def list_customer():
    db_handler = DbHandler(logger)
    db_session = db_handler.get_orm_db_session();

    # todo make list to json
    sensor_list =[]
    sensor_service = SensorService(db_session)
    sensors = sensor_service.get_sensor()
    for sensor in sensors:
        sensor_list.append(sensor.get_json)
    return sensor_list

def handler(event, context):
  print('received event:')
  print(event)
  return awsgi.response(app,event,context)

def provide_database_session():
    
    """ 
        PRODUCTION
    """
    #dbusername = validate_db_username(os.environ.get("DB_USERNAME"))
    #dbpassword = validate_db_password(os.environ.get("DB_PASSWORD"))
    #dbhost = validate_db_host(os.environ.get("DB_HOST"))
    #dbname = validate_db_name(os.environ.get("DB_NAME"))

    """
        LOCAL TESTING
    """
    dbusername = validate_db_username('postgres')
    dbpassword = validate_db_password('admin123$')
    dbhost = validate_db_host('equipmentdb.cmqdxui4uot8.us-west-2.rds.amazonaws.com')
    dbname = validate_db_name('postgres')

    dbhandler = DbHandler(logger)
    return dbhandler.get_orm_db_session(dbusername, dbpassword, dbhost , dbname)


def validate_db_username(username):
    if username != None:
        return username
    else:
        logger.critical("UNABLE TO GET DB USERNAME FROM ENVIRONMENT CONFIG")

def validate_db_password(password):
    if password != None:
        return password
    else:
        logger.critical("UNABLE TO GET DB PASSWORD FROM ENVIRONMENT CONFIG")

def validate_db_host(host):
    if host != None:
        return host
    else:
        logger.critical("UNABLE TO GET DB HOSTNAME FROM ENVIRONMENT CONFIG")

def validate_db_name(name):
    if name != None:
        return name
    else:
        logger.critical("UNABLE TO GET DB NAME FROM ENVIRONMENT CONFIG")

from modal.sensor import Sensor
from sqlalchemy.orm.session import Session


class SensorService():

    def __init__(self, db_session):
        self.__db_session=db_session
    
    def save_sensor(self, sensor):
        self.__db_session.add(sensor)
        self.__db_session.commit()
        self.__db_session.flush()

    def get_sensor(self):
        return self.__db_session.query(Sensor).all()

    def get_sensor_by_id(self,id):
        return self.__db_session.query(Sensor).filter(Sensor.id == id).all()
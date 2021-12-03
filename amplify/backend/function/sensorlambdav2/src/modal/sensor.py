from sqlalchemy import (
    Column,
    Text,
    Integer,
    Enum,
    BigInteger
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
import logging

from sqlalchemy.sql.functions import mode

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column('id',BigInteger, primary_key=True, unique=True, nullable=False)
    sensor_name = Column('sensor_name', Text, nullable=True)
    model = Column('model', Text, nullable=True)
    temperature = Column('temperature', Integer, nullable=True)
    operating_location =  Column('operating_location', Text, nullable=True)

    @property
    def get_json(self):
        return {
            'id': self.id,
            'sensor_name': self.sensor_name,
            'model': self.model,
            'temperature': self.temperature,
            'operating_location': self.operating_location
        }
    
    
    


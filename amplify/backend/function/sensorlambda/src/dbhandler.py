import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbHandler():
    
    def __init__(self,dbusername,dbpassword,dbhost,dbname):
        self.__db_username=dbusername
        self.__db_password=dbpassword
        self.__db_host = dbhost
        self.__db_name=dbname
    
    def get_orm_db_session(self):
        postgres_engine = create_engine(f'postgresql://{self.__db_username}:{self.__db_password}@{self.__db_host}:5432/{self.__db_name}')
        session = sessionmaker(bind=postgres_engine)()
        return session;
    

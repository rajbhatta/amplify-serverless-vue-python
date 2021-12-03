from os import error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbHandler():

    def __init__(self, logger, db_username, db_password, db_host, db_name):
        self.__logger =logger
        self.__db_username =db_username
        self.__db_password =db_password
        self.__db_host= db_host
        self.__db_name = db_name
    
    def get_orm_db_session(self):
        try:
            postgres_engine = create_engine(f'postgresql://{self.__db_username}:{self.__db_password}@{self.__db_host}:5432/{self.__db_name}')
            session = sessionmaker(bind=postgres_engine)()
            return session;
        except error as e:
            self.__logger.critical(e)
    

from os import error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbHandler():

    def __init__(self, logger):
        self.__logger =logger
    
    def get_orm_db_session(self,dbusername,dbpassword, dbhost,dbname):
        try:
            postgres_engine = create_engine(f'postgresql://{dbusername}:{dbpassword}@{dbhost}:5432/{dbname}')
            session = sessionmaker(bind=postgres_engine)()
            return session;
        except error as e:
            self.__logger.critical(e)
    

import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbHandler():
    
    def get_orm_db_session(self,dbusername,dbpassword, dbhost,dbname):
        postgres_engine = create_engine(f'postgresql://{dbusername}:{dbpassword}@{dbhost}:5432/{dbname}')
        session = sessionmaker(bind=postgres_engine)()
        return session;
    

import sys
import logging 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
logging.basicConfig(format='%(asctime)s:%(message)s', level=logging.INFO)

class PostgresConnector:
    def __init__(self):
        pass
    
    def get_conn(self): 
        try:
            engine = self.get_engine()
            session = sessionmaker()
            session.configure(bind=engine)
            Session = session()
            if Session!= None:
                logging.info(" ****** Successfully connected to Local database ****** ")
        except Exception as err:
            logging.exception("Failed to create new connection Session!")
            print(str(err))
            raise err
        return Session

    def get_engine(self):
        try:
            engine = create_engine('postgresql+psycopg2://postgres:Pratham07@127.0.0.1/postgres')
        except Exception as err:
            logging.exception("Failed to get database connection!")
            print(str(err))
            raise err
        return engine


    def create_table(self):
        session = self.get_conn()
        query = 'CREATE TABLE IF NOT EXISTS books (id serial PRIMARY KEY,'
        'title varchar (150) NOT NULL,'
        'author varchar (50) NOT NULL);'
        session.execute(query)
        session.commit()





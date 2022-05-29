from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://admin_cesfam:cesfam1359@localhost:3306/dbcesfam")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session() 

Base = declarative_base()

def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
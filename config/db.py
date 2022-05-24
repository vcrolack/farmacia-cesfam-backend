from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+pymysql://admin_cesfam:cesfam1359@localhost:3306/cesfamdb")

meta = MetaData()

conn = engine.connect()

Base = declarative_base()
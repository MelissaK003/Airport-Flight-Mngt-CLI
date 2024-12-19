from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Airline, Destination, Flight

engine =  create_engine("sqlite:///airport.sqlite")

Session =  sessionmaker(bind=engine)
session = Session()

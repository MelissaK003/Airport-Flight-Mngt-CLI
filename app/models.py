from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, CHAR, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Airline model
class Airline(Base):
    __tablename__ = 'airlines'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False,unique=True)
    email = Column(String(100), unique=True, nullable=False )
    phone_number = Column(String(30), nullable=False, unique=True)

    #One Airline can have many Flights
    flights = relationship("Flight", back_populates="airline")

# Destination model
class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    country = Column(String(100), nullable=True)
    city = Column(String(100), nullable=False)
    airport_code = Column(CHAR(10), nullable=True, unique=True)

    # One Destination can receive many Flights
    flights = relationship("Flight", back_populates="destination")

# Flight model
class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    flight_number = Column(String(10), nullable=False )
    airline_id = Column(Integer, ForeignKey('airlines.id'))
    base_location = Column(CHAR(100), nullable=False)
    destination_id = Column(Integer, ForeignKey('destinations.id'))
    flight_date = Column(String(10), nullable=False)
    departure_time = Column(String(5), nullable=False)
    arrival_time = Column(String(5), nullable=False)

    # Relationships
    airline = relationship("Airline", back_populates="flights")
    destination = relationship("Destination", back_populates="flights")

    # Composite uniqueness constraint
    __table_args__ = (UniqueConstraint('flight_number', 'flight_date', name='uq_flight_number_date'),)

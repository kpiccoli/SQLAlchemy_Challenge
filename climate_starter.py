#Dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify


#DATA BASE SETUP
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
measure = Base.classes.measurement
station = Base.classes.station

# FLASK SETUP
app= Flask(__name__)


# FLASK ROUTES

@app.route("/")
def welcome():
    """List all available api routes."""
    return (f'Welcome to Climate Analysis and Exploration Hawaii.'
            f'Available Routes:<br/>'
            f'/api/v1.0/precipitation<br/>'
            f'/api/v1.0/stations<br/>'
            f'/api/v1.0/tobs<br/>')


# Design a query to retrieve the last 12 months of precipitation data
@app.route("/api/v1.0/precip")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(measure.date,measure.prcp).\
                        filter(measure.date >= year_ago).\
                        order_by(measure.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitations
    precip = []

    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["precipitation"] = prcp
        precip.append(precip_dict)
    
    return jsonify(precip)



# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order. 
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    station_most = session.query(measure.station, func.count(measure.station)).\
                   group_by(measure.station).order_by(func.count(measure.station).desc()).all()

    session.close()

    return jsonify(station_most)


# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    waikiki = session.query(measure.date,measure.tobs).\
                        filter(measure.date >= year_ago).\
                        order_by(measure.date).all()

    session.close()

    return jsonify(waikiki)

if __name__ == '__main__':
    app.run(debug=True)
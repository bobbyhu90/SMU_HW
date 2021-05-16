# import dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
# set up sqlite db and tables
engine = create_engine("sqlite:///D:/DataScience/SMU_HW/10_SQLalchemy_Challenge/Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
# create flask app
app = Flask(__name__)
#create home page
@app.route('/')
def home():
    return(
        f'Welcome<br/>'
        f'To see all precipitation data follow the path: /api/v1.0/precipitation<br/>'
        f'To see all station data follow the path: /api/v1.0/stations<br/>'
        f'To see all temperature data follow the path: /api/v1.0/tobs<br/>'
        f'To see all temperature data with a start date follow the path and input years(yyyy-mm-dd): /api/v1.0/<start><br/>'
        f'To see all temperature data with a start and end date follow the path and input years(yyyy-mm-dd): /api/v1.0/<start>/<end>'
    )
# create precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    prcp = session.query(Measurement.date, Measurement.prcp).group_by(Measurement.date).all()
    results = list(np.ravel(prcp))
    session.close()
    return jsonify(results)
# create station route
@app.route('/api/v1.0/stations')
def stations():
   session = Session(engine)
   stations = session.query(Measurement.station).group_by(Measurement.station).all()
   results = list(np.ravel(stations))
   session.close()
   return jsonify(results)
# create tabs route
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    temps = session.query(Measurement.date, Measurement.tobs).group_by(Measurement.date).all()
    results = list(np.ravel(temps))
    session.close()
    return jsonify(results)
# create start date route
@app.route('/api/v1.0/<start>')
def start(start):
    session = Session(engine)
    data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    results = list(np.ravel(data))
    session.close()
    return jsonify(results)
# create start and end day route
@app.route('/api/v1.0/<start>/<end>')
def start_end(start, end):
    session = Session(engine)
    data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    results = list(np.ravel(data))
    session.close()
    return jsonify(results)
# run debug
if __name__ == '__main__':
    app.run(debug=False)
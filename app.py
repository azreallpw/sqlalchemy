import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify 


#####################################################
# Database Setup
####################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
         f"List of Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    prec_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>="2016-08-23").all()
    prec_dict = list(np.ravel(prec_query))
#  Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.
    prec_dict = []
    for temps in prec_query:
        temps_dict = {}
        temps_dict["date"] = Measurement.date
        temps_dict["tobs"] = Measurement.tobs
        prec_dict.append(temps_dict)

#  Return the JSON representation of your dictionary.
    return jsonify(prec_dict)

@app.route("/api/v1.0/stations")
def stations():
    stat_query = session.query(Station.station, Station.name).all()

    stat_dict = list(np.ravel(stat_query))
# # #  Convert the query results to a Dictionary.
    stat_dict = []
    for sta in results2:
        station_dict = {}
        station_dict["station"] = Station.station
        station_dict["name"] = Station.name
        stat_dict.append(station_dict)

# # #  Return the JSON representation of your dictionary.

    return jsonify(stat_dict)

@app.route("/api/v1.0/<start_date>")
def Start_date(start_date):
 session = Session(engine)

results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).all()

  # Get a list of column names and types
columns = inspector.get_columns('measurement')
for c in columns:
    print(c['name'], c["type"])
# columns


# Get a list of column names and types
columns = inspector.get_columns('station')
for c in columns:
    print(c['name'], c["type"])
# columns
    session.close()


final = []
for min, avg, max in results:
    final_dict = {}
    final_dict["min_temp"] = min
    final_dict["avg_temp"] = avg
    final_dict["max_temp"] = max
    final.append(final_dict) 

results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

if __name__ == "__main__":
app.run(debug=True)
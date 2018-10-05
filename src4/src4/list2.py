import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.get(28)
    if flights is not None:
        for flight in flights:
            print("{} to {}, {} minutes.".format( flight.origin, flight.destination, flight.duration ))

if __name__ == "__main__":
    with app.app_context():
        main()

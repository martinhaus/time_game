from flask import Flask, request
import os 
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Player

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {name}!'

@app.route("/add", methods = ["POST"])
def add_book():
    rfid_id=request.form['rfid_id']
    time=request.form['time']
    try:
        player=Player(
            rfid_id=rfid_id,
            time=time
        )
        db.session.add(player)
        db.session.commit()
        return "Player added. Player id={}".format(player.id)
    except Exception as e:
        return(str(e))

@app.route("/getall")
def get_all():
    try:
        players=Player.query.all()
        return  jsonify([e.serialize() for e in players])
    except Exception as e:
	    return(str(e))

@app.route("/get/<rfid_id>")
def get_one(rfid_id):
    try:
        player=Player.query.filter_by(rfid_id=rfid_id).first()
        return jsonify(player.serialize())
    except Exception as e:
        return(str(e))
from flask import Flask, request
import os 
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import render_template

app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Player
from models import Group

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/get_all')
def get_all_page():
    return render_template('get_all.html')

@app.route("/api/add", methods = ["POST"])
def add_player():
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

@app.route("/api/update", methods = ["POST"])
def update_player():
    rfid_id=request.form['rfid_id']
    time=request.form['time']
    update_player_record(rfid_id, time)
    return "Player updated"

@app.route("/api/getall")
def get_all():
    try:
        players=Player.query.all()
        return  jsonify([e.serialize() for e in players])
    except Exception as e:
	    return(str(e))

@app.route("/api/get/<rfid_id>")
def get_one(rfid_id):
    try:
        player=Player.query.filter_by(rfid_id=rfid_id).first()
        print(player)
        if player is None:
           insert_player(rfid_id, 60)
        return jsonify(player.serialize())
    except Exception as e:
        return(str(e))

def insert_player(rfid_id, time):
    try:
        player=Player(
            rfid_id=rfid_id,
            time=time
        )
        db.session.add(player)
        db.session.commit()
        return "Player added. Player id={}".format(player.rfid_id)
    except Exception as e:
        print(e)


def update_player_record(rfid_id, time):
    try:
        player=Player.query.filter_by(rfid_id=rfid_id).first()
        print(player)
        player.time = time
        db.session.commit()
        return "Player updated. Player id={}".format(player.rfid_id)
    except Exception as e:
        print(e)
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    rfid_id = db.Column(db.String())
    time = db.Column(db.Integer)

    def __init__(self, rfid_id, time):
        self.rfid_id = rfid_id
        self.time = time
       
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'rfid_id': self.rfid_id,
            'time': self.time
        }
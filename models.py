from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = db.Table('association_table', Base.metadata,
    db.Column('player_id', db.Integer, db.ForeignKey('player.rfid_id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
)


class Player(db.Model):
    __tablename__ = 'players'

    # id = db.Column(db.Integer, primary_key=True)
    rfid_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    groups = db.relationship(
        "Group",
        secondary=association_table,
        # primaryjoin=(association_table.c.group_id == id),
        back_populates="players")

    def __init__(self, rfid_id, time):
        self.rfid_id = rfid_id
        self.time = time
       
    def __repr__(self):
        return '<id {}>'.format(self.rfid_id)
    
    def serialize(self):
        return {
            'rfid_id': self.rfid_id,
            'time': self.time
        }

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    players = db.relationship(
        "Player",
        secondary=association_table,
        # primaryjoin=(association_table.c.player_id == id),
        back_populates="groups")

    def __init__(self, name):
        self.name = name
       
    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.name)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

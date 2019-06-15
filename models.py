from app import db
from sqlalchemy.dialects.postgresql import JSON


association_table = Table('association', Base.metadata,
    Column('player_id', Integer, ForeignKey('player.rfid_id')),
    Column('group_id', Integer, ForeignKey('group.id'))
)

class Player(db.Model):
    __tablename__ = 'players'

    # id = db.Column(db.Integer, primary_key=True)
    rfid_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    groups = relationship(
        "Group",
        secondary=association_table,
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
    players = relationship(
        "Player",
        secondary=association_table,
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

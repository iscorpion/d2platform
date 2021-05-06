from app import db, engine
from sqlalchemy.orm import sessionmaker


class BaseItem(db.Model):
    __table_args__ = {"schema": "d2platform"}
    __tablename__ = "base_items"
    base_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    type = db.Column(db.Text)
    player_class = db.Column(db.Text)
    item_class = db.Column(db.Text)
    stats = db.Column(db.Text)
    icon = db.Column(db.Text)
    is_ethereal = db.Column(db.Boolean)

    def __repr__(self):
        return '<Base Item {}>'.format(self.name)


class Item(db.Model):
    __table_args__ = {"schema": "d2platform"}
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    base_id = db.Column(db.Integer, db.ForeignKey(BaseItem.base_id))
    rarity = db.Column(db.Text)
    affixes = db.Column(db.Text)
    set_name = db.Column(db.Text)
    icon = db.Column(db.Text)

    base_item = db.relationship('BaseItem', uselist=False, lazy='joined')

    def __repr__(self):
        return '<Item {}>'.format(self.name)


Session = sessionmaker(bind=engine)
session = Session()

from flask import current_app as app

from app.domain.dataclasses import BaseItemData, ItemData
from app.domain.item_models import db, Item
from app.domain.item_models import BaseItem, session


def get_base_items():
    return db.session().query(BaseItem).all()


def get_items():
    return db.session().query(Item).all()

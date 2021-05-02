from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app

from app.domain.dataclasses import BaseItemData, ItemData
from app.domain.models import db, Item
from app.domain.models import BaseItem, session


@app.route('/')
def initial():
    return jsonify("Hello World!")


@app.route('/base_items', methods=['GET'])
def base_item_all():
    """Create a user via query string parameters."""

    result = db.session().query(BaseItem).all()

    items = []
    for item in result:
        items.append(BaseItemData(item))
    return jsonify(items)


@app.route('/items', methods=['GET'])
def items_all():
    """Create a user via query string parameters."""

    result = db.session().query(Item).all()

    items = []
    for item in result:
        items.append(ItemData(item))
    return jsonify(items)

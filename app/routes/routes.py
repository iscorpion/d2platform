from flask import jsonify
from flask import current_app as app

from app.service import item_service


@app.route('/')
def initial():
    return jsonify("Hello World!")


@app.route('/base_items', methods=['GET'])
def base_item_all():
    items = item_service.get_base_items()

    return jsonify(items)


@app.route('/items', methods=['GET'])
def items_all():
    items = item_service.get_items()

    return jsonify(items)

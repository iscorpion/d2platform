from flask import current_app as app

from app.domain.dataclasses import BaseItemData, ItemData
from app.repository import item_repository


def get_base_items():
    result = item_repository.get_base_items()

    base_items = [BaseItemData(item) for item in result]
    return base_items


def get_items():
    result = item_repository.get_items()

    items = [ItemData(item) for item in result]
    return items

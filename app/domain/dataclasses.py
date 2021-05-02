from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional


@dataclass()
@dataclass_json
class BaseItemData:
    base_id: int
    name: str
    type: str
    player_class: Optional[str]
    item_class: str
    stats: str
    icon: str
    is_ethereal: bool

    def __init__(self, base_item):
        self.base_id = base_item.base_id
        self.name = base_item.name
        self.type = base_item.type
        self.player_class = base_item.player_class
        self.item_class = base_item.item_class
        self.stats = base_item.stats
        self.icon = base_item.icon
        self.is_ethereal = base_item.is_ethereal


@dataclass
@dataclass_json
class ItemData:
    item_id: int
    name: str
    rarity: str
    affixes: str
    set_name: str
    icon: str

    def __init__(self, item):
        self.item_id = item.item_id
        self.name = item.item_id
        self.rarity = item.rarity
        self.affixes = item.affixes
        self.set_name = item.set_name
        self.icon = item.icon

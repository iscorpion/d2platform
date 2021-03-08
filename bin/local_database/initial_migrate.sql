CREATE SCHEMA IF NOT EXISTS d2platform
AUTHORIZATION d2platform_adm;

CREATE EXTENSION IF NOT EXISTS HSTORE ;

CREATE EXTENSION pgcrypto ;

CREATE TABLESPACE TSD_D2PLATFORM
    OWNER d2platform_adm
    LOCATION '/tablespace/data';

CREATE TABLESPACE TSI_D2PLATFORM
    OWNER d2platform_adm
    LOCATION '/tablespace/index';

CREATE TABLE d2platform.base_items (
    base_id int PRIMARY KEY,
    name text unique,
    type text,
    player_class varchar,
    item_class varchar,
    stats json,
    icon text,
    is_ethereal boolean
);

CREATE TABLE d2platform.items (
    item_id int PRIMARY KEY,
    name text unique,
    base_id int,
    rarity text,
    affixes text,
    set_name text,
    icon text,
    foreign key (base_id) references d2platform.base_items (base_id)
);

CREATE TABLE d2platform.runewords (
  name text,
  base text,
  runes text,
  stats json,
  affixes text
);

INSERT INTO d2platform.runewords (name, base, runes, stats, affixes) VALUES
('Enigma', 'Body armor {2}', 'Jah + Ith + Ber', '{"level":72}','+1 To Teleport\n+2 To All Skills');

INSERT INTO d2platform.base_items
    (base_id,
    name,
    type,
    player_class,
    item_class,
    stats,
    icon,
    is_ethereal )
values
    (1, 'Shako', 'Helm', null, 'Elite', '{"defense":"98-141","level requirement":"43"}',
    'http://classic.battle.net/images/battle/diablo2exp/images/items/armor/cap.gif',
    false);

INSERT INTO d2platform.items
    (item_id,
    name,
    base_id,
    rarity ,
    affixes ,
    set_name,
    icon)
values
    (1, 'Harlequin Crest', 1, 'Unique', '+2 To All Skills', null,
    'http://classic.battle.net/images/battle/diablo2exp/images/items/uniques/harlequincrest.gif');


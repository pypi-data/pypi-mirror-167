import logging
from dataclasses import dataclass
from typing import List

import netdot.dataclasses
from netdot.csv_util import CSVDataclass
from netdot.dataclasses.base import NetdotAPIDataclass

logger = logging.getLogger(__name__)


@dataclass
class Site(NetdotAPIDataclass, CSVDataclass):
    NETDOT_MENU_URL_PATH = 'cable_plant'
    NETDOT_TABLE_NAME = 'Site'
    id: int = None
    name: str = None
    aliases: str = None
    availability: str = None
    availability_xlink: int = None
    contactlist: str = None
    contactlist_xlink: int = None
    gsf: str = None
    number: str = None   # maps to GISSite `building_number` property
    street1: str = None  # First line of 'civic address'
    street2: str = None  # Optional second line of 'civic address'
    state: str = None
    city: str = None
    country: str = None
    zip: str = None
    pobox: str = None
    info: str = None

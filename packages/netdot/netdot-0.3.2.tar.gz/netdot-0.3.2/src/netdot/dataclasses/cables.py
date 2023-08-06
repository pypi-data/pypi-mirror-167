from dataclasses import dataclass

from netdot import parse
from netdot.csv_util import CSVDataclass
from netdot.dataclasses.base import NetdotAPIDataclass


@dataclass
class HorizontalCable(NetdotAPIDataclass, CSVDataclass):
    NETDOT_MENU_URL_PATH = 'management'  # [1] Choose from [management, contacts, cable_plant, advanced, reports, export, help]
    NETDOT_TABLE_NAME = 'horizontalcable'  # [2] Appropriate capitalization pulled from Netdot [1]
    account: str = None
    closet: int = None
    contactlist: int = None
    datetested: parse.DateTime = None
    faceplateid: str = None
    id: int = None
    info: str = None
    installdate: parse.DateTime = None
    jackid: str = None
    length: str = None
    room: int = None
    testpassed: bool = False
    type: int = None

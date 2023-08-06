from dataclasses import dataclass
from netdot.csv_util import CSVDataclass
from netdot.dataclasses.base import NetdotAPIDataclass

from netdot import parse


@dataclass()
class rr(NetdotAPIDataclass, CSVDataclass):
    NETDOT_MENU_URL_PATH = 'management'  # [1] Choose from [management, contacts, cable_plant, advanced, reports, export, help]
    NETDOT_TABLE_NAME = 'rr'        
    # TODO the web_url is actually 'host' -- need to add another class variable for 'NETDOT_MENU_URL_PATH'
    id: int = None
    active: bool = False
    auto_update: bool = False
    expiration: parse.DateTime = None
    info: str = None
    name: str = None
    zone: str = None
    zone_xlink: int = None
    created: parse.DateTime = None
    modified: parse.DateTime = None


ResourceRecord = rr


@dataclass()
class rraddr(NetdotAPIDataclass, CSVDataclass):
    NETDOT_MENU_URL_PATH = 'management'  # [1] Choose from [management, contacts, cable_plant, advanced, reports, export, help]
    NETDOT_TABLE_NAME = 'rraddr'
    id: int = None
    ipblock: str = None
    ipblock_xlink: int = None
    rr: str = None
    rr_xlink: int = None
    ttl: str = None


ResourceRecordAddress = rraddr


@dataclass()
class rrcname(NetdotAPIDataclass, CSVDataclass):
    NETDOT_MENU_URL_PATH = 'management'  # [1] Choose from [management, contacts, cable_plant, advanced, reports, export, help]
    NETDOT_TABLE_NAME = 'rrcname'
    cname: str = None
    rr: str = None
    rr_xlink: int = None
    id: int = None
    ttl: str = None


ResourceRecordCNAME = rrcname


# class rrds:
#     algorithm: int = None
#     digest: str = None
#     digest_type: int = None
#     id: int = None
#     key_tag: int = None
#     rr: int = None
#     ttl: str = None


# class rrhinfo:
#     cpu: str = None
#     id: int = None
#     os: str = None
#     rr: int = None
#     ttl: str = None


# class rrloc:
#     altitude: int = None
#     horiz_pre: str = None
#     id: int = None
#     latitude: str = None
#     longitude: str = None
#     rr: int = None
#     size: str = None
#     ttl: str = None
#     vert_pre: str = None


# class rrmx:
#     exchange: str = None
#     id: int = None
#     preference: int = None
#     rr: int = None
#     ttl: str = None


# class rrnaptr:

#     flags: str = None
#     id: int = None

#     order_field: int = None
#     preference: int = None
#     regexpr: str = None
#     replacement: str = None
#     rr: int = None
#     services: str = None
#     ttl: str = None


# class rrns:

#     id: int = None

#     nsdname: str = None
#     rr: int = None
#     ttl: str = None


# class rrptr:

#     id: int = None

#     ipblock: int = None
#     rr: int = None
#     ttl: str = None
#     ptrdname: str = None


# class rrsrv:

#     id: int = None

#     port: int = None
#     priority: int = None
#     rr: int = None
#     target: str = None
#     ttl: str = None
#     weight: int = None


# class rrtxt:

#     id: int = None

#     rr: int = None
#     ttl: str = None
#     txtdata: str = None
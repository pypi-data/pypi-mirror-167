from .asset import Asset
from .base import NetdotAPIDataclass
from .device import Device
from .interface import Interface
from .ipblock import IPBlock
from .products import Product, ProductType
from .site import Site
from .vlan import VLAN
from .physaddr import PhysAddr
from .fwtable import FWTable, FWTableEntry
from .dns import ResourceRecordCNAME, ResourceRecord, ResourceRecordAddress

_initialized = False

def initialize():
    # TODO can these just be at module-level instead of having this be a runtime function?
    global _initialized
    if not _initialized:
        Asset()
        Device()
        FWTable()
        FWTableEntry()
        Interface()
        IPBlock()
        Product()
        ProductType()
        Site()
        VLAN()
        PhysAddr()
        ResourceRecordCNAME()
        ResourceRecord()
        ResourceRecordAddress()
        _initialized = True


Subnet = IPBlock
IPAddr = IPBlock
IPContainer = IPBlock

__all__ = [
    'initialize', 'Asset', 'Device', 'Interface', 'IPBlock', 'Subnet', 'IPAddr', 'IPContainer',
    'Product', 'ProductType', 'Site', 'VLAN', 'NetdotAPIDataclass', 'PhysAddr', 'FWTable', 'FWTableEntry',         'ResourceRecordCNAME', 'ResourceRecord', 'ResourceRecordAddress'
]

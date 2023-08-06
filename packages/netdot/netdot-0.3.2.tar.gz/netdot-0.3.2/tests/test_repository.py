import datetime
import ipaddress
import os

import pytest
from assertpy import assert_that

import netdot.dataclasses
from netdot import Repository
from netdot.mac_address import MACAddress


@pytest.fixture
def repository() -> Repository:
    url = os.environ.get('NETDOT_URL', 'https://nsdb.uoregon.edu')
    username = os.environ.get('NETDOT_USERNAME', '')
    password = os.environ.get('NETDOT_PASSWORD', '')
    return Repository(url, username, password, times_to_retry=1)


def test_Repository_initialization_of_methods():
    # Arrange (assert)
    assert_that(Repository._initialized).is_false()

    # Act
    Repository.prepare_class()

    # Assert
    assert_that(Repository._initialized).is_true()
    Repository_attribute_names = vars(Repository).keys()
    assert_that(Repository_attribute_names).contains('get_device')
    assert_that(Repository_attribute_names).contains('get_all_devices')
    assert_that(Repository_attribute_names).contains('get_site')
    assert_that(Repository_attribute_names).contains('get_devices_by_site')
    assert_that(Repository_attribute_names).contains('get_devices_by_asset')
    assert_that(Repository_attribute_names).contains(
        'get_interfaces_by_device')


@pytest.mark.vcr()
def test_discover_sites_devices(repository: Repository):
    # Arrange
    site = repository.get_site(142)  # 142 => 1900 Millrace Drive

    # Act
    devices = site.load_devices()

    # Assert
    assert_that(devices).is_length(3)
    device = devices[0]
    assert_that(device.base_MAC).is_equal_to(MACAddress('F0B2E560AA00'))


@pytest.mark.vcr()
def test_get_devices_by_site(repository: Repository):
    # Arrange
    site = repository.get_site(142)  # 142 => 1900 Millrace Drive

    # Act
    devices = repository.get_devices_by_site(site)

    # Assert
    assert_that(devices).is_length(3)
    device = devices[0]
    assert_that(device.base_MAC).is_equal_to(MACAddress('F0B2E560AA00'))


@pytest.mark.vcr()
def test_get_site_from_device(repository: Repository):
    # Arrange
    MILLRACE_BLDG_NUMBER = '043'
    # A device from 1900 Millrace Drive (rrpnet-1900-millrace-drive-poe-sw1.net.uoregon.edu)
    MILLRACE_DEVICE_ID = 9061
    device = repository.get_device(MILLRACE_DEVICE_ID)

    # Act
    site = device.load_site()

    # Assert
    assert_that(site.number).is_equal_to(MILLRACE_BLDG_NUMBER)


@pytest.mark.vcr()
def test_web_urls(repository: Repository):
    # Arrange
    site = repository.get_site(142)  # 1900 Millrace Drive
    # autzen-idfc-sw1's First interface
    interface = repository.get_interface(87428)
    device = repository.get_device(9643)  # alder-building-mdf-poe-sw1

    assert_that(site.web_url).is_equal_to(
        'https://nsdb.uoregon.edu/cable_plant/view.html?table=Site&id=142')
    assert_that(device.web_url).is_equal_to(
        'https://nsdb.uoregon.edu/management/device.html?id=9643')
    assert_that(interface.web_url).is_equal_to(
        'https://nsdb.uoregon.edu/management/interface.html?id=87428')


@pytest.mark.vcr()
def test_discover_device_interfaces(repository: Repository):
    # Arrange
    device = repository.get_device(9643)  # 9643 => alder-building-mdf-poe-sw1

    # Act
    interfaces = device.load_interfaces()

    # Assert
    assert_that(interfaces).is_length(58)
    interface = interfaces[0]
    assert_that(interface.physaddr).is_equal_to(MACAddress('B033A673763B'))


@pytest.mark.vcr()
def test_get_vlan_by_interface(repository: Repository):
    # Act
    vlans = repository.get_vlans_by_interface(87428)  # autzen-idfc-sw1's First interface

    # Assert
    assert_that(vlans).is_length(1)
    vlan = vlans[0]
    assert_that(vlan.vid).is_equal_to(216)
    assert_that(vlan.name).is_equal_to('CC_IS_NGR_216')


@pytest.mark.vcr()
def test_get_vlan_count_by_interface(repository: Repository):
    # Act
    count = repository.get_vlans_count_by_interface(
        87428)  # autzen-idfc-sw1's First interface

    # Assert
    assert_that(count).is_equal_to(1)


@pytest.mark.vcr()
def test_get_ipblock_StaticAddress(repository: Repository):
    # Act
    ipblock_address = repository.get_ipblock(
        177611046)  # "uoregon.edu" IP address

    # Assert
    assert_that(ipblock_address.address).is_equal_to(
        ipaddress.ip_address('184.171.111.233'))
    assert_that(ipblock_address.prefix).is_equal_to(32)
    assert_that(ipblock_address.status).is_equal_to('Static')
    assert_that(ipblock_address.used_by).is_none()


@pytest.mark.vcr()
def test_get_ipblock_Subnet(repository: Repository):
    # Act
    # Subnet associated to "uoregon.edu" IP address
    ipblock_subnet = repository.get_ipblock(271514934)

    # Assert
    assert_that(ipblock_subnet.address).is_equal_to(
        ipaddress.ip_address('184.171.111.0'))
    assert_that(ipblock_subnet.prefix).is_equal_to(24)
    assert_that(ipblock_subnet.status).is_equal_to('Subnet')
    assert_that(ipblock_subnet.used_by).is_equal_to('Information Services')


@pytest.mark.vcr()
def test_get_ipblock_Container(repository: Repository):
    # Act
    # Container associated to "uoregon.edu" Subnet
    ipblock_container = repository.get_ipblock(177611409)

    # Assert
    assert_that(ipblock_container.address).is_equal_to(
        ipaddress.ip_address('184.171.96.0'))
    assert_that(ipblock_container.prefix).is_equal_to(19)
    assert_that(ipblock_container.status).is_equal_to('Container')


@pytest.mark.vcr()
def test_discover_ipblock_Subnet_from_StaticAddress(repository: Repository):
    # Arrange
    ipblock_address = repository.get_ipblock(177611046)

    # Act
    ipblock_subnet = ipblock_address.get_parent()

    # Assert
    assert_that(ipblock_subnet.address).is_equal_to(
        ipaddress.ip_address('184.171.111.0'))
    assert_that(ipblock_subnet.prefix).is_equal_to(24)
    assert_that(ipblock_subnet.status).is_equal_to('Subnet')
    assert_that(ipblock_subnet.used_by).is_equal_to('Information Services')


@pytest.mark.vcr()
def test_get_ipblock_by_address_StaticAddress(repository: Repository):
    # Act
    ipblock_address = repository.get_ipblock_by_address('184.171.111.233')

    # Assert
    assert_that(ipblock_address.address).is_equal_to(
        ipaddress.ip_address('184.171.111.233'))
    assert_that(ipblock_address.prefix).is_equal_to(32)
    assert_that(ipblock_address.status).is_equal_to('Static')
    assert_that(ipblock_address.used_by).is_none()


@pytest.mark.vcr()
def test_get_ipblock_by_address_StaticAddressIPv6(repository: Repository):
    # Act
    ipblock_address = repository.get_ipblock_by_address('2605:bc80:200f:2::5')

    # Assert
    assert_that(ipblock_address.address).is_equal_to(
        ipaddress.ip_address('2605:bc80:200f:2::5'))
    assert_that(ipblock_address.prefix).is_equal_to(128)
    assert_that(ipblock_address.status).is_equal_to('Reserved')


@pytest.mark.vcr()
def test_get_ipblock_by_address_Subnet(repository: Repository):
    # Act
    ipblock_subnet = repository.get_ipblock_by_address('184.171.111.0')
    ipblock_subnet.get_children()

    # Assert
    assert_that(ipblock_subnet.address).is_equal_to(
        ipaddress.ip_address('184.171.111.0'))
    assert_that(ipblock_subnet.prefix).is_equal_to(24)
    assert_that(ipblock_subnet.status).is_equal_to('Subnet')
    assert_that(ipblock_subnet.used_by).is_equal_to('Information Services')


@pytest.mark.vcr()
def test_get_product_with_wierd_name(repository: Repository):
    # Act
    product = repository.get_product(377)

    # Assert
    assert_that(product.name).is_equal_to('800-????5-02')
    assert_that(product.type).is_equal_to('Module')


@pytest.mark.vcr()
def test_get_product(repository: Repository):
    # Act
    product = repository.get_product(802)

    # Assert
    assert_that(product.name).is_equal_to('EX3400-24P')
    assert_that(product.type).is_equal_to('Switch')


@pytest.mark.vcr()
def test_get_products(repository: Repository):
    # Act
    products = repository.get_all_products()

    # Assert
    assert_that(products).is_length(786)


@pytest.mark.vcr()
def test_infer_product(repository: Repository):
    # Arrange
    device = repository.get_device(10091)

    # Act
    product = device.infer_product()

    # Assert
    assert_that(product.type).is_equal_to('Switch')
    assert_that(product.name).is_equal_to('EX3400-48P')


@pytest.mark.vcr()
def test_get_physaddr(repository: Repository):
    # Act
    physaddr = repository.get_physaddr(17206353813)

    # Assert
    assert_that(physaddr.address).is_equal_to(MACAddress('8C3BADDA9EF1'))
    assert_that(physaddr.static).is_equal_to(False)
    assert_that(physaddr.web_url).is_equal_to(
        'https://nsdb.uoregon.edu/management/mac.html?id=17206353813')


@pytest.mark.vcr()
def test_get_interface(repository: Repository):
    # Act
    interface = repository.get_interface(364234)

    # Assert
    assert_that(interface.device).is_equal_to(
        'white-stag-1st-poe-sw1.net.uoregon.edu')
    assert_that(interface.jack).is_equal_to('814B0091')
    assert_that(interface.snmp_managed).is_equal_to(True)
    assert_that(interface.oper_up).is_equal_to(True)
    assert_that(interface.overwrite_descr).is_equal_to(True)
    assert_that(interface.web_url).is_equal_to(
        'https://nsdb.uoregon.edu/management/interface.html?id=364234')


@pytest.mark.vcr()
def test_get_physaddr_by_MACAddress(repository: Repository):
    # Act
    physaddr = repository.get_physaddr_by_MACAddress(
        MACAddress('9C8ECD25905B'))

    # Assert
    assert_that(physaddr.id).is_equal_to(9629748756)
    assert_that(physaddr.address).is_equal_to(MACAddress('9C8ECD25905B'))
    assert_that(physaddr.static).is_equal_to(False)
    assert_that(physaddr.first_seen).is_equal_to(datetime.datetime(2020, 6, 9, 16, 39, 3))
    assert_that(physaddr.last_seen).is_after(datetime.datetime(2022, 9, 2, 17, 0, 3))

@pytest.mark.vcr()
def test_get_FWTableEntry(repository: Repository):
    # Act
    entry = repository.get_fwtableentry(285686)

    # Assert
    assert_that(entry.interface).is_equal_to(
        'white-stag-3rd-poe-sw2.net.uoregon.edu [ge-0/0/47]')
    assert_that(entry.physaddr).is_equal_to(MACAddress('9c934e5ec4ca'))
    assert_that(entry.web_url).is_equal_to(
        'https://nsdb.uoregon.edu/generic/view.html?table=fwtableentry&id=285686')


@pytest.mark.vcr()
def test_find_edge_port1(repository: Repository):
    # Act
    interface = repository.find_edge_port('9C8ECD25905B')

    # Assert
    assert_that(interface.device).is_equal_to('pmo-ap4.net.uoregon.edu')
    assert_that(interface.name).is_equal_to('Dot11Radio0')


@pytest.mark.vcr()
def test_find_edge_port2(repository: Repository):
    # Act
    interface = repository.find_edge_port('00107F152EFF')

    # Assert
    assert_that(interface.device).is_equal_to('white-stag-1st-poe-sw1.net.uoregon.edu')
    assert_that(interface.name).is_equal_to('ge-1/0/3')


@pytest.mark.vcr()
def test_find_edge_port3(repository: Repository):
    # Act
    interface = repository.find_edge_port('8C3BADDA9EF1')

    # Assert
    assert_that(interface.device).is_equal_to('resnet-graduate-housing-e-poe-sw1.net.uoregon.edu')
    assert_that(interface.name).is_equal_to('GigabitEthernet2/0/8')
    assert_that(interface.jack).is_equal_to('146A010B')
    assert_that(interface.description).is_equal_to('Resnet Dot1x-MAB Access Port')


@pytest.mark.vcr()
def test_get_ResourceRecord(repository: Repository):
    # Act
    dns_record = repository.get_rr(54482)

    # Assert
    assert_that(dns_record.info).is_equal_to('LOC: 215A Oregon Hall CON: Chris LeBlanc, 6-2931 ')
    assert_that(dns_record.name).is_equal_to('metadata2')
    # TODO fix the web_url logic 
    # assert_that(dns_record.web_url).is_equal_to('https://nsdb.uoregon.edu/management/host.html?id=54482')


@pytest.mark.vcr()
def test_get_ResourceRecord_by_ipaddress1(repository: Repository):
    # Act
    dns_record = repository.get_rr_by_address('128.223.37.93')

    # Assert
    assert_that(dns_record.info).is_equal_to('LOC: 215A Oregon Hall CON: Chris LeBlanc, 6-2931 ')
    assert_that(dns_record.name).is_equal_to('metadata2')


@pytest.mark.vcr()
def test_get_ResourceRecord_by_ipaddress2(repository: Repository):
    # Act
    dns_record = repository.get_rr_by_address('128.223.93.66')

    # Assert
    assert_that(dns_record.info).is_equal_to('LOC: Onyx Bridge 361 CON: Solar Radiation Monitoring Lab, 346-4745 CON: Peter Harlan, 346-4745 ')
    assert_that(dns_record.name).is_equal_to('solardat')

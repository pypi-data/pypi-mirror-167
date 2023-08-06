
import os

import pytest
from assertpy import assert_that

from netdot.client import Client


@pytest.fixture
def client() -> Client:
    url = os.environ.get('NETDOT_URL', 'https://nsdb.uoregon.edu')
    username = os.environ.get('NETDOT_USERNAME', '')
    password = os.environ.get('NETDOT_PASSWORD', '')
    return Client(url, username, password)


@pytest.mark.vcr()
def test_get_object_by_id(client: Client):
    # Act
    device = client.get_object_by_id('Device', 12973)

    # Assert
    assert_that(device).is_type_of(dict)
    assert_that(device).contains_key('name')
    assert_that(device).contains_key('site')
    assert_that(device).contains_key('bgplocalas')
    assert_that(device).contains_key('last_arp')


@pytest.mark.vcr()
def test_get_all(client):
    # Act
    sites = client.get_all('Site')

    # Assert
    assert_that(sites).is_type_of(list).is_not_empty()
    site = sites[0]
    assert_that(site).is_type_of(dict)
    assert_that(site).contains_key('street1')
    assert_that(site).contains_key('street2')
    assert_that(site).contains_key('state')
    assert_that(site).contains_key('city')
    assert_that(site).contains_key('country')


@pytest.mark.vcr()
def test_create_object_site(client: Client):
    # Act
    site = client.create_object("site", {
        'name':'Test site 123',
        'info':'A site created by automated testing (netdot-sites-manager).'
    })

    # Assert
    assert_that(site['name']).is_equal_to('Test site 123')


@pytest.mark.vcr()
def test_delete(client: Client):
    # Act
    client.delete_object_by_id("site", 738)

    # Assert
    assert_that(client.get_object_by_id).raises(ValueError).when_called_with('site', 738)

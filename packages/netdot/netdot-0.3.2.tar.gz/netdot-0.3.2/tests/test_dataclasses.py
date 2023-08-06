from assertpy import assert_that

import netdot.dataclasses as dataclasses


def test_replace():
    # Arrange
    dataclasses.initialize()
    site = dataclasses.Site(
        name='Test netdot-sites-manager package', 
        info="""Created to test the netdot-sites-manager Python package. 
            See more in the project's user guide: 
            https://git.uoregon.edu/projects/ISN/repos/netdot-sites-manager/browse/docs/user-guide.md"""
    )

    # Act
    updated_site = site.replace(name=f'UPDATED: {site.name}')

    # Assert
    assert_that(updated_site.name).starts_with('UPDATED: ')


def test_Device_initialization():
    # Act
    dataclasses.initialize()

    # Assert
    assert_that(dataclasses.Device._initialized).is_true()
    assert_that(vars(dataclasses.Device).keys()).contains('with_asset')
    assert_that(vars(dataclasses.Device).keys()).contains('with_site')
    assert_that(vars(dataclasses.Device).keys()).contains('load_site')
    assert_that(vars(dataclasses.Device).keys()).contains('get_site')


def test_Site_initialization():
    # Act
    dataclasses.initialize()

    # Assert
    assert_that(dataclasses.Site._initialized).is_true()
    assert_that(vars(dataclasses.Site).keys()).contains('load_devices')
    assert_that(vars(dataclasses.Site).keys()).contains('load_devices')


def test_Product_initialization():
    # Act
    dataclasses.initialize()

    # Assert
    assert_that(dataclasses.Site._initialized).is_true()
    assert_that(vars(dataclasses.Site).keys()).contains('load_devices')
    assert_that(vars(dataclasses.Site).keys()).contains('load_devices')


def test_with_asset_setter():
    # Arrange
    device = dataclasses.Device()
    my_asset = dataclasses.Asset(info='Testing')

    # Asset
    device.with_asset(my_asset)

    # Assert
    assert_that(device.get_asset()).is_equal_to(my_asset)

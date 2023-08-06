This project follows [Semantic Versioning](https://semver.org/).

> Notice: Major version zero (0.y.z) is for initial development. Anything MAY change at any time. 
> This public API should **not** be considered stable.

> ⚠ Disclaimer: From 0.2.0 onward, this API wrapper does not ensure support for the [de facto Open Source version of NetDot (GitHub)](https://github.com/cvicente/Netdot).

## 0.3.2

* Enable looking up a DNS Resource Record (RR) by address, using `repo.get_rr_by_address()`

## 0.3.1

* Speed up `find_edge_port`.
  * HTTP requests are parallelized via multithreading where possible.

## 0.3.0

> ⚠ Breaking Backwards Compatibility: Several `netdot.Repository` methods are renamed, as discussed below.

* Add `Repository.find_edge_port(mac_address)` method.
  * This requires a lot of HTTP requests since we do not have the ability to run arbitrary database queries (SQL JOIN behavior is unavailable via RESTful interface).
* Wired up the following netdot.dataclasses: 
  * `ForwardingTable`
  * `ForwardingTableEntry`
  * `PhysAddr`
* Renamed several generated methods to end in "ies" instead of "ys" when pluralized.
* Dropping Python 3.6 and 3.7 compatibility (required to use [hatch](https://github.com/pypa/hatch))


## 0.2.6

* Fix typo in `MACAddress:format` method argument: "delimeter" becomes "delimiter"
  * Additionally, force keyword arguments for the `format`using Python 3 feature.  

## 0.2.5

* In `netdot.Client` the base `delete(..., id)` method can now accept an `int`.
    * Before, it only accepted `str`.

## 0.2.4

* Gracefully handle response from HTTP Delete requests when possible.
  * Delete seems to return 'empty' (a couple of newlines actually) on success.

## 0.2.3

* Enable a `replace` function for all `netdot.dataclassess`
  * This makes it easier to do 'update' like operations using this library.

## 0.2.2

* Fix for REGRESSION: The `post` method of `netdot.Client` does not work.
  * Debugged using a simple automated test (captured by a PyVCR Cassette for reproducibility)


## 0.2.1

> 🐛 REGRESSION: The `post` method of `netdot.Client` does not work!

* Fix for REGRESSION: The `netdot.Client.Connection` class is missing!
  * Re-added `Connection` directly to client.py for now. 
  * Aliased `netdot.client` module to also be available as it was formerly named, `netdot.Client` (pep8 suggests lowercase module names instead of CamelCase).
    * Using `__all__` in "netdot/\_\_init\_\_.py" 


## 0.2.0 

> 🐛 REGRESSION: The `netdot.Client.Connection` class is MISSING!

> ⚠ We have not ensured support for the [de facto Open Source version of NetDot (GitHub)](https://github.com/cvicente/Netdot).

* Introducing a new layer of abstraction -- a Repository and many Python dataclasses.
    * See more info in the [User Guide](user-guide.md)
* Provide technical documentation in "docs/" directory (following NTS's standards).
    * See [the README.md in the "docs/" directory](README.md) for an overview.

## 0.1.0

* Provide Python Netdot Client, as originally authored by Francisco Gray.

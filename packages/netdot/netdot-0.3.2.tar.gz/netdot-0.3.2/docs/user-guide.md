A python wrapper for UO-NetDot's RESTful API.

> ⚠ Disclaimer: From 0.2.0 onward, this API wrapper does not ensure support for the [de facto Open Source version of NetDot (GitHub)](https://github.com/cvicente/Netdot).

[![PyPI version](https://badge.fury.io/py/netdot.svg)](https://badge.fury.io/py/netdot)

# Install 

This package is deployed to pypi.org.
Download it with `pip`:

    pip install netdot

# Interactive Usage (Python interpreter)

> ℹ Many methods of `netdot.Repository` and `netdot.dataclasses` are actually runtime-generated code.
> So, using the Repository interactively at the interpreter allows using features like tab completion and ['`help()`' function (discussed in Appendix below)](#appendix-using-help-in-interpreter) to learn more. 

Before getting into building a massive integration/tool, you might jump in and get some experience.
Thankfully, we have the [Python interpreter](https://docs.python.org/3/tutorial/interpreter.html) where we can jump in and do some testing!

    # Enter the Python interpreter by running just "python" in your shell
    $ python
    Python 3.6.15 (default, Sep 10 2021, 00:26:58) 
    ... omitted for brevity...
    >>> import netdot
    >>>

> ℹ The Python interpreter is often referred to as 'a REPL' (Read-Eval-Print-Loop).
> If you are unfamiliar with the Python interpreter, aka 'REPL', you might want to get started by reading ["Using the REPL (in VSCode)" documentation](https://www.learnpython.dev/01-introduction/02-requirements/05-vs-code/04-the-repl-in-vscode/).

With the netdot package imported, you can proceed with setting up a connecting and downloading some data!

## Connecting in the interpreter: `netdot.connect()`

We have enabled interpreter-usage as a first-class feature.
In particular, you will want to use the `connect` function like the following.

> `netdot.connect()` returns a `netdot.Repository` instance.

    >>> import netdot
    >>> repo = netdot.connect()
    What is the URL of the NetDot server? [https://nsdb.uoregon.edu]: ('enter' to use default)
    NetDot username: myusername
    NetDot password: ********** (using getpass module, to securely collect password)

That `repo` can be used for some interactive viewing of NetDot's data.

### Example: Lookup IP Address in interpreter

As an example, you can use this API to lookup an IP Address.

    >>> ipaddr = repo.get_ipblock_by_address('128.223.61.69')

Lets assume we want to determine who all may depend on this IP Address.
We'll see if we can discover useful information from the `used_by` field of this IP Address, or its Subnet...

    >>> ipaddr.used_by
    None
    >>> subnet = ipaddr.get_parent()
    >>> subnet.used_by
    'Network & Telecom Services'
    >>> ip_container = subnet.get_parent()
    >>> ip_container.used_by
    'University of Oregon (3582)'

This demonstrates programatic read-access to the Address Space in NetDot.

> ℹ Similar to `get_parent`, you'll notice you can `get_children` if you would like to!

### Example: Lookup DNS Record by Address 

As an example, you can use this API to lookup the DNS Resource Record (RR) associated to some IP Address.

    >>> dns_record = repository.get_rr_by_address('128.223.37.93')

The RR contains several pieces of information that may be useful!

    >>> dns_record.info
    'LOC: 215A Oregon Hall CON: Chris LeBlanc, 6-2931 '

### Example: Lookup Edge Port for MAC Address in NetDot

> **⚠ WARNING**: "find_edge_port" includes assumptions that can result in inaccurate results.
> See full warning at end of this section for more info.

As an example, you can use this API to lookup the Edge Port associated to some MAC Address.

> ℹ Tip: This is useful for tracking down the physical location of some MAC Address.
> 
> ℹ Info: This requires a LOT of HTTP requests.
> HTTP requests are [parallelized via multithreading (discussed below)](#multithreading-for-parallelizing-http-requests).

    >>> interface = repository.find_edge_port('8C3BADDA9EF1')

Once the interface lookup is complete (may take more than 60 seconds), it is very easy to check if there is any "`jack`" (location information) associated to this Interface!

    >>> interface.jack
    '146A010B'

> **⚠ WARNING**: "find_edge_port" includes assumptions that can result in inaccurate results. 
> (This issue is present when looking up an edge port using NetDot's frontend as well)
> 
> Particularly, **if more than one forwarding table contains the MAC Address**, then NetDot will select the one whose forwarding table had the least entries.
>
> This can be inaccurate especially if a forwarding table scan is happening while trying to `find_edge_port`.

### Example: Update 'aliases' of Sites in NetDot

As a simple script example, imagine we want to update the 'aliases' with the string "(odd layout)" for some set of sites in NetDot.
In this example, we will write a script to do just that.

> For those who want to just see the script, there is the [full code sample below](#code-sample-for-example-update-aliases-of-sites-in-netdot)

For starters, we need to set up a `Repository` to interact with NetDot.

    import netdot
    repo = netdot.Repository(...)  # Provide credentials, e.g. via environment variables using `os` module

Now, we are given a list of `SITE_IDS` to which we want to update the 'alias' with the string "(odd layout)". 
We can use Python list comprehensions along with the handy `replace()` method!

> Note that all `site`'s fields may be referenced when using the `site.replace()` method!

    SITE_IDS = [98, 124, 512, 123, 111]
    sites = [ repo.get_site(id) for id in SITE_IDS ]
    updated_sites = [ site.replace(aliases=f'{site.aliases}(odd layout)') for site in sites ]

Then, it is time to actually apply the updates to NetDot!

    for updated_site in updated_sites:
        response = repo.update_site(updated_site.id, updated_site)
        print(response)


#### Code Sample for Example: Update 'aliases' of Sites in NetDot

The full code sample is provided here.

    import netdot
    
    repo = netdot.Repository(...)  # Provide credentials, e.g. via environment variables using `os` module

    SITE_IDS = [98, 124, 512, 123, 111]
    sites = [ repo.get_site(id) for id in SITE_IDS ]
    updated_sites = [ site.replace(aliases=f'{site.aliases}(odd layout)') for site in sites ]

    for site in sites:
        response = repo.update_site(site.id, updated_site)
    

# Primary Interface: `netdot.Repository`

> `netdot.Repository` is the type of object that gets returned from the `netdot.connect()` function.

The `netdot.Repository` class is the primary interface of this package.
It provides many methods to download data from NetDot (e.g. get_site, get_device, get_devices_by_site, get_all_sites...)

> **⚠ NOTE**: ... Work in progress!!
> 
> There are several NetDot entities that need to be added to this `netdot.Repository` interface!
>
> In the meantime, consider using the [Legacy Interface (discussed below)](#legacy-interface-netdotclientconnect) for anything not found here.

## Multithreading for Parallelizing HTTP Requests

The `netdot.Repository` class provides parallelization by multithreading HTTP requests when possible.

Change the number of threads by passing the `threads` keyword argument to the constructor.

    >>> repo = netdot.Repository(..., threads=4)

This `threads` keyword argument can be used in the [interactive interface (discussed above)](#interactive-usage-python-interpreter) as well.

    >>> repo = netdot.connect(threads=2)

# Legacy Interface: `netdot.Client.Connect()`

The legacy `netdot.Client.Connect()` class is still available at this time!
This can be used to access all aspects of the NetDot RESTful API.

See the legacy example code that was provided with this Connect class:

> ⚠ This example has been untested for a very long time!

    #!/usr/bin/env python2.7
    import sys
    import os
    import netdot

    uname = 'my_user'
    pword = 'my_pass'
    server = "https://netdot.localdomain/netdot"
    debug = 1

    dot = netdot.Client.Connect(uname, pword, server, [debug])

    # Direct GET/POST/DELETE calls
    r = dot.get('/host?name=my-server-name')
    r = dot.post('/host', host)

    name = dot.get_host_by_name('foo')
    cname = dot.add_cname_to_record('foo','bar.foo.example.com')
    ipid = dot.get_host_by_ipid('11111')
    rrid = dot.get_host_by_rrid('11111')

    ipblock =  dot.get_ipblock("184.171.96.0/24")
    user = dot.get_person_by_username('mary')
    user_id = dot.get_person_by_id('111')

    host = {
        'name':'my-server', 
        'subnet':'192.168.1.0/24', 
        'ethernet':'XX:XX:XX:XX:XX:XX',
        'info':'My Server'
    }
    r = dot.create_host(host)

    print r

# Appendix: Using `help()` in interpreter

When in the interpreter session, it can be very useful to run `help(netdot.Repository)` to learn more about the Repository's capabilities.

> ℹ If you've already established a connection via `repo = netdot.connect()`, then you can run `help(repo)` instead!

    >>> help(netdot.Repository)
    class Repository(builtins.object)
    |  Work with Netdot API using Python objects.
    |  
    |  Methods defined here:
    |  
    |  __init__(self, netdot_url, user, password, parallelization_factor=11, **kwargs)
    |      Initialize self.  See help(type(self)) for accurate signature.
    |  
    |  get_asset(repo:netdot_sites_manager.netdot.repository.Repository, id:int) -> ~T
    |      Get info about a Asset from Netdot.
    |      
    |      Args: ... trimmed for brevity...
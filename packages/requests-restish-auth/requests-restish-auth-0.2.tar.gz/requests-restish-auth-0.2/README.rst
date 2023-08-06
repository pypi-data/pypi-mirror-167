Requests Restish Auth
=====================

This package lets you shell-out to `restish`_ for negotiating a bearer token
with an OIDC provider, and use that token for authenticating requests.

.. _restish: https://rest.sh


Installation
------------

::

    pip install requests-restish-auth

Usage
-----

.. code-block:: python

    import requests
    from restish_auth import RestishAuth

    auth = RestishAuth("my-restish-api-name")
    response = requests.get("https://my-api-endpoint.com/", auth=auth)

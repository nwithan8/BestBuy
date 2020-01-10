Python Best Buy API Wrapper
===========================

This is a small Python wrapper implementation for BestBuy APIs. This was originally
forked from an earlier version from https://github.com/lv10, but was **later
rewritten from scratch**. This implementation aims to implement all of the public APIs
from BestBuy, including the Products, Stores, Categories, Open Box, Recommendations
and Smart Lists APIs.

The wrapper does not alter any of the values returned by the Best Buy APIs. The raw
JSON data from Best Buy is converted into an object with attributes that can be used.
This library merely simplifies the process of calling the API by handling query structure,
GET requests and JSON parsing behind the scenes.

How to Product and Category APIs
--------------------------------

.. code-block:: python

    >>> import bestbuy
    >>> product_api = bestbuy.ProductAPI("YourSecretAPIKey")
    >>> category_api = bestbuy.CategoryAPI("YourSecretAPIKey")
    >>>
    >>> product_api.search_by_sku(sku=9776457)
    >>> category_api.search_by_category_id(category_id="abcat0011001")

How to get a BestBuy API Key
----------------------------

Visit https://developer.bestbuy.com/

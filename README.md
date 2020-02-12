Python Best Buy API Wrapper
===========================

This is a simple Python wrapper implementation for most of BestBuy APIs. This was originally
forked from an earlier version from [lv10](https://github.com/lv10), but was **later
rewritten from scratch**. This implementation aims to implement all of the public APIs
from BestBuy, including the Products, Stores, Categories, Open Box, Recommendations
and Smart Lists APIs.

The wrapper does not alter any of the values returned by the Best Buy APIs. The raw
JSON data from Best Buy is converted into an object with attributes that can be used.
This library merely simplifies the process of calling the API by handling query structure,
GET requests and JSON parsing behind the scenes.

Example of using Product, Store and Category APIs
--------------------------------

```python
    from bestbuy.apis import BestBuy
    bb = BestBuy("YourSecretAPIKey")
    
    bb.ProductAPI.search_by_sku(sku=9776457)
    bb.ProductAPI.search(searchTerm="hard drive", onSale="true")
    bb.StoreAPI.search_by_city(city="Atlanta")
    bb.CategoryAPI.search_by_category_id(category_id="abcat0011001")
```

How to get a BestBuy API Key
----------------------------

Visit [Best Buy's Developer portal](https://developer.bestbuy.com/)

Installation
---------------------------

Download from [PyPi](https://pypi.org/project/bestbuy/) with ``pip3 install bestbuy``


Documentation
-----------------------------
### ProductAPI:
Returns a list of Product objects
    
#### Methods:
* search_by_sku(sku=1234)
* search_by_upc(upc=4321)
* search_by_description(description="hard drive")
* search(searchTerm="tv", \*\*kwargs)

    *Available kwargs:*
        bestSellingRank,
        color,
        categoryPath.id,
        categoryPath.name,
        condition,
        customerReviewAverage,
        customerReviewCount,
        description,
        dollarSavings,
        freeShipping = true|false,
        inStoreAvailability = true|false,
        manufacturer,
        modelNumber,
        name,
        onlineAvailability = true|false,
        onSale = true|false,
        percentSavings,
        preowned = true|false,
        regularPrice,
        salePrice,
        shippingCost,
        sku,
        type,
        upc


### StoreAPI:
Returns a list of Store objects
    
#### Methods:
* search_by_postal_code(postal_code=30307, (*Optional*) distance, (*Optional*) store_services=[], (*Optional*) store_type=[])
* search_by_city(city="Atlanta", (*Optional*) store_services=[], (*Optional*) store_type=[])
* search_by_lat_long(lat=###, long=###, distance=###, (*Optional*) store_services=[], (*Optional*) store_type=[])
* search_by_store_id(store_id=###, (*Optional*) store_services=[], (*Optional*) store_type=[])
* search_by_region_state(region_state="Georgia", (*Optional*) store_services=[], (*Optional*) store_type=[])
        
        
### CategoryAPI:
Returns a list of Category objects
    
#### Methods:
* search_all_categories()
* search_top_level_categories()
* search_by_category_name(category_name="TVs")
* search_by_category_id(category_id=1234)
        
        
### RecommendationAPI:
Returns a list of Recommendation objects
    
#### Methods:
* most_popular_by_category_id(category_id=1234)
* trending_by_category_id(category_id=1234)
        
        
### OpenBoxAPI:
Returns a list of OpenBox objects
    
#### Methods:
* all_open_box_offers()
* open_box_offers_by_skus(skus=[])
* open_box_offers_by_category_id(category_id=1234)

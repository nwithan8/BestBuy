#!/usr/bin/python3

import requests
import json
from collections import namedtuple
from bestbuy.objects import *

api_key = None


def _query(version, query, category, sort=None):
    """
    Make API call
    Return JSON
    """
    return requests.get(
        'https://api.bestbuy.com/{version}/{category}{query}?apiKey={key}{sort}&format=json'.format(version=version,
                                                                                                    category=category,
                                                                                                    query=query,
                                                                                                    key=api_key,
                                                                                                    sort=(
                                                                                                        sort if sort else ""))).json()


def connected_home_smart_list():
    return _query('beta/products', '', 'connectedHome')


def active_adventurer_smart_list():
    return _query('beta/products', '', 'activeAdventurer')


class BestBuy:
    """
    TODO: Add Results Per Page option
    """

    def __init__(self, key):
        global api_key
        api_key = key
        self.ProductAPI = ProductAPI()
        self.StoreAPI = StoreAPI()
        self.RecommendationAPI = RecommendationAPI()
        self.CategoryAPI = CategoryAPI()
        self.OpenBoxAPI = OpenBoxAPI()


class StoreAPI:
    """
    TODO: Store type and services filters
    """

    category = 'stores'

    def _post_query(self, query):
        store_list = _query('v1', '({0})'.format(query), self.category, None).get('stores', [])
        return [Store(store) for store in store_list]

    def search_by_postal_code(self, postal_code, distance=None, store_services=[], store_type=[]):
        """
        Returns multiple Store objects
        """
        query = ""
        if store_type:
            query = query + '&('
            for storeType in store_type:
                query = query + "(storeType={0})|".format(storeType)
            query = query[:-1] + ")"
        if store_services:
            query = query + '&('
            for service in store_services:
                query = query + "(services.service=\"{0}\")&".format(service)
            query = query[:-1] + ")"
        if distance:
            return self._post_query('(area({0},{1}))'.format(str(postal_code), str(distance)))
        return self._post_query('(postalCode={0}){1}'.format(str(postal_code, query)))

    def search_by_city(self, city, store_services=[], store_type=[]):
        """
        Returns multiple Store objects
        """
        query = ""
        if store_type:
            query = query + '&('
            for storeType in store_type:
                query = query + "(storeType={0})|".format(storeType)
            query = query[:-1] + ")"
        if store_services:
            query = query + '&('
            for service in store_services:
                query = query + "(services.service=\"{0}\")&".format(service)
            query = query[:-1] + ")"
        return self._post_query('(city={0}){1}'.format(city, query))

    def search_by_lat_long(self, latitude, longitude, distance, store_services=[], store_type=[]):
        """
        Returns multiple Store objects
        """
        query = ""
        if store_type:
            query = query + '&('
            for storeType in store_type:
                query = query + "(storeType={0})|".format(storeType)
            query = query[:-1] + ")"
        if store_services:
            query = query + '&('
            for service in store_services:
                query = query + "(services.service=\"{0}\")&".format(service)
            query = query[:-1] + ")"
        return self._post_query('(area({0},{1},{2}){3}'.format(str(latitude), str(longitude), str(distance), query))

    def search_by_store_id(self, store_id, store_services=[], store_type=[]):
        """
        Returns one Store object
        """
        query = ""
        if store_type:
            query = query + '&('
            for storeType in store_type:
                query = query + "(storeType={0})|".format(storeType)
            query = query[:-1] + ")"
        if store_services:
            query = query + '&('
            for service in store_services:
                query = query + "(services.service=\"{0}\")&".format(service)
            query = query[:-1] + ")"
        try:
            return self._post_query('(storeId={0}){1}'.format(str(store_id), query))[0]
        except IndexError:
            return None

    def search_by_region_state(self, region_state, store_services=[], store_type=[]):
        """
        Returns multiple Store objects
        """
        query = ""
        if store_type:
            query = query + '&('
            for storeType in store_type:
                query = query + "(storeType={0})|".format(storeType)
            query = query[:-1] + ")"
        if store_services:
            query = query + '&('
            for service in store_services:
                query = query + "(services.service=\"{0}\")&".format(service)
            query = query[:-1] + ")"
        return self._post_query('(region={0}){1}'.format(region_state), query)


class ProductAPI:
    """
    TODO: Document Sort params
    """

    category = 'products'

    def _post_query(self, query, sort=None):
        """
        Call API

        :param query: query against the API

        Return Product object(s)
        """
        product_list = _query('v1', query, self.category,
                              '&sort={0}.asc'.format(sort) if sort else None).get('products', [])
        return [Product(product) for product in product_list]

    def search_by_sku(self, sku, sort=None):
        """
        Search by SKU number

        :param sort:
        :param sku: SKU number

        Returns one Product object
        """
        try:
            return self._post_query('(sku={0})'.format(str(sku)), sort)[0]
        except IndexError:
            return None

    def search_by_upc(self, upc, sort=None):
        """
        Search by UPC number

        :param sort:
        :param upc: UPC number

        Returns one Product object
        """
        try:
            return self._post_query('(upc={0})'.format(str(upc)), sort)[0]
        except IndexError:
            return None

    def search_by_description(self, description, sort=None):
        """
        Search by product description

        :param sort:
        :param description: Product description to search

        Returns multiple Product objects
        """
        return self._post_query('(description={0})'.format(description), sort=None)

    def search(self, searchTerm=None, **kwargs):
        """
        General search

        :param searchTerm: Keyword or phrase to search for
        :param **kwargs: Available options:
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


        Returns multiple Product objects
        """
        if not searchTerm:
            searchTerm = ""
        else:
            searchTerm = '(search={})&'.format(searchTerm)
        if kwargs:
            for key, value in kwargs.items():
                searchTerm = '{s}{k}={v}&'.format(s=searchTerm, k=key, v=value)
            searchTerm = '({})'.format(searchTerm[:-1])
        return self._post_query(searchTerm)


class RecommendationAPI:

    def _post_query(self, query, endpoint):
        recommendation_list = _query('beta/products', '{0}'.format(query), endpoint, None).get('results', [])
        return [Recommendation(recommendation) for recommendation in recommendation_list]

    def most_popular_by_category_id(self, category_id):
        return self._post_query('(categoryId={0})'.format(str(category_id)), 'mostViewed')

    def trending_by_category_id(self, category_id):
        return self._post_query('(categoryId={0})'.format(str(category_id)), 'trendingViewed')


class CategoryAPI:
    category = 'categories'

    def _post_query(self, query):
        category_list = _query('v1', '{0}'.format(query), self.category, None).get('categories', [])
        return [Category(category) for category in category_list]

    def search_all_categories(self):
        return self._post_query('')

    def search_top_level_categories(self):
        return self._post_query('(id=abcat*)')

    def search_by_category_name(self, category_name):
        return self._post_query('(name={0}*)'.format(str(category_name)))

    def search_by_category_id(self, category_id):
        return self._post_query('(id={0})'.format(str(category_id)))


class OpenBoxAPI:
    category = 'openBox'

    def _post_query(self, query, sort=None):
        openBox_list = _query('beta/products', query, self.category, None).get('results', [])
        return [OpenBox(openBox) for openBox in openBox_list]

    def all_open_box_offers(self):
        return self._post_query('')

    def open_box_offers_by_skus(self, skus):
        query = ""
        for sku in skus:
            query = str(sku) + ", "
        query = query[:-2]
        return self._post_query('(sku%20%in({0}))'.format(query))

    def open_box_offers_by_category_id(self, category_id):
        return self._post_query('(categoryId={0})'.format(str(category_id)))

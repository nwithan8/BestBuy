#!/usr/bin/python3
from typing import Union, List

import requests
from bestbuy.classes import Store, Product, OpenBox, Category, Recommendation


class BestBuy:
    """
    TODO: Add Results Per Page option
    """

    def __init__(self,
                 api_key: str,
                 raw_json: bool = False,
                 verbose: bool = False):
        self.key = api_key
        self.raw = raw_json
        self.verbose = verbose
        self.ProductAPI = ProductAPI(best_buy=self)
        self.StoreAPI = StoreAPI(best_buy=self)
        self.RecommendationAPI = RecommendationAPI(best_buy=self)
        self.CategoryAPI = CategoryAPI(best_buy=self)
        self.OpenBoxAPI = OpenBoxAPI(best_buy=self)

    def _query(self,
               version: str,
               query: str,
               category: str,
               sort: str = None) -> dict:
        """
        Make API call
        Return JSON
        """
        url = f'https://api.bestbuy.com/{version}/{category}{query}?apiKey={self.key}{sort if sort else ""}&pageSize=100&format=json'
        if self.verbose:
            print(f"GET {url}")
        res = requests.get(url)
        if res:
            return res.json()
        return {}

    @property
    def open_box_offers(self) -> Union[dict, List[OpenBox]]:
        return self.OpenBoxAPI.all_open_box_offers()

    @property
    def categories(self) -> Union[dict, List[Category]]:
        return self.CategoryAPI.search_all_categories()

    @property
    def top_level_categories(self) -> Union[dict, List[Category]]:
        return self.CategoryAPI.search_top_level_categories()

class Lists:

    def __init__(self,
                 best_buy: BestBuy):
        self._best_buy = best_buy

    @property
    def connected_home_smart_list(self) -> dict:
        return self._best_buy._query(version='beta/products',
                                     query='',
                                     category='connectedHome')

    @property
    def active_adventurer_smart_list(self) -> dict:
        return self._best_buy._query(version='beta/products',
                                     query='',
                                     category='activeAdventurer')


class StoreAPI:
    """
    TODO: Store type and services filters
    """

    category = 'stores'

    def __init__(self,
                 best_buy: BestBuy):
        self._best_buy = best_buy

    @property
    def store_types(self):
        return ["Big Box", "Express Kiosk", "Warehouse Sale", "Outlet Center", "PAC Standalone Store"]

    def _get_query(self,
                   query: str) -> Union[dict, List[Store]]:
        store_list = self._best_buy._query(version='v1',
                                           query=f'({query})',
                                           category=self.category)
        if self._best_buy.raw:
            return store_list.get('stores', {})
        return [Store(store, best_buy=self._best_buy) for store in store_list.get('stores', [])]

    def _add_store_types_and_services(self,
                                      store_services: List[str] = None,
                                      store_types: List[str] = None) -> str:
        query = ""
        if store_types:
            filtered_store_types = []
            for store_type in store_types:
                if store_type in self.store_types:
                    filtered_store_types.append(store_type)
            query += '&(' + "|".join(f"storeType={store_type}" for store_type in filtered_store_types) + ")"
        if store_services:
            query += '&(' + "&".join(f'services.service="{service}"' for service in store_services) + ")"
        return query

    def search_by_postal_code(self,
                              postal_code: int,
                              distance: int = None,
                              store_services: List[str] = None,
                              store_types: List[str] = None) -> Union[dict, List[Store]]:
        """
        Returns Store objects
        """
        prefix = f'(postalCode={postal_code})'
        if distance:
            prefix = f'(area({postal_code},{distance})'
        query = f"{prefix}{self._add_store_types_and_services(store_services=store_services, store_types=store_types)}"
        return self._get_query(query=query)

    def search_by_city(self,
                       city: str,
                       store_services: List[str] = None,
                       store_types: List[str] = None) -> Union[dict, List[Store]]:
        """
        Returns Store objects
        """
        query = f"(city={city}){self._add_store_types_and_services(store_types=store_types, store_services=store_services)}"
        return self._get_query(query=query)

    def search_by_lat_long(self,
                           latitude: float,
                           longitude: float,
                           distance: int,
                           store_services: List[str] = None,
                           store_types: List[str] = None) -> Union[dict, List[Store]]:
        """
        Returns Store objects
        """
        query = f'(area({latitude},{longitude},{distance}){self._add_store_types_and_services(store_services=store_services, store_types=store_types)}'
        return self._get_query(query=query)

    def search_by_store_id(self,
                           store_id: int,
                           store_services: List[str] = None,
                           store_types: List[str] = None) -> Union[dict, List[Store]]:
        """
        Returns Store objects
        """
        query = f'(storeId={store_id}){self._add_store_types_and_services(store_services=store_services, store_types=store_types)}'
        return self._get_query(query=query)

    def search_by_region_state(self,
                               region_state: str,
                               store_services: List[str] = None,
                               store_types: List[str] = None) -> Union[dict, List[Store]]:
        """
        Returns Store objects
        """
        query = f'(region={region_state}){self._add_store_types_and_services(store_services=store_services, store_types=store_types)}'
        return self._get_query(query=query)

    def product_availability(self,
                             sku: int,
                             store_id: int = None,
                             postal_code: int = None) -> Union[dict, List[Store]]:
        if not store_id and not postal_code:
            return []
        store_list = self._best_buy._query(version='v1',
                                           query='stores.json',
                                           category=f"products/{sku}/",
                                           sort=f"&storeId={store_id}" if store_id else f"&postalCode={postal_code}")
        if self._best_buy.raw:
            return store_list.get('stores', {})
        return [Store(store, best_buy=self._best_buy) for store in store_list.get('stores', [])]


class ProductAPI:
    """
    TODO: Document Sort params
    """

    category = 'products'

    def __init__(self,
                 best_buy: BestBuy):
        self._best_buy = best_buy

    def _get_query(self,
                   query: str,
                   sort: str = None) -> Union[dict, List[Product]]:
        """
        Call API

        :param query: query against the API

        Return Product object(s)
        """
        product_list = self._best_buy._query(version='v1',
                                             query=query,
                                             category=self.category,
                                             sort=f'&sort={sort}.asc' if sort else None)
        if self._best_buy.raw:
            return product_list.get('products', {})
        return [Product(product, best_buy=self._best_buy) for product in product_list.get('products', [])]

    def search_by_sku(self,
                      sku: int,
                      sort: str = None) -> Union[dict, List[Product]]:
        """
        Search by SKU number

        :param sort:
        :param sku: SKU number

        Returns Product objects
        """
        return self._get_query(query=f'(sku={sku})', sort=sort)

    def search_by_upc(self,
                      upc: int,
                      sort: str = None) -> Union[dict, List[Product]]:
        """
        Search by UPC number

        :param sort:
        :param upc: UPC number

        Returns Product objects
        """
        return self._get_query(query=f'(upc={upc})', sort=sort)

    def search_by_description(self,
                              description: str,
                              sort: str = None) -> Union[dict, List[Product]]:
        """
        Search by product description

        :param sort:
        :param description: Product description to search

        Returns Product objects
        """
        return self._get_query(query=f'(description={description})', sort=sort)

    @property
    def search_parameters(self) -> List[str]:
        return ["bestSellingRank",
                "color",
                "condition",
                "customerReviewAverage",
                "customerReviewCount",
                "description",
                "dollarSavings",
                "freeShipping",
                "inStoreAvailability",
                "manufacturer",
                "modelNumber",
                "name",
                "onlineAvailability",
                "onSale",
                "percentSavings",
                "regularPrice",
                "salePrice",
                "shippingCost",
                "sku",
                "type",
                "upc"]

    def _bool_to_string(self,
                        boolean: bool) -> str:
        if boolean:
            return 'true'
        return 'false'

    def _lowercase_string(self,
                          string: str) -> str:
        return string.lower()

    def _split_argument(self,
                        argument: str) -> [str, str, str]:
        sign = "="
        if "<=" in argument:
            sign = "<="
        if ">=" in argument:
            sign = ">="
        argument.replace(sign, "=")
        k, v = argument.split("=")
        return k, sign, v

    def _clean_parameters(self,
                          *args) -> List[str]:
        final_args = []
        for arg in args:
            k, sign, v = self._split_argument(argument=arg)
            if k in self.search_parameters:
                if k in ['onSale', 'onlineAvailability', 'inStoreAvailability', 'freeShipping']:
                    final_v = self._lowercase_string(string=v)
                else:
                    final_v = v
                final_args.append(f"{k}{sign}{final_v}")
        return final_args

    def search(self,
               keyword: str = None,
               *args) -> Union[dict, List[Product]]:
        """
        General search

        :param keyword: Keyword or phrase to search for
        :param *args: Available options:
            bestSellingRank,
            color,
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


        Returns Product objects
        """
        if not keyword:
            keyword = ""
        else:
            keyword = f'(search={keyword})'
        if args:
            keyword += '&' + "&".join(f"{k}" for k in self._clean_parameters(*args))
            keyword = f'({keyword})'
        return self._get_query(query=keyword)

    def also_viewed(self, sku: int) -> Union[dict, List[Product]]:
        product_list = self._best_buy._query(version='beta/products',
                                             query='',
                                             category=f"{sku}/alsoViewed")
        if self._best_buy.raw:
            return product_list.get('results', {})
        return [Product(product, best_buy=self._best_buy) for product in product_list.get('results', [])]


class RecommendationAPI:

    def __init__(self,
                 best_buy: BestBuy):
        self._best_buy = best_buy

    def _get_query(self,
                   query: str,
                   endpoint: str) -> Union[dict, List[Recommendation]]:
        recommendation_list = self._best_buy._query(version='beta/products',
                                                    query=f'{query}',
                                                    category=endpoint)
        if self._best_buy.raw:
            return recommendation_list.get('results', {})
        return [Recommendation(recommendation, best_buy=self._best_buy) for recommendation in recommendation_list.get('results', [])]

    def most_popular_by_category_id(self,
                                    category_id) -> Union[dict, List[Recommendation]]:
        return self._get_query(query=f'(categoryId={category_id})', endpoint='mostViewed')

    def trending_by_category_id(self,
                                category_id) -> Union[dict, List[Recommendation]]:
        return self._get_query(query=f'(categoryId={category_id})', endpoint='trendingViewed')


class CategoryAPI:

    category = 'categories'

    def __init__(self,
                 best_buy: BestBuy):
        self._best_buy = best_buy

    def _get_query(self,
                   query: str) -> Union[dict, List[Category]]:
        category_list = self._best_buy._query(version='v1',
                                              query=f'{query}',
                                              category=self.category,
                                              sort=None)
        if self._best_buy.raw:
            return category_list.get('categories', {})
        return [Category(category, best_buy=self._best_buy) for category in category_list.get('categories', [])]

    def search_all_categories(self) -> Union[dict, List[Category]]:
        return self._get_query(query='')

    def search_top_level_categories(self) -> Union[dict, List[Category]]:
        return self._get_query(query='(id=abcat*)')

    def search_by_category_name(self,
                                category_name: str) -> Union[dict, List[Category]]:
        return self._get_query(query=f'(name={category_name}*)')

    def search_by_category_id(self,
                              category_id) -> Union[dict, List[Category]]:
        return self._get_query(query=f'(id={category_id})')


class OpenBoxAPI:

    category = 'openBox'

    def __init__(self,
                 best_buy: BestBuy):
        self._best_buy = best_buy

    def _get_query(self,
                   query: str,
                   sort: str = None) -> Union[dict, List[OpenBox]]:
        open_box_list = self._best_buy._query(version='beta/products',
                                             query=query,
                                             category=self.category,
                                             sort=sort)
        if self._best_buy.raw:
            return open_box_list.get('results', {})
        return [OpenBox(openBox, best_buy=self._best_buy) for openBox in open_box_list.get('results', [])]

    def all_open_box_offers(self) -> Union[dict, List[OpenBox]]:
        return self._get_query('')

    def open_box_offers_by_skus(self,
                                skus: List[int]) -> Union[dict, List[OpenBox]]:
        query = ", ".join(str(sku) for sku in skus)
        return self._get_query(query=f'(sku%20%in({query}))')

    def open_box_offers_by_category_id(self,
                                       category_id) -> Union[dict, List[OpenBox]]:
        return self._get_query(query=f'(categoryId={category_id})')

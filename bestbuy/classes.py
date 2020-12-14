# import json


def _make_object_from_json(json_data: dict, obj: object) -> bool:
    """
    Take key-value pairs from a JSON object and make them into attribute-value pairs for a Python object
    Object attributes will be named the same (with same case) as presented in the JSON object
    Existing attributes will be overwritten
    Automatic recursion down into sub-dictionaries
    :param json_data: JSON data to parse
    :param obj: Python object to add attributes to
    :return: None
    """
    for k, v in json_data.items():
        setattr(obj, k, v)
        """
        if isinstance(v, dict):
            _make_object_from_json(json_data=v, obj=obj)
        else:
            setattr(obj, k, v)
        """
    return True

class BaseObject:

    def __init__(self, data: dict, best_buy):
        self._data = data
        self._best_buy = best_buy
        _make_object_from_json(json_data=data, obj=self)

    def __getattr__(self, name) -> None:
        return None

class Category(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)

class Review(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)

class Prices(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)

class Recommendation(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)
        self._reviews = []
        self._prices = None
        self._images = []

    @property
    def reviews(self):
        if not self._reviews and self._data.get('customerReviews'):
            self._reviews = [Review(review) for review in self._data['customerReviews']]
        return self._reviews


class Store(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)


class Product(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)
        self._images = []

    @property
    def also_viewed(self):
        if self.sku:
            return self._best_buy.ProductAPI.also_viewed(sku=self.sku)
        return []

    def stores(self, postal_code: int = None, store_id: int = None):
        return self._best_buy.StoreAPI.product_availability(sku=self.sku, postal_code=postal_code, store_id=store_id)


class OpenBox(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)
        self._offers = []
        self._prices = None
        self._images = []


class Image(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)


class Offer(BaseObject):

    def __init__(self, data: dict, best_buy):
        super().__init__(data=data, best_buy=best_buy)
        self._prices = None
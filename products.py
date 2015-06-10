import requests

from constants import PRODUCT_SEARCH_PARAMS, PRODUCT_DESCRIPTION_TYPES, \
    BASE_URL


class BestBuyProductAPIError(Exception):

    """
        Errors generated before BestBuy servers respond to a call
    """
    pass


class BestBuyProductsAPI(object):

    def __init__(self, api_key):
        """
            :param api_key: best buy developer API key.
        """
        self.api_key = api_key.strip()
        self.api_query = None

    def _call(self, payload):
        """
            Actual call ot the Best Buy API.

            :rType: JSON
        """
        valid_payload = self._validate_params(payload)
        url, valid_payload = self._build_url(valid_payload)
        request = requests.get(url, pa=valid_payload)

        return request.json()

    def _build_url(self, payload):
        """
            Receives a payload (dict) with all the necessary make a call to
            the Best Buy API and returns a string URL that includes the query
            and the dict parameters pre-processed for a API call to be made.

            :param paylod: dictionary with request parameters

            :rType: tuple that contains the url that includes the query and
                    the parameters pre-processed for a API call to be made.
        """

        query = payload['query']

        # Pre-process paramenters before submitting payload.

        out = dict()

        for key, value in payload['params']:
            if type(value) is list:
                out[key] = ",".join(value)
            else:
                out[key] = value

        # Add key to params
        out['key'] = self.api_key

        url = BASE_URL + "({0})".format(query)

        return (url, out)

    def _validate_params(self, payload):
        """
            Validate parameters, double check that there are no None values
            in the keys.

            :param payload: dictionary, with the parameters to be used to make
                            a request.
        """

        for key, value in payload['params'].iteritems():

            if key not in PRODUCT_SEARCH_PARAMS:
                err_msg = ("{0} is an invalid Product"
                           " Search Parameter".format(key))
                raise BestBuyProductAPIError(err_msg)

            if value is None:
                err_msg = "Key {0} can't have None for a value".format(key)
                raise BestBuyProductAPIError(err_msg)

        return payload

    # =================================
    #   Search by description or SKU
    # =================================

    def search_by_description(self, description_type, description, **kwargs):
        """
            Searches the product API using description parameter

            :param description_type: Integer from 1 to 4 to determine the type
                                     of description the call is going to use.
                                     The integers represent:
                                     - 1: name
                                     - 2: description
                                     - 3: shortDescription
                                     - 4: longDescription
            :param description: String with the actual description's content.
        """
        d_type = PRODUCT_DESCRIPTION_TYPES[description_type]

        payload = {
            'query': "{0}={1}".format(d_type, description),
            'params': kwargs
        }

        return self._call(payload)

    def search_by_sku(self, sku, **kwargs):
        """
            Search the product API by SKU

            :param sky: string, with the SKU number of the desired product.
           :param kwargs: dictionary, with request parameters
        """
        payload = {
            'query': "sku={0}".format(sku),
            'params': kwargs
        }

        return self._call(payload)
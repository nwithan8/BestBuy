#!/usr/bin/python3

import requests
import json
import time
from collections import namedtuple

class BestBuy:
    
    """
    TODO: Add Results Per Page option
    """
    
    def __init__(self):
        pass
    
    def _query(self, version, query, category, api_key, sort=None):
        """
        Make API call
        Return JSON
        """
        return requests.get('https://api.bestbuy.com/{version}/{category}{query}?apiKey={key}{sort}&format=json'.format(version=version, category=category, query=query, key=api_key, sort=(sort if sort else ""))).json()
    
    def connected_home_smart_list(self):
        return self._query('beta/products', '', 'connectedHome')
    
    def active_adventurer_smart_list(self):
        return self._query('beta/products', '', 'activeAdventurer')
"""
class Store:
    json = None
    storeId = None
    storeType = None
    tradeIn = None
    brand = None
    name = None
    longName = None
    address = None
    city = None
    region = None
    postalCode = None
    country = None
    latitude = None
    longitude = None
    hours = None
    gmtOffset = None
    language = None
    phone = None
    services = []
    
    def __init__(self, json):
        self.json = json
        self.storeId = json['storeId']
        self.storeType = json['storeType']
        self.tradeIn = json['tradeIn']
        self.brand = json['brand']
        self.name = json['name']
        self.longName = json['longName']
        self.address = json['address'] + json['address2']
        self.city = json['city']
        self.region = json['region']
        self.postalCode = json['fullPostalCode']
        self.country = json['country']
        self.latitude = json['lat']
        self.longitude = json['lng']
        self.hours = json['hours']
        self.gmtOffset = json['gmtOffset']
        self.language = json['language']
        self.phone = json['phone']
        for service in json['services']:
            self.services.append(service['service'])
"""

class StoreAPI(BestBuy):
    """
    TODO: Store type and services filters
    """
    
    category = 'stores'
    api_key = None
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _post_query(self, query):
        stores = []
        store_list = super()._query('v1', '({0})'.format(query), self.category, self.api_key, None)['stores']
        for store in store_list:
            x = json.loads(json.dumps(store), object_hook=lambda d: namedtuple('Store', d.keys(), rename=True)(*d.values()))
            stores.append(x)
            #stores.append(Store(store))
        return stores
    
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
        return self._post_query('(storeId={0}){1}'.format(str(store_id), query))[0]
    
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

"""
class Recommendation:
    json = None
    sku = None
    customerReviewAverage = None
    customerReviewCount = None
    description = None
    images = None
    name = None
    regularPrice = None
    currentPrice = None
    productUrl = None
    webUrl = None
    addToCartUrl = None
    rank = None
    
    def __init__(self, json):
        self.json = json
        self.sku = json['sku']
        self.customerReviewAverage = json['customerReviews']['averageScore']
        self.customerReviewCount = json['customerReviews']['count']
        self.description = json['descriptions']['short']
        self.images = json['images']
        self.name = json['names']['title']
        self.regularPrice = json['prices']['regularPrice']
        self.currentPrice = json['prices']['currentPrice']
        self.productUrl = json['links']['product']
        self.webUrl = json['links']['web']
        self.addToCartUrl = json['links']['addToCart']
        self.rank = json['rank']
"""        
    
class RecommendationAPI(BestBuy):
    
    api_key = None
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _post_query(self, query, endpoint):
        recommendations = []
        recommendation_list = super()._query('beta/products', '{0}'.format(query), endpoint, self.api_key, None)['results']
        for recommendation in recommendation_list:
            x = json.loads(json.dumps(recommendation), object_hook=lambda d: namedtuple('Recommendation', d.keys(), rename=True)(*d.values()))
            stores.append(x)
            recommendations.append(x)
            #recommendations.append(Recommendation(recommendation))
        return recommendations
    
    def most_popular_by_category_id(self, category_id):
        return self._post_query('(categoryId={0})'.format(str(category_id)), 'mostViewed')
    
    def trending_by_category_id(self, category_id):
        return self._post_query('(categoryId={0})'.format(str(category_id)), 'trendingViewed')

"""
class Category:
    json = None
    id = None
    name = None
    active = None
    url = None
    path = None
    subCategories = []
    
    def __init__(self, json):
        self.json = json
        self.id = json['id']
        self.name = json['name']
        if json['active']:
            self.active = json['active']
            self.url = json['url']
            self.path = json['path']
            self.subCategories = json['subCategories']
"""    
    
class CategoryAPI(BestBuy):
    
    category = 'categories'
    api_key = None
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _post_query(self, query):
        categories = []
        category_list = super()._query('v1', '{0}'.format(query), self.category, self.api_key, None)['categories']
        for category in category_list:
            x = json.loads(json.dumps(category), object_hook=lambda d: namedtuple('Category', d.keys(), rename=True)(*d.values()))
            categories.append(x)
            #categories.append(Category(category))
        return categories
        
    def search_all_categories(self):
        return self._post_query('')
    
    def search_top_level_categories(self):
        return self._post_query('(id=abcat*)')
    
    def search_by_category_name(self, category_name):
        return self._post_query('(name={0}*)'.format(str(category_name)))
    
    def search_by_category_id(self, category_id):
        return self._post_query('(id={0})'.format(str(category_id)))

class Offer:
    json = None
    currentPrice = None
    regularPrice = None
    condition = None
    onlineAvailability = None
    inStoreAvailability = None
    listingId = None
    sellerId = None
    
    def __init__(self, json):
        self.json = json
        self.currentPrice = json['prices']['currentPrice']
        self.regularPrice = json['prices']['regularPrice']
        self.condition = json['condition']
        self.onlineAvailability = json['onlineAvailability']
        self.inStoreAvailability = json['inStoreAvailability']
        self.listingId = json['listingId']
        self.sellerId = json['sellerId']

class OpenBox:
    json = None
    sku = None
    customerReviewAverage = None
    customerReviewCount = None
    description = None
    images = None
    name = None
    regularPrice = None
    currentPrice = None
    productUrl = None
    webUrl = None
    addToCartUrl = None
    offers = []
    
    def __init__(self, json):
        self.json = json
        self.sku = json['sku']
        self.customerReviewAverage = json['customerReviews']['averageScore']
        self.customerReviewCount = json['customerReviews']['count']
        self.description = json['descriptions']['short']
        self.images = json['images']
        self.name = json['names']['title']
        self.regularPrice = json['prices']['regularPrice']
        self.currentPrice = json['prices']['currentPrice']
        self.productUrl = json['links']['product']
        self.webUrl = json['links']['web']
        self.addToCartUrl = json['links']['addToCart']
        for offer in json['offers']:
            self.offers.append(Offer(offer))

class OpenBoxAPI(BestBuy):
    
    category = 'openBox'
    api_key = None
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _post_query(self, query, sort=None):
        openBoxes = []
        openBox_list = super()._query('beta/products', query, self.category, self.api_key, None)['results']
        for openBox in openBox_list:
            openBoxes.append(OpenBox(openBox))
        return openBoxes
    
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

"""
class Image:
    json = None
    rel = None
    unitOfMeasure = None
    width = None
    height = None
    href = None
    primary = None
    
    def __init__(self, json):
        self.json = json
        self.rel = json['rel']
        self.unitOfMeasure = json['unitOfMeasure']
        self.width = json['width']
        self.height = json['height']
        self.href = json['href']
        self.primary = json['primary']
"""
"""
class Product:
    json = None
    sku = None
    score = None
    productId = None
    name = None
    source = None
    type = None
    startDate = None
    new = False
    active = False
    lowPriceGuarantee = False
    activeUpdateDate = None
    regularPrice = None
    salePrice = None
    clearance = False
    onSale = False
    planPrice = None
    priceWithPlan = None
    contracts = None
    priceRestriction = None
    priceUpdateDate = None
    digital = False
    preowned = False
    carriers = None
    planFeatures = None
    devices = None
    carrierPlans = None
    technologyCode = None
    carrierModelNumber = None
    earlyTerminationFees = None
    monthlyRecurringCharge = None
    monthlyRecurringChargeGrandTotal = None
    activationCharge = None
    minutePrice = None
    planCategory = None
    planType = None
    familyIndividualCode = None
    validFrom = None
    validUntil = None
    carrierPlan = None
    outletCenter = None
    secondaryMarket = None
    frequentlyPurchasedWith = None
    accessories = None
    relatedProductsSKUs = []
    requiredParts = None
    techSupportPlans = None
    crossSell = None
    salesRankShortTerm = None
    salesRankMediumTerm = None
    salesRankLongTerm = None
    bestSellingRank = None
    url = None
    spin360Url = None
    mobileUrl = None
    affiliateUrl = None
    addToCartUrl = None
    affiliateAddToCartUrl = None
    linkShareAffiliateUrl = None
    linkShareAffiliateAddToCartUrl = None
    upc = None
    productTemplate = None
    categoryPath = []
    alternateCategories = []
    lists = []
    customerReviewCount = None
    customerReviewAverage = None
    customerTopRated = False
    format = None
    freeShipping = False
    freeShippingEligible = False
    inStoreAvailability = False
    inStoreAvailabilityText = None
    inStoreAvailabilityUpdateDate = None
    itemUpdateDate = None
    onlineAvailability = False
    onlineAvailabilityText = None
    onlineAvailabilityUpdateDate = None
    releaseDate = None
    shippingCost = None
    shipping = None
    shippingLevelsOfService = None
    specialOrder = False
    shortDescription = None
    longDescription = None
    manufacturer = None
    modelNumber = None
    itemClass = None
    itemClassId = None
    itemSubclass = None
    itemSubclassId = None
    department = None
    departmentId = None
    protectionPlanTerm = None
    protectionPlanType = None
    protectionPlanLowPrice = None
    protectionPlanHighPrice = None
    buybackPlans = []
    protectionPlans = []
    protectionPlanDetails = []
    productFamilies = []
    productVariations = []
    aspectRatio = None
    screenFormat = None
    lengthInMinutes = None
    mpaaRating = None
    plot = None
    studio = None
    theatricalReleaseDate = None
    description = None
    images = []
    image = None
    largeFrontImage = None
    mediumImage = None
    thumbnailImage = None
    largeImage = None
    alternateViewsImage = None
    angleImage = None
    backViewImage = None
    energyGuideImage = None
    leftViewImage = None
    accessoriesImage = None
    remoteControlImage = None
    rightViewImage = None
    topViewImage = None
    albumTitle = None
    artistName = None
    artistId = None
    originalReleaseDate = None
    parentalAdvisory = None
    mediaCount = None
    monoStereo = None
    studioLive = None
    condition = None
    inStorePickup = None
    friendsAndFamilyPickup = None
    homeDelivery = None
    quantityLimit = None
    fulfilledBy = None
    members = []
    bundledIn = []
    albumLabel = None
    genre = None
    color = None
    depth = None
    dollarSavings = None
    percentSavings = None
    tradeInValue = None
    height = None
    orderable = None
    weight = None
    shippingWeight = None
    width = None
    warrantyLabor = None
    warrantyParts = None
    softwareAge = None
    softwareGrade = None
    platform = None
    numberOfPlayers = None
    softwareNumberOfPlayers = None
    esrbRating = None
    includedItemList = []
    marketplace = None
    listingId = None
    sellerId = None
    shippingRestrictions = None
    proposition65WarningMessage = None
    proposition65WarningType = None
    coaxialDigitalAudioOutputs = None
    componentVideoOutputs = None
    compositeVideoOutputs = None
    energyStarQualified = None
    hdmiOutputs = None
    maximumOutputResolution = None
    mediaCardSlot = None
    numberOfCoaxialDigitalAudioOutputs = None
    numberOfOpticalDigitalAudioOutputs = None
    opticalDigitalAudioOutputs = None
    playerType = None
    smartCapable = None
    usbPort = None
    
    
    def __init__(self, json):
        self.json = json
        self.sku = json['sku']
        self.score = json['score']
        self.productId = json['productId']
        self.name = json['name']
        self.source = json['source']
        self.type = json['type']
        self.startDate = json['startDate']
        self.new = json['new']
        self.active = json['active']
        self.lowPriceGuarantee = json['lowPriceGuarantee']
        self.activeUpdateDate = json['activeUpdateDate']
        self.regularPrice = json['regularPrice']
        self.salePrice = json['salePrice']
        self.clearance = json['clearance']
        self.onSale = json['onSale']
        self.planPrice = json['planPrice']
        self.priceWithPlan = json['priceWithPlan']
        self.contracts = json['contracts']
        self.priceRestriction = json['priceRestriction']
        self.priceUpdateDate = json['priceUpdateDate']
        self.digital = json['digital']
        self.preowned = json['preowned']
        self.carriers = json['carriers']
        self.planFeatures = json['planFeatures']
        self.devices = json['devices']
        self.carrierPlans = json['carrierPlans']
        self.technologyCode = json['technologyCode']
        self.carrierModelNumber = json['carrierModelNumber']
        self.earlyTerminationFees = json['earlyTerminationFees']
        self.monthlyRecurringCharge = json['monthlyRecurringCharge']
        self.monthlyRecurringChargeGrandTotal = json['monthlyRecurringChargeGrandTotal']
        self.activationCharge = json['activationCharge']
        self.minutePrice = json['minutePrice']
        self.planCategory = json['planCategory']
        self.planType = json['planType']
        self.familyIndividualCode = json['familyIndividualCode']
        self.validFrom = json['validFrom']
        self.validUntil = json['validUntil']
        self.carrierPlan = json['carrierModelNumber']
        self.outletCenter = json['outletCenter']
        self.secondaryMarket = json['secondaryMarket']
        self.frequentlyPurchasedWith = json['frequentlyPurchasedWith']
        self.accessories = json['accessories']
        for item in json['relatedProducts']:
            self.relatedProductsSKUs.append(item['sku'])
        self.requiredParts = json['requiredParts']
        self.techSupportPlans = json['techSupportPlans']
        self.crossSell = json['crossSell']
        self.salesRankShortTerm = json['salesRankShortTerm']
        self.salesRankMediumTerm = json['salesRankMediumTerm']
        self.salesRankLongTerm = json['salesRankLongTerm']
        self.bestSellingRank = json['bestSellingRank']
        self.url = json['url']
        self.spin360Url = json['spin360Url']
        self.mobileUrl = json['mobileUrl']
        self.affiliateUrl = json['affiliateUrl']
        self.addToCartUrl = json['addToCartUrl']
        self.affiliateAddToCartUrl = json['affiliateAddToCartUrl']
        self.linkShareAffiliateUrl = json['linkShareAffiliateUrl']
        self.linkShareAffiliateAddToCartUrl = json['linkShareAffiliateAddToCartUrl']
        self.upc = json['upc']
        self.productTemplate = json['productTemplate']
        self.categoryPath = json['categoryPath']
        self.alternateCategories = json['alternateCategories']
        self.lists = json['lists']
        self.customerReviewCount = json['customerReviewCount']
        self.customerReviewAverage = json['customerReviewAverage']
        self.customerTopRated = json['customerTopRated']
        self.format = json['format']
        self.freeShipping = json['freeShipping']
        self.freeShippingEligible = json['freeShippingEligible']
        self.inStoreAvailability = json['inStoreAvailability']
        self.inStoreAvailabilityText = json['inStoreAvailabilityText']
        self.inStoreAvailabilityUpdateDate = json['inStoreAvailabilityUpdateDate']
        self.itemUpdateDate = json['itemUpdateDate']
        self.onlineAvailability = json['onlineAvailability']
        self.onlineAvailabilityText = json['onlineAvailabilityText']
        self.onlineAvailabilityUpdateDate = json['onlineAvailabilityUpdateDate']
        self.releaseDate = json['releaseDate']
        self.shippingCost = json['shippingCost']
        self.shipping = json['shipping']
        self.shippingLevelsOfService = json['shippingLevelsOfService']
        self.specialOrder = json['specialOrder']
        self.shortDescription = json['shortDescription']
        self.longDescription = json['longDescription']
        self.itemClass = json['class']
        self.itemClassId = json['classId']
        self.itemSubclass = json['subclass']
        self.itemSubclassId = json['subclassId']
        self.department = json['department']
        self.departmentId = json['departmentId']
        self.protectionPlanTerm = json['protectionPlanTerm']
        self.protectionPlanType = json['protectionPlanType']
        self.protectionPlanLowPrice = json['protectionPlanLowPrice']
        self.protectionPlanHighPrice = json['protectionPlanHighPrice']
        self.buybackPlans = json['buybackPlans']
        self.protectionPlans = json['protectionPlans']
        self.protectionPlanDetails = json['protectionPlanDetails']
        self.productFamilies = json['productFamilies']
        self.productVariations = json['productVariations']
        self.aspectRatio = json['aspectRatio']
        self.screenFormat = json['screenFormat']
        self.lengthInMinutes = json['lengthInMinutes']
        self.mpaaRating = json['mpaaRating']
        self.plot = json['plot']
        self.studio = json['studio']
        self.theatricalReleaseDate = json['theatricalReleaseDate']
        self.description = json['description']
        self.manufacturer = json['manufacturer']
        self.modelNumber = json['modelNumber']
        for image in json['images']:
            self.images.append(Image(image))
        self.image = json['image']
        self.largeFrontImage = json['largeFrontImage']
        self.mediumImage = json['mediumImage']
        self.thumbnailImage = json['thumbnailImage']
        self.largeImage = json['largeImage']
        self.alternateViewsImage = json['alternateViewsImage']
        self.angleImage = json['angleImage']
        self.backViewImage = json['backViewImage']
        self.energyGuideImage = json['energyGuideImage']
        self.leftViewImage = json['leftViewImage']
        self.accessoriesImage = json['accessoriesImage']
        self.remoteControlImage = json['remoteControlImage']
        self.rightViewImage = json['rightViewImage']
        self.topViewImage = json['topViewImage']
        self.albumTitle = json['albumTitle']
        self.artistName = json['artistName']
        self.artistId = json['artistId']
        self.originalReleaseDate = json['originalReleaseDate']
        self.parentalAdvisory = json['parentalAdvisory']
        self.mediaCount = json['mediaCount']
        self.monoStereo = json['monoStereo']
        self.studioLive = json['studioLive']
        self.condition = json['condition']
        self.inStorePickup = json['inStorePickup']
        self.friendsAndFamilyPickup = json['friendsAndFamilyPickup']
        self.homeDelivery = json['homeDelivery']
        self.quantityLimit = json['quantityLimit']
        self.fulfilledBy = json['fulfilledBy']
        self.members = json['members']
        self.bundledIn = json['bundledIn']
        self.albumLabel = json['albumLabel']
        self.genre = json['genre']
        self.color = json['color']
        self.depth = json['depth']
        self.dollarSavings = json['dollarSavings']
        self.percentSavings = json['percentSavings']
        self.tradeInValue = json['tradeInValue']
        self.height = json['height']
        self.orderable = json['orderable']
        self.weight = json['weight']
        self.shippingWeight = json['shippingWeight']
        self.width = json['width']
        self.warrantyLabor = json['warrantyLabor']
        self.warrantyParts = json['warrantyParts']
        self.softwareAge = json['softwareAge']
        self.softwareGrade = json['softwareGrade']
        self.platform = json['platform']
        self.numberOfPlayers = json['numberOfPlayers']
        self.softwareNumberOfPlayers = json['softwareNumberOfPlayers']
        self.esrbRating = json['esrbRating']
        for item in json['includedItemList']:
            self.includedItemList.append(item['includedItem'])
        self.marketplace = json['marketplace']
        self.listingId = json['listingId']
        self.sellerId = json['sellerId']
        self.shippingRestrictions = json['shippingRestrictions']
        self.proposition65WarningMessage = json['proposition65WarningMessage']
        self.proposition65WarningType = json['proposition65WarningType']
        self.coaxialDigitalAudioOutputs = json['coaxialDigitalAudioOutputs']
        self.componentVideoOutputs = json['componentVideoOutputs']
        self.compositeVideoOutputs = json['compositeVideoOutputs']
        self.energyStarQualified = json['energyStarQualified']
        self.hdmiOutputs = json['hdmiOutputs']
        self.maximumOutputResolution = json['maximumOutputResolution']
        self.mediaCardSlot = json['mediaCardSlot']
        self.numberOfCoaxialDigitalAudioOutputs = json['numberOfCoaxialDigitalAudioOutputs']
        self.numberOfOpticalDigitalAudioOutputs = json['numberOfOpticalDigitalAudioOutputs']
        self.opticalDigitalAudioOutputs = json['opticalDigitalAudioOutputs']
        self.playerType = json['playerType']
        self.smartCapable = json['smartCapable']
        self.usbPort = json['usbPort']
"""        

class ProductAPI(BestBuy):
    """
    TODO: Document Sort params
    """
    
    category = 'products'
    api_key = None
    
    def __init__(self, api_key):
        self.api_key = api_key

    def _post_query(self, query, sort=None):
        """
        Call API
        
        :param query: query against the API
        
        Return Product object(s)
        """
        products = []
        product_list = super()._query('v1', query, self.category, self.api_key, '&sort={0}.asc'.format(sort) if sort else None)['products']
        for product in product_list:
            x = json.loads(json.dumps(product), object_hook=lambda d: namedtuple('Product', d.keys(), rename=True)(*d.values()))
            products.append(x)
            #products.append(Product(product))
        return products

    def search_by_sku(self, sku, sort=None):
        """
        Search by SKU number
        
        :param sku: SKU number
        
        Returns one Product object
        """
        return self._post_query('(sku={0})'.format(str(sku)), sort)[0]
    
    def search_by_upc(self, upc, sort=None):
        """
        Search by UPC number
        
        :param upc: UPC number
        
        Returns one Product object
        """
        return self._post_query('(upc={0})'.format(str(upc)), sort)[0]
    
    def search_by_description(self, description, sort=None):
        """
        Search by product description
        
        :param description: Product description to search
        
        Returns multiple Product objects
        """
        return self._post_query('(description={0})'.format(description), sort=None)

    def search(self, query=None, **kwargs):
        """
        General search
        
        :param query: query against the API
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
            freeShipping,
            inStoreAvailability,
            manufacturer,
            modelNumber,
            name,
            onlineAvailability,
            onSale,
            percentSavings,
            preowned,
            regularPrice,
            salePrice,
            shippingCost,
            sku,
            type,
            upc
            
        
        Returns multiple Product objects
        """
        if not query:
            query = ""
        else:
            query = query + "&"
        if kwargs:
            for key, value in kwargs.items():
                query = '{q}{k}{v}&'.format(q=query, k=key, v=value)
            query = '(' + query[:-1] + ')'
        return self._post_query(query)

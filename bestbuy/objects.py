# import json


class Category:

    def __init__(self, json):
        # self.__dict = json.loads(str(j))
        self.json = json
        self.id = json.get('id', None)
        self.name = json.get('name', None)
        self.active = json.get('active', None)
        self.url = json.get('url', None)
        self.path = json.get('path', None)
        self.subCategories = json.get('subCategories', [])

    def __getattr__(self, name):
        return None


class Recommendation:

    def __init__(self, json):
        # self.__dict = json.loads(str(j))
        self.json = json
        self.sku = json.get('sku', None)
        self.customerReviewAverage = json.get('customerReviews', []).get('averageScore', None)
        self.customerReviewCount = json.get('customerReviews', []).get('count', None)
        self.description = json.get('descriptions', None).get('short', None)
        self.images = json.get('images', None)
        self.name = json.get('names', None).get('title', None)
        self.regularPrice = json.get('prices', None).get('regularPrice', None)
        self.currentPrice = json.get('prices', None).get('currentPrice', None)
        self.productUrl = json.get('links', None).get('product', None)
        self.webUrl = json.get('links', None).get('web', None)
        self.addToCartUrl = json.get('links', None).get('addToCart', None)
        self.rank = json.get('rank', None)

    def __getattr__(self, name):
        return None


class Store:

    def __init__(self, json):
        # self.__dict = json.loads(str(j))
        self.json = json
        self.storeId = json.get('storeId', None)
        self.storeType = json.get('storeType', None)
        self.tradeIn = json.get('tradeIn', None)
        self.brand = json.get('brand', None)
        self.name = json.get('name', None)
        self.longName = json.get('longName', None)
        self.address = json.get('address', None) + json.get('address2', None)
        self.city = json.get('city', None)
        self.region = json.get('region', None)
        self.postalCode = json.get('fullPostalCode', None)
        self.country = json.get('country', None)
        self.latitude = json.get('lat', None)
        self.longitude = json.get('lng', None)
        self.hours = json.get('hours', None)
        self.gmtOffset = json.get('gmtOffset', None)
        self.language = json.get('language', None)
        self.phone = json.get('phone', None)
        self.services = []
        for service in json.get('services', []):
            self.services.append(service.get('service', ""))

    def __getattr__(self, name):
        return None


class Image:

    def __init__(self, json):
        # self.__dict = json.loads(str(j))
        self.json = json
        self.rel = json.get('rel', None)
        self.unitOfMeasure = json.get('unitOfMeasure', None)
        self.width = json.get('width', None)
        self.height = json.get('height', None)
        self.href = json.get('href', None)
        self.primary = json.get('primary', None)

    def __getattr__(self, name):
        return None


class Product:

    def __init__(self, json):
        # self.__dict = json.loads(str(j))
        self.relatedProductsSKUs = []
        self.categoryPath = []
        self.alternateCategories = []
        self.lists = []
        self.buybackPlans = []
        self.protectionPlans = []
        self.protectionPlanDetails = []
        self.productFamilies = []
        self.productVariations = []
        self.members = []
        self.bundledIn = []
        self.includedItemList = []
        self.images = []
        self.json = json
        self.sku = json.get('sku', None)
        self.score = json.get('score', None)
        self.productId = json.get('productId', None)
        self.name = json.get('name', None)
        self.source = json.get('source', None)
        self.type = json.get('type', None)
        self.startDate = json.get('startDate', None)
        self.new = json.get('new', None)
        self.active = json.get('active', None)
        self.lowPriceGuarantee = json.get('lowPriceGuarantee', None)
        self.activeUpdateDate = json.get('activeUpdateDate', None)
        self.regularPrice = json.get('regularPrice', None)
        self.salePrice = json.get('salePrice', None)
        self.clearance = json.get('clearance', None)
        self.onSale = json.get('onSale', None)
        self.planPrice = json.get('planPrice', None)
        self.priceWithPlan = json.get('priceWithPlan', None)
        self.contracts = json.get('contracts', None)
        self.priceRestriction = json.get('priceRestriction', None)
        self.priceUpdateDate = json.get('priceUpdateDate', None)
        self.digital = json.get('digital', None)
        self.preowned = json.get('preowned', None)
        self.carriers = json.get('carriers', None)
        self.planFeatures = json.get('planFeatures', None)
        self.devices = json.get('devices', None)
        self.carrierPlans = json.get('carrierPlans', None)
        self.technologyCode = json.get('technologyCode', None)
        self.carrierModelNumber = json.get('carrierModelNumber', None)
        self.earlyTerminationFees = json.get('earlyTerminationFees', None)
        self.monthlyRecurringCharge = json.get('monthlyRecurringCharge', None)
        self.monthlyRecurringChargeGrandTotal = json.get('monthlyRecurringChargeGrandTotal', None)
        self.activationCharge = json.get('activationCharge', None)
        self.minutePrice = json.get('minutePrice', None)
        self.planCategory = json.get('planCategory', None)
        self.planType = json.get('planType', None)
        self.familyIndividualCode = json.get('familyIndividualCode', None)
        self.validFrom = json.get('validFrom', None)
        self.validUntil = json.get('validUntil', None)
        self.carrierPlan = json.get('carrierModelNumber', None)
        self.outletCenter = json.get('outletCenter', None)
        self.secondaryMarket = json.get('secondaryMarket', None)
        self.frequentlyPurchasedWith = json.get('frequentlyPurchasedWith', None)
        self.accessories = json.get('accessories', None)
        for item in json.get('relatedProducts', []):
            self.relatedProductsSKUs.append(item.get('sku', None))
        self.requiredParts = json.get('requiredParts', None)
        self.techSupportPlans = json.get('techSupportPlans', None)
        self.crossSell = json.get('crossSell', None)
        self.salesRankShortTerm = json.get('salesRankShortTerm', None)
        self.salesRankMediumTerm = json.get('salesRankMediumTerm', None)
        self.salesRankLongTerm = json.get('salesRankLongTerm', None)
        self.bestSellingRank = json.get('bestSellingRank', None)
        self.url = json.get('url', None)
        self.spin360Url = json.get('spin360Url', None)
        self.mobileUrl = json.get('mobileUrl', None)
        self.affiliateUrl = json.get('affiliateUrl', None)
        self.addToCartUrl = json.get('addToCartUrl', None)
        self.affiliateAddToCartUrl = json.get('affiliateAddToCartUrl', None)
        self.linkShareAffiliateUrl = json.get('linkShareAffiliateUrl', None)
        self.linkShareAffiliateAddToCartUrl = json.get('linkShareAffiliateAddToCartUrl', None)
        self.upc = json.get('upc', None)
        self.productTemplate = json.get('productTemplate', None)
        self.categoryPath = json.get('categoryPath', None)
        self.alternateCategories = json.get('alternateCategories', None)
        self.lists = json.get('lists', None)
        self.customerReviewCount = json.get('customerReviewCount', None)
        self.customerReviewAverage = json.get('customerReviewAverage', None)
        self.customerTopRated = json.get('customerTopRated', None)
        self.format = json.get('format', None)
        self.freeShipping = json.get('freeShipping', None)
        self.freeShippingEligible = json.get('freeShippingEligible', None)
        self.inStoreAvailability = json.get('inStoreAvailability', None)
        self.inStoreAvailabilityText = json.get('inStoreAvailabilityText', None)
        self.inStoreAvailabilityUpdateDate = json.get('inStoreAvailabilityUpdateDate', None)
        self.itemUpdateDate = json.get('itemUpdateDate', None)
        self.onlineAvailability = json.get('onlineAvailability', None)
        self.onlineAvailabilityText = json.get('onlineAvailabilityText', None)
        self.onlineAvailabilityUpdateDate = json.get('onlineAvailabilityUpdateDate', None)
        self.releaseDate = json.get('releaseDate', None)
        self.shippingCost = json.get('shippingCost', None)
        self.shipping = json.get('shipping', None)
        self.shippingLevelsOfService = json.get('shippingLevelsOfService', None)
        self.specialOrder = json.get('specialOrder', None)
        self.shortDescription = json.get('shortDescription', None)
        self.longDescription = json.get('longDescription', None)
        self.itemClass = json.get('class', None)
        self.itemClassId = json.get('classId', None)
        self.itemSubclass = json.get('subclass', None)
        self.itemSubclassId = json.get('subclassId', None)
        self.department = json.get('department', None)
        self.departmentId = json.get('departmentId', None)
        self.protectionPlanTerm = json.get('protectionPlanTerm', None)
        self.protectionPlanType = json.get('protectionPlanType', None)
        self.protectionPlanLowPrice = json.get('protectionPlanLowPrice', None)
        self.protectionPlanHighPrice = json.get('protectionPlanHighPrice', None)
        self.buybackPlans = json.get('buybackPlans', None)
        self.protectionPlans = json.get('protectionPlans', None)
        self.protectionPlanDetails = json.get('protectionPlanDetails', None)
        self.productFamilies = json.get('productFamilies', None)
        self.productVariations = json.get('productVariations', None)
        self.aspectRatio = json.get('aspectRatio', None)
        self.screenFormat = json.get('screenFormat', None)
        self.lengthInMinutes = json.get('lengthInMinutes', None)
        self.mpaaRating = json.get('mpaaRating', None)
        self.plot = json.get('plot', None)
        self.studio = json.get('studio', None)
        self.theatricalReleaseDate = json.get('theatricalReleaseDate', None)
        self.description = json.get('description', None)
        self.manufacturer = json.get('manufacturer', None)
        self.modelNumber = json.get('modelNumber', None)
        for image in json.get('images', []):
            self.images.append(Image(image))
        self.image = json.get('image', None)
        self.largeFrontImage = json.get('largeFrontImage', None)
        self.mediumImage = json.get('mediumImage', None)
        self.thumbnailImage = json.get('thumbnailImage', None)
        self.largeImage = json.get('largeImage', None)
        self.alternateViewsImage = json.get('alternateViewsImage', None)
        self.angleImage = json.get('angleImage', None)
        self.backViewImage = json.get('backViewImage', None)
        self.energyGuideImage = json.get('energyGuideImage', None)
        self.leftViewImage = json.get('leftViewImage', None)
        self.accessoriesImage = json.get('accessoriesImage', None)
        self.remoteControlImage = json.get('remoteControlImage', None)
        self.rightViewImage = json.get('rightViewImage', None)
        self.topViewImage = json.get('topViewImage', None)
        self.albumTitle = json.get('albumTitle', None)
        self.artistName = json.get('artistName', None)
        self.artistId = json.get('artistId', None)
        self.originalReleaseDate = json.get('originalReleaseDate', None)
        self.parentalAdvisory = json.get('parentalAdvisory', None)
        self.mediaCount = json.get('mediaCount', None)
        self.monoStereo = json.get('monoStereo', None)
        self.studioLive = json.get('studioLive', None)
        self.condition = json.get('condition', None)
        self.inStorePickup = json.get('inStorePickup', None)
        self.friendsAndFamilyPickup = json.get('friendsAndFamilyPickup', None)
        self.homeDelivery = json.get('homeDelivery', None)
        self.quantityLimit = json.get('quantityLimit', None)
        self.fulfilledBy = json.get('fulfilledBy', None)
        self.members = json.get('members', None)
        self.bundledIn = json.get('bundledIn', None)
        self.albumLabel = json.get('albumLabel', None)
        self.genre = json.get('genre', None)
        self.color = json.get('color', None)
        self.depth = json.get('depth', None)
        self.dollarSavings = json.get('dollarSavings', None)
        self.percentSavings = json.get('percentSavings', None)
        self.tradeInValue = json.get('tradeInValue', None)
        self.height = json.get('height', None)
        self.orderable = json.get('orderable', None)
        self.weight = json.get('weight', None)
        self.shippingWeight = json.get('shippingWeight', None)
        self.width = json.get('width', None)
        self.warrantyLabor = json.get('warrantyLabor', None)
        self.warrantyParts = json.get('warrantyParts', None)
        self.softwareAge = json.get('softwareAge', None)
        self.softwareGrade = json.get('softwareGrade', None)
        self.platform = json.get('platform', None)
        self.numberOfPlayers = json.get('numberOfPlayers', None)
        self.softwareNumberOfPlayers = json.get('softwareNumberOfPlayers', None)
        self.esrbRating = json.get('esrbRating', None)
        for it in json.get('includedItemList', []):
            self.includedItemList.append(it.get('includedItem', None))
        self.marketplace = json.get('marketplace', None)
        self.listingId = json.get('listingId', None)
        self.sellerId = json.get('sellerId', None)
        self.shippingRestrictions = json.get('shippingRestrictions', None)
        self.proposition65WarningMessage = json.get('proposition65WarningMessage', None)
        self.proposition65WarningType = json.get('proposition65WarningType', None)
        self.coaxialDigitalAudioOutputs = json.get('coaxialDigitalAudioOutputs', None)
        self.componentVideoOutputs = json.get('componentVideoOutputs', None)
        self.compositeVideoOutputs = json.get('compositeVideoOutputs', None)
        self.energyStarQualified = json.get('energyStarQualified', None)
        self.hdmiOutputs = json.get('hdmiOutputs', None)
        self.maximumOutputResolution = json.get('maximumOutputResolution', None)
        self.mediaCardSlot = json.get('mediaCardSlot', None)
        self.numberOfCoaxialDigitalAudioOutputs = json.get('numberOfCoaxialDigitalAudioOutputs', None)
        self.numberOfOpticalDigitalAudioOutputs = json.get('numberOfOpticalDigitalAudioOutputs', None)
        self.opticalDigitalAudioOutputs = json.get('opticalDigitalAudioOutputs', None)
        self.playerType = json.get('playerType', None)
        self.smartCapable = json.get('smartCapable', None)
        self.usbPort = json.get('usbPort', None)

    def __getattr__(self, name):
        return None


class Offer:

    def __init__(self, json):
        # self.__dict = json.loads(str(j))
        self.json = json
        self.currentPrice = json.get('prices', None).get('currentPrice', None)
        self.regularPrice = json.get('prices', None).get('regularPrice', None)
        self.condition = json.get('condition', None)
        self.onlineAvailability = json.get('onlineAvailability', None)
        self.inStoreAvailability = json.get('inStoreAvailability', None)
        self.listingId = json.get('listingId', None)
        self.sellerId = json.get('sellerId', None)

    def __getattr__(self, name):
        return None


class OpenBox:

    def __init__(self, json):
        # self.__dict = json.loads(j)
        self.json = json
        self.sku = json.get('sku', None)
        self.customerReviewAverage = json.get('customerReviews', None).get('averageScore', None)
        self.customerReviewCount = json.get('customerReviews', None).get('count', None)
        self.description = json.get('descriptions', None).get('short', None)
        self.images = json.get('images', None)
        self.name = json.get('names', None).get('title', None)
        self.regularPrice = json.get('prices', None).get('regularPrice', None)
        self.currentPrice = json.get('prices', None).get('currentPrice', None)
        self.productUrl = json.get('links', None).get('product', None)
        self.webUrl = json.get('links', None).get('web', None)
        self.addToCartUrl = json.get('links', None).get('addToCart', None)
        self.offers = []
        for offer in json.get('offers', None):
            self.offers.append(Offer(offer))

    def __getattr__(self, name):
        return None

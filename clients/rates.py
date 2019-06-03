"""rates module
"""
from enum import Enum
import requests


class RateItem(object):
    nmfc_class = ''
    weight = 0

    def __init__(self, nmfc_class, weight):
        super().__init__()
        self.nmfc_class = nmfc_class
        self.weight = weight


class DestinationType(Enum):
    RESIDENTIAL = 'RESIDENTIAL'
    CONSTRUCTIONSITE = 'CONSTRUCTIONSITE'
    TRADESHOW = 'TRADESHOW'
    BUSINESS = 'BUSINESS'


def estimate(access_token, origin_postal_code, destination_postal_code,
             destination_type, pickup_date, pallet_quantity, items):
    headers = {'Authorization': 'Basic {}'.format(access_token)}
    response = requests.post(
        'https://restapi.echo.com/v2/rates?Take&SCAC&TransitDays&Guaranteed&CarrierName',
        headers=headers,
        json={
            'OriginPostalCode': origin_postal_code,
            'OriginCountryCode': 'US',
            'DestinationPostalCode': destination_postal_code,
            'DestinationCountryCode': 'US',
            'DestinationType': destination_type.value,
            'PickUpDate': pickup_date,
            'PalletQuantity': pallet_quantity,
            'UnitOfWeight': 'LB',
            'items': __map_items__(items)
        })
    return response.json()

def __map_items__(items):
    result = []
    for item in items:
        result.append({
            'NmfcClass': item.nmfc_class,
            'Weight': item.weight
        })
    return result

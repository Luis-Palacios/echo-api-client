"""rates module
"""
import requests


def estimate(access_token, origin_postal_code, destination_postal_code,
             destination_type, pickup_date, pallet_quantity, items):
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.post(
        'https://restapi.echo.com/v2/rates?Take&SCAC&TransitDays&Guaranteed&CarrierName',
        headers=headers,
        json={
            'OriginPostalCode': origin_postal_code,
            'OriginCountryCode': 'US',
            'DestinationPostalCode': destination_postal_code,
            'DestinationCountryCode': 'US',
            'DestinationType': destination_type,
            'PickUpDate': pickup_date,
            'PalletQuantity': pallet_quantity,
            'UnitOfWeight': 'LB',
            'items': items
        })
    return response.json()
import pytest

from yelpSample import *

input = '-term= "bars" --location= "San Francisco, CA"'
fullResponse = { u'alias': u'barrio-san-francisco-2',
  u'categories': [ { u'alias': u'wine_bars', u'title': u'Wine Bars'},
                   { u'alias': u'beerbar', u'title': u'Beer Bar'},
                   { u'alias': u'latin', u'title': u'Latin American'}],
  u'coordinates': { u'latitude': 37.7995429440611,
                    u'longitude': -122.410825960609},
  u'display_phone': u'(415) 923-8997',
  u'hours': [ { u'hours_type': u'REGULAR',
                u'is_open_now': False,
                u'open': [ { u'day': 0,
                             u'end': u'2200',
                             u'is_overnight': False,
                             u'start': u'1600'},
                           { u'day': 1,
                             u'end': u'2200',
                             u'is_overnight': False,
                             u'start': u'1600'},
                           { u'day': 2,
                             u'end': u'2200',
                             u'is_overnight': False,
                             u'start': u'1600'},
                           { u'day': 3,
                             u'end': u'2200',
                             u'is_overnight': False,
                             u'start': u'1600'},
                           { u'day': 4,
                             u'end': u'0000',
                             u'is_overnight': False,
                             u'start': u'1200'},
                           { u'day': 5,
                             u'end': u'0000',
                             u'is_overnight': False,
                             u'start': u'1200'}]}],
  u'id': u'CzhF2Ye0-4gCVthYqm9p0w',
  u'image_url': u'https://s3-media1.fl.yelpcdn.com/bphoto/DerTMlO1VWeeCQpzRoD0cg/o.jpg',
  u'is_claimed': True,
  u'is_closed': False,
  u'location': { u'address1': u'1609 Powell St',
                 u'address2': u'',
                 u'address3': None,
                 u'city': u'San Francisco',
                 u'country': u'US',
                 u'cross_streets': u'Union St & Green St',
                 u'display_address': [ u'1609 Powell St',
                                       u'San Francisco, CA 94133'],
                 u'state': u'CA',
                 u'zip_code': u'94133'},
  u'name': u'Barrio',
  u'phone': u'+14159238997',
  u'photos': [ u'https://s3-media1.fl.yelpcdn.com/bphoto/DerTMlO1VWeeCQpzRoD0cg/o.jpg',
               u'https://s3-media2.fl.yelpcdn.com/bphoto/o6UGAh-jlZ1_CRIpu7hTvg/o.jpg',
               u'https://s3-media2.fl.yelpcdn.com/bphoto/RkdhkZ7Nszg6GCmlhACurg/o.jpg'],
  u'rating': 5.0,
  u'review_count': 25,
  u'transactions': [],
  u'url': u'https://www.yelp.com/biz/barrio-san-francisco-2?adjust_creative=Ta2_UFQRZt8BbmkOnGLZYQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=Ta2_UFQRZt8BbmkOnGLZYQ'}


def test_extractArgs():
    assert extractArgs(input) == {"term": "bars", "location": "San Francisco, CA"}

def test_fullResponse():
    assert query_api(extractArgs(input)["term"], extractArgs(input)["location"])[0] == fullResponse

def test_parseResponse():
    assert parseResponse(fullResponse) == "Name: Barrio San Francisco 2; Address: 1609 Powell St, San Francisco, CA 94133; Rating: 5.0 (25 reviews)"

def test_clientResponse():
    print clientResponse('-term= "bars" --location= "San Francisco, CA"')



            if input:
                [user, content, channel] = input
                print(content)
                responseList = clientResponse(content)
                print(responseList)
                for res in responseList:
                    self.writeBack(channel,res)
                return

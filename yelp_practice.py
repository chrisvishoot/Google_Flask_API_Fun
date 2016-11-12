# from googleplaces import GooglePlaces, types, lang
# YOUR_API_KEY = 'AIzaSyAs6zKhY63VwUB7QdXvuf96A45gmuh5UPw'
# google_places = GooglePlaces(YOUR_API_KEY)
# query_result = google_places.nearby_search(
#         location='Puyallup, Washington', keyword='Food',
#         radius=200, types=[types.TYPE_FOOD], opennow='true')
# print str(query_result.places)
# # for place in query_result.places:
# #     print place.name
# #     print place.geo_location
# #     print place.place_id
import urllib2
import json

AUTH_KEY = 'AIzaSyAs6zKhY63VwUB7QdXvuf96A45gmuh5UPw'
LOCATION = '37.787930,-122.4074990'
RADIUS = 5000

url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
     '&radius=%s&sensor=false&key=%s') % (LOCATION, RADIUS, AUTH_KEY)
response = urllib2.urlopen(url)
json_raw = response.read()
json_data = json.loads(json_raw)
if json_data['status'] == 'OK':
    for place in json_data['results']:
        print '%s: %s\n' % (place['name'], place['geometry']['location']['lat'])

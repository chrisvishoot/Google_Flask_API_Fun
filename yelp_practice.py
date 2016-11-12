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
# import urllib2
# import json
#
# YOUR_API_KEY = 'AIzaSyAs6zKhY63VwUB7QdXvuf96A45gmuh5UPw'
# LOCATION = '37.787930,-122.4074990'
# RADIUS = 5000
# geolocation_url = 'https://maps.googleapis.com/maps/api/geocode/json?&latlng=37.787930,-122.4074990'
# response = urllib2.urlopen(geolocation_url)
# json_raw = response.read()
# json_data = json.loads(json_raw)
# if json_data['status'] == 'OK':
#     for place in json_data['results']:
#         print place[0]['geometry']['location']

import geocoder
import urllib2
import json
g = geocoder.ip('me')
print g.latlng
print g.city
LOCATION = '%s,%s' %(g.lat, g.lng)
RADIUS = 200
YOUR_API_KEY = 'AIzaSyAs6zKhY63VwUB7QdXvuf96A45gmuh5UPw'
url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
     '&radius=%s&sensor=false&key=%s') % (LOCATION, RADIUS, YOUR_API_KEY)
response = urllib2.urlopen(url)
json_raw = response.read()
json_data = json.loads(json_raw)
if json_data['status'] == 'OK':
    print json_data['results']
    for place in json_data['results']:
        #print '%s: %s %s\n' % (place['name'], place['geometry']['location']['lat'], place['geometry']['location']['lng'])
        latitutde = float(place['geometry']['location']['lat'])
        longitude = float(place['geometry']['location']['lng'])
        print '%s, %s' % (latitutde, longitude)
        g = geocoder.google([latitutde, longitude], method='reverse')
        get_address_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=YOUR_API_KEY' % (latitutde, longitude)
        response = urllib2.urlopen(url)
        json_raw = response.read()
        json_data = json.loads(json_raw)
        address = ""
        #address = json_data['results'][0]
        print address
        # address = ""
        # address += g.city + ", "
        # address += g.state + ", "
        # address += g.country
        print address + " Postal Code: " + g.postal
        #g = geocoder.google([longitude, -latitutde], method='reverse')

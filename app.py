from flask import Flask
import urllib2
import json
import geocoder
AUTH_KEY = 'AIzaSyAs6zKhY63VwUB7QdXvuf96A45gmuh5UPw'
LOCATION = '37.787930,-122.4074990'
RADIUS = 5000
url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
     '&radius=%s&sensor=false&key=%s') % (LOCATION, RADIUS, AUTH_KEY)
ip_address = str(socket.gethostbyname(socket.gethostname()))
geolocation_url = 'https://maps.googleapis.com/maps/api/geocode/json?&latlng=37.787930,-122.4074990'

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to our page!"
@app.route('/yelpCallIpLocation')
def call():
    g = geocoder.ip('me')
    LOCATION = '%s,%s' %(g.lat, g.lng)
    TYPE = 'restaurant'
    url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
         '&radius=%s&sensor=false&opennow=true&type=%s&key=%s') % (LOCATION, RADIUS, TYPE, AUTH_KEY)
    response = urllib2.urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    string_result = ""
    if json_data['status'] == 'OK':
        for place in json_data['results']:
            string_result += '%s: %s\n' % (place['name'], place['geometry']['location']['lat'])
    return string_result
if __name__ == "__main__":
    app.run()

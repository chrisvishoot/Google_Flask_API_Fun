from flask import Flask, render_template
import urllib2
import json
import geocoder
AUTH_KEY = 'AIzaSyAs6zKhY63VwUB7QdXvuf96A45gmuh5UPw'
LOCATION = '37.787930,-122.4074990'
RADIUS = 5000
url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
     '&radius=%s&sensor=false&key=%s') % (LOCATION, RADIUS, AUTH_KEY)

app = Flask(__name__)

@app.route('/')
def hello():
    string_result = 'Welcome to our page!<br/>'
    string_result += 'Web Page locations include:<br/>'
    string_result += 'yelpCallIpLocation'
    return render_template('index.html')
@app.route('/PenguinsAreCool')
def PenguinsAreCool():
    return "So Penguins Are Cool"

@app.route('/yelpCallIpLocation')
def call():
    #This is to get the longitude and the latitutde
    g = geocoder.ip('me')
    LOCATION = '%s,%s' %(g.lat, g.lng)
    TYPE = 'food'
    url = ('https://maps.googleapis.com/maps/api/place/search/json?location=%s'
         '&radius=%s&sensor=false&opennow=true&type=%s&key=%s') % (LOCATION, RADIUS, TYPE, AUTH_KEY)
    response = urllib2.urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    string_result = ""
    if json_data['status'] == 'OK':
        for place in json_data['results']:
            string_result += '%s: %s<br/>' % (place['name'], place['geometry']['location']['lat'])
            #print ('%s: %s<br/>') % (place['name'], place['geometry']['location']['lat']['lng'])
            print str(place)
    return string_result
if __name__ == "__main__":
    app.run()

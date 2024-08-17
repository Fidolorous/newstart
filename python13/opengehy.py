# Exercise 1: Change geojson.py to print out the two-character country code from
# the retrieved data. Add error checking so your program does not traceback if the
# country code is not there. Once you have it working, search for “Atlantic Ocean”
# and make sure it can handle locations that are not in any country.

import urllib.request, urllib.parse
import json, ssl
import requests

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    if 'features' in js and js['features']:
        first_feature = js['features'][0]
    if 'properties' in first_feature and 'country_code' in first_feature['properties']:
        country = first_feature['properties']['country_code']
        print("Country code:", country)
    else:
        print("'country_code' does not exist in the properties of the first feature.")

    # print(json.dumps(js, indent=4))
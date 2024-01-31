""" Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
 The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
 and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like.
 If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter 
that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson 
and json endpoints so make sure you are using the same end point as this autograder is using. """


import urllib.request, urllib.parse, urllib.error
import json
import ssl

the_key = False
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


if the_key is False:
    the_key = 42
    the_link = 'http://py4e-data.dr-chuck.net/json?'
else :
    the_link = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    my_address = input('Enter location: ')
    if len(my_address) < 1 : break

    my_dict = dict()
    my_dict['address'] = my_address
    if the_key is not False: my_dict['key'] = the_key
    url = the_link + urllib.parse.urlencode(my_dict)
    print ('Retrieving', url)

    uh = urllib.request.urlopen(url, context=ctx)
    read_data = uh.read().decode()
    print ('Retrieved',len(read_data),'characters')

    try: 
        js = json.loads(read_data)
    except: 
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('= Failure To Retrieve =')
        print (read_data)
        continue

    place_id = js["results"][0]["place_id"]
    print ("Place Id:", place_id)  


    
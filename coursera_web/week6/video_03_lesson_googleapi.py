__author__ = 'srgtolm'

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Tnter locaation:')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sendor':'false',
                                         'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'charaters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '========Failure to Retrieve========'
        print data
        continue

    #print json.dumps(js, indent=4)

    lat = js['results'][1]["geometry"]["location"]["lat"]
    lng = js['results'][1]["geometry"]['location']['lng']
    print 'lat',lat, 'and lng', lng
    location = js['results'][0]['formatted_address']
    #print location
    #js = json.loads(str(data))
    #print json.dumps(js, indent=2), js
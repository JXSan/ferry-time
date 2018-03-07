from urllib2 import Request, urlopen, URLError
from transit import gtfs_realtime_pb2
import urllib

# MTA Live Feed API Link
train_url = 'http://datamine.mta.info/mta_esi.php?key=e4bf4522e761d29a01d146d75bba2d79'

# GTFS is the method we are using to parse the GTFS data
feed = gtfs_realtime_pb2.FeedMessage()

# Response is a variable used to open the URL 
response = urllib.urlopen(train_url)

# Feed has a method called ParseFromString to parse the URL that we opened in a readable format
feed.ParseFromString(response.read())

for entity in feed.entity:
    if entity.id == '000001':
        print entity.trip_update
    
'''   
request = Request(train_url)

try:
    response = urlopen(request)
    r = response.read()
    print r
except URLError, e:
    print 'Got an error code:', e
'''
import requests
from bs4 import BeautifulSoup
import math
from Tkinter import *
import xml
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
    
# St George Door 1
sgDoor1= Polygon([
    (40.6438818226571, -74.07182693503273), 
    (40.644093481758155, -74.0707755090989), 
    (40.6435887551014, -74.07064676306618), 
    (40.643572473532785, -74.07171964667214)
    ])

# St George Door 2
sgDoor2= Polygon([
    (40.64422373311693, -74.07202247147848), 
    (40.64468775173805, -74.07121072317614), 
    (40.64411926068469, -74.07080232019473), 
    (40.64397679795706, -74.0718947665082)
    ])

# St George Door 3
sgDoor3= Polygon([
    (40.644310567297715, -74.07220201703376), 
    (40.644694582393, -74.07122522587088), 
    (40.64520113554916, -74.07164901489523), 
    (40.64457369982163, -74.07237857574728)
    ])

# -------------------------------------------------- #

# Whitehall Door 1
whDoor1= Polygon([
    (40.70056013085226,-74.01321262126658), 
    (40.70050261595964,-74.01362031703684), 
    (40.69976066939244,-74.01362568145487), 
    (40.699743414722796,-74.01306241756174)
    ])

# Whitehall Door 2
whDoor2= Polygon([
   (-74.01312053214497,40.70059080558764), 
   (-74.01293814193195,40.70059080558764), 
   (-74.01262700568623,40.70009617611592), 
   (-74.01302397262043,40.69978559294257)
   ])

# Whitehall Door 3
whDoor3 = Polygon([
    (40.70061189425705, -74.01275932790213), 
    (40.7001057618909, -74.01253938676291), 
    (40.700077004254624, -74.01190102101737),  
    (40.7007384267477, -74.01226580144339)
    ])

# This function takes two points (Longitude/Latitude) and determines if it falls in a specified area
def dockCheck(latitude, longitude):
    
    # The vessels coordinates
    point = Point(latitude, longitude)
    
    if (sgDoor1.contains(point)):
        print('Docking in St George, Door 1')
    elif (sgDoor2.contains(point)):
        print('Docking in St George, Door 2')
    elif (sgDoor3.contains(point)):
        print('Docking in St George, Door 3')
    elif (whDoor1.contains(point)):
        print('Docking in WhiteHall, Door 1')
    elif (whDoor2.contains(point)):
        print('Docking in WhiteHall, Door 2')
    elif (whDoor3.contains(point)):
        print('Docking in Whitehall, Door 3')
    else:
        print("In Route")
        

    
# Test Run
dockCheck(40.6438, -74.070)
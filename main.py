'''
Ferry Time 

This application is for commuters who travel back and forth from Staten Island via the Ferry.

What we want to accomplish:
- Live feed of the ferries 
- Calculate estimated time of arrival of each individual ferry 
- Be able to determine when the ferry is 'in route', 'docking', or 'docked'
- Determine which slip (door) the ferry doors will be opening 
- Find out when the doors open or close 

How the application will work:
- Open the application
- You are presented with an option to choose between the two terminals (St Georgre vs Whitehall)
- Upon clicking a terminal, you will be presented with the 'Home Page' where it will show the ETA of the approaching ferry
- There will also be seperate tabs (Live Feed, Ferry Schedule, Contact)

// Live Feed \\
- This tab will display a live Google Maps representation of the ferry 

// Ferry Schedule \\
- This tab will be a static image (or table) of the ferry departure schedule

// Contact \\
- This tab will be used to contact the developers (us) for any feedback regarding the application

@author: Jonathan, Sekani, Ishrat, Catrina
@course: CSCI-440-M01
@title: SENIOR PROJECT
'''

#----------------------------------------------------------------------#
#                              IMPORTS                                 #
#----------------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup
import math
from Tkinter import *
import xml
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

#----------------------------------------------------------------------#
#                          GLOBAL VARIABLES                            #
#----------------------------------------------------------------------#

# Staten Island Vessel MMSI
JOHN_A_NOBLE = '367000110'
JOHN_F_KENNEDY = '367000190'
SAMUEL_I_NEWHOUSE = '367000140'
GUY_V_MOLINARI = '366952790'
ALICE_AUSTEN = '367000120'
ANDREW_J_BARBERI = '367000150'
SPIRIT_OF_AMERICA = '366952890'
SEN_JOHN_MARCHI = '366952870'

# KM -> MPH Converter 
km_converter = 0.621371

# Terminal coordinates 
stGeorge = [40.644212, -74.0725526]
whiteHall = [40.701098, -74.012913]

#----------------------------------------------------------------------#
#                          REQUEST HTML SITE                           #
#----------------------------------------------------------------------#

# The get function in the 'requests' library will...
r = requests.get('http://www.aishub.net/ais-hub-vessel-information.php?mmsi=367000140', headers={'User-Agent': 'Chrome'})

# BeautifulSoup will now take the HTML contents of the website and parse it into the 'soup' variable
soup = BeautifulSoup(r.content, "lxml")

#----------------------------------------------------------------------#
#                          GET FUNCTIONS                               #
#----------------------------------------------------------------------#

# Returns a live Feed of Vessel Coordinates
def get_coordinates(MMSI):
    
    # Call the 'get' function from the soup library to parse the HTML
    r = requests.get('http://www.aishub.net/ais-hub-vessel-information.php?mmsi=' + MMSI, headers={'User Agent': 'Chrome'})
    soup = BeautifulSoup(r.content, "lxml")
    
    # Found variable that will control whether or not we've located the LONGITUDE or LATITUDE in the links page source
    found = False
    
    # This list will hold the coordinates for the vessel 
    coordinates = []
    
    # This for loop will go through every <td> tag in the page source (This is where the coordinates are being held)
    for link in soup.find_all("td"):
        if(found == True):
            coordinates.append(link.text[:7])
            found = False
        if(link.text == 'LATITUDE:'):
            found = True
        elif(link.text == 'LONGITUDE:'):
            found = True
    return coordinates

# Returns the knots of the vessel in MPH
def get_knots(MMSI):
    
    # Call the 'get' function from the soup library to parse the HTML
    r = requests.get('http://www.aishub.net/ais-hub-vessel-information.php?mmsi=' + MMSI, headers={'User Agent': 'Chrome'})
    soup = BeautifulSoup(r.content, "lxml")
    
    # Conversion of knots to mph --> 1 knot = 1.15078 mph
    mph = 1.1507794
    
    # Found variable that will control whether or not we've located the LONGITUDE or LATITUDE in the links page source
    found = False
    
    # The speed is initialized as a string to make it easier to strip and print
    speed = ''
    
    # This for loop will go through every <td> tag in the page source and filter out the SOG (Knots)
    for link in soup.find_all("td"):
        if(found == True):
            speed = str(link.text[:2])
            found = False
        if(link.text == 'SOG:'):
            found = True
        
    # Strip any whitespace in the variable 'speed'
    speed = speed.strip(' ')
    
    # Convert knot into a float
    speed = float(speed) * mph    
            
    return speed


# This function returns the destination (St George vs Whitehall) of the vessel
def get_destination(MMSI):
    
    # Call the 'get' function from the soup library to parse the HTML
    r = requests.get('http://www.aishub.net/ais-hub-vessel-information.php?mmsi=' + MMSI, headers={'User Agent': 'Chrome'})
    soup = BeautifulSoup(r.content, "lxml")
    
    # Found variable that will control whether or not we've located the LONGITUDE or LATITUDE in the links page source
    found = False

    # This for loop will go through every <td> tag in the page source and filter out the destination
    for link in soup.find_all("td"):
        if(found == True):
            destination = str(link.text)
            found = False
        if(link.text == 'DESTINATION:'):
            found = True
            
    return destination

# This function returns the name of the vessel
def get_vessel_name(MMSI):
    
    # Call the 'get' function from the soup library to parse the HTML
    r = requests.get('http://www.aishub.net/ais-hub-vessel-information.php?mmsi=' + MMSI, headers={'User Agent': 'Chrome'})
    soup = BeautifulSoup(r.content, "lxml")
    
    # Found variable that will control whether or not we've located the LONGITUDE or LATITUDE in the links page source
    found = False

    # This for loop will go through every <h1> tag in the page source (There is only 1)
    for link in soup.find_all("h1"):
        name = link.text
        name = name.strip(' ')
        
    return name
            
# This function takes two lan/long coordinates (origin, destination) and return the amount of miles between the two
def get_miles(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    
    radius = 6371 # km
    
    # Convert to float
    lat1 = float(lat1)
    lon1 = float(lon1)
    
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d * km_converter

# This function takes two points (Longitude/Latitude) and determines if it falls in a specified area
def dockCheck(latitude, longitude):
    
    print("Entered dockCheck Function")
    
    # The vessels coordinates
    point = Point(latitude, longitude)
    
    # St George Door 1
    sgDoor1= Polygon([
        (-74.07162039048575,40.64358875503926), 
        (-74.07171142767857,40.64373528897797), 
        (-74.0708162286162,40.64404463734769), 
        (-74.07062656779789,40.643621318164556)
        ])
    
    # St George Door 2
    sgDoor2= Polygon([
        (-74.07186315639103,40.64400393369676), 
        (-74.07196936644931,40.64411790385683), 
        (-74.0710893402524,40.644573782551035), 
        (-74.07086174727044,40.64415046672397)
        ])
    
    # Whitehall Door 1
    whDoor1= Polygon([
        (-74.01350140582508,40.70053329072149), 
        (-74.01326537143177,40.7005447936987), 
        (-74.013125896563,40.699762586723956), 
        (-74.01356577884144,40.7001076791686)
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
        (40.7006, -74.0126), 
        (40.7006, -74.0124), 
        (40.7001, -74.0125), 
        (40.7002, -74.0122), 
        (40.7001, -74.012)
        ])
    '''
    if (sgDoor1.contains(point)):
        print('Docking in St George, Door 1')
    elif (sgDoor2.contains(point)):
        print('Docking in St George, Door 2')
    elif (whDoor1.contains(point)):
        print('Docking in WhiteHall, Door 1')
    elif (whDoor2.contains(point)):
        print('Docking in WhiteHall, Door 2')
    elif (whDoor3.contains(point)):
        print('Docking in Whitehall, Door 3')
    else:
        print("In Route")
    '''
    
    print(whDoor3.contains(point))

# This function is used to test out the application and verify all functions are working properly
def test(MMSI, destination):
    vessel_coordinates = get_coordinates(MMSI)
    miles = get_miles(vessel_coordinates, destination)
    speed = get_knots(MMSI)
    
    if(speed == 0 or miles < .1):
        print('The ferry ' + get_vessel_name(MMSI) + ' is docked at ' + get_destination(MMSI)) 
    elif (miles > .25):
        eta = float(miles/speed)
        eta = str((miles/speed) * 60)
        eta = eta[:2]
        eta = eta.strip('.')
        print(eta + ' minutes until the ferry ' + get_vessel_name(MMSI) + ' arrives at ' + get_destination(MMSI)) 
    elif (miles < .25):
        print("The ferry " + get_vessel_name(MMSI) + " is docking at " + get_destination(MMSI) + ', at slip #')
   
#----------------------------------------------------------------------#

# Test Run
#dockCheck(40.7001, -74.012)
#dockCheck(40.7001, -74.012)

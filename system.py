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
- You are presented with an option to choose between the two terminals (St George vs Whitehall)
- Upon clicking a terminal, you will be presented with the 'Home Page' where it will show the ETA of the approaching ferry
- There will also be separate tabs (Live Feed, Ferry Schedule, Contact)

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

''' IMPORTS '''
import random, time, datetime, sys, math
from database import cursor, conn
from main import *
''' IMPORTS '''

  
# Retrieve latitude from database by MMSI
def getLatitude(MMSI):
    
    # Check to see if the membership ID already exists in the database
    cursor.execute('SELECT latitude FROM location_tracking')
    check = str(cursor.fetchone()[0])
    print(check)
    
def setEntry(distance, longitude, latitude):

    try:
        cursor.execute("""
                       INSERT INTO ferrytime.location_tracking (tripID, distanceFromDock, longitude, latitude,
                       timestamp) VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP)
                       """, (distance, longitude, latitude))
        conn.commit()
        print('Entry successful')
    except:
        conn.rollback()
        print('Entry unsuccessful')
    
def trackBoat(MMSI):
    
    while True:
        
        # Get boat name
        vessel = str(get_vessel_name(MMSI))
        
        # Get boat MPH
        mph = str(get_knots(MMSI))
        
        # Get boat destination 
        direction = str(get_destination(MMSI))
        
        #Get boat speed in knots
        speed = get_knots(MMSI)
        
        # Boat ETA
        eta = 0
        
        #Status of boat
        status = ''
        
        print("Vessel: " + vessel)
        print('MPH: ' + mph)
        print('Direction: ' + direction)
        
        # Get coordinates of the boat
        coordinates = get_coordinates(MMSI)
        latitude = str(coordinates[0])
        longitude = str(coordinates[1])
        
        
        # If the direction of the boat is St George, calculate the miles from the boat to St George
        if (direction == 'ST GEORGE'):
            miles = str(get_miles(coordinates, stGeorge))
        # If the direction of the boat is Whitehall, calculate the miles from the boat to Whitehall
        elif (direction == 'WHITEHALL'):
            miles = str(get_miles(coordinates, whiteHall))
            
        # Convert the miles into a float, to make it easier to use in calculations
        miles = float(miles)
        
        # If the speed of the boat is 0 or below .1, the boat is docked.
        if(speed == 0 or miles < .1):
            print('The ferry ' + get_vessel_name(MMSI) + ' is docked at ' + get_destination(MMSI)) 
            status = 'Docked'
            print("Status: " + status)
            
            # Try to insert the data into the database
            try:
                cursor.execute("""
                               INSERT INTO ferrytime.boat_information (MMSI, vessel_name, destination, latitude, longitude,
                               mph, miles_to_dock, ETA, status, time, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, NULL)
                               """, (MMSI, vessel, direction, latitude, longitude, mph, miles, eta, status))
                conn.commit()
                print('Entry successful')
            except:
                conn.rollback()
                print('Entry unsuccessful')
            break
        
        # If the amount of miles to get to the destination is greater than .25, the boat is in route. 
        elif (miles > .25):
            eta = (miles/speed)
            eta = str((miles/speed) * 100)
            eta = eta[:2]
            eta = eta.strip('.')
            status = 'In Route'
            print(eta + ' minutes until the ferry ' + get_vessel_name(MMSI) + ' docks at ' + get_destination(MMSI)) 
            
        # If the amount of miles to get to the destination is less than .10, the boat is docking. 
        elif (miles < .10):
            status = 'Docking'
            print("Status: " + status)
            print("The ferry " + get_vessel_name(MMSI) + " is docking at " + get_destination(MMSI) + ', at slip #')
            
        try:
            cursor.execute("""
                           INSERT INTO ferrytime.boat_information (MMSI, vessel_name, destination, latitude, longitude,
                           mph, miles_to_dock, ETA, status, time, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, NULL)
                           """, (MMSI, vessel, direction, latitude, longitude, mph, miles, eta, status))
            conn.commit()
            print('Entry successful')
        except:
            conn.rollback()
            print('Entry unsuccessful')
            
        # The program runs every 2 minutes
        time.sleep(120)
     
# Track all boats
def run():
    while True:
        trackBoat(JOHN_A_NOBLE)
        trackBoat(JOHN_F_KENNEDY)
        trackBoat(SAMUEL_I_NEWHOUSE)
        trackBoat(GUY_V_MOLINARI)
        trackBoat(ALICE_AUSTEN)
        trackBoat(ANDREW_J_BARBERI)
        trackBoat(SPIRIT_OF_AMERICA)
        trackBoat(SEN_JOHN_MARCHI)
        time.sleep(120)
        
trackBoat(ANDREW_J_BARBERI)
    

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
from Tkinter import *
from main import *


#----------------------------------------------------------------------#
#                          GLOBAL VARIABLES                            #
#----------------------------------------------------------------------#
        
# Width/Height of the application window
WIDTH = 655
HEIGHT = 400

#----------------------------------------------------------------------#
#                          CREATE THE GUI                              #
#----------------------------------------------------------------------#
#Create the window
root = Tk()

#Modify the title
root.title("Ferry Time Location Tracking")
root.geometry("{}x{}".format(WIDTH, HEIGHT))

#
variable = StringVar(root)
variable.set("Choose Vessel")
w = OptionMenu(root, variable, "ALICE AUSTEN", "ANDREW J BARBERI", "GUY V MOLINARI", "JOHN A NOBLE", "JOHN_F_KENNEDY", "SAMUEL I NEWHOUSE", "SPIRIT OF AMERICA")
w.pack()

#----------------------------------------------------------------------#
#                        CREATE THE TOP TEXT                           #
#----------------------------------------------------------------------#

'''Choose Vessel'''
#vessel_label = Label(root, text='This tool will capture information on a specific ferry')
#vessel_label.place(x=0, y=20, anchor="w")
#vessel_label.config(font=("Courier", 16))

'''Line Seperator'''
f = Frame(root, height=1, width=WIDTH+HEIGHT, bg="black")
f.place(x=WIDTH/2-10, y=40, anchor="center")

#----------------------------------------------------------------------#
#                        CREATE THE BUTTONS                            #
#----------------------------------------------------------------------#

'''JOHN F KENNEDY'''
jfk_button = Button(root, text='John F Kennedy', command = lambda: displayJFKInfo())
jfk_button.place(x=80, y=60, anchor="center")
'''JOHN F KENNEDY'''


'''Line Seperator'''
f = Frame(root, height=1, width=WIDTH+HEIGHT, bg="black")
f.place(x=WIDTH/2-10, y=80, anchor="center")

#----------------------------------------------------------------------#
#                            VESSEL INFO                               #
#----------------------------------------------------------------------#
'''Status'''
status_label = Label(root, text='Status:')
status_label.place(x=0, y=100, anchor="w")
status_label.config(font=("Courier", 20))

'''Distance From Dock'''
eta_label = Label(root, text='Distance From Dock:')
eta_label.place(x=0, y=140, anchor="w")
eta_label.config(font=("Courier", 20))

'''Miles Per Hour'''
mph_label = Label(root, text='Miles Per Hour:')
mph_label.place(x=0, y=190, anchor="w")
mph_label.config(font=("Courier", 20))

'''Destination'''
destination_label = Label(root, text='Destination:')
destination_label.place(x=0, y=240, anchor="w")
destination_label.config(font=("Courier", 20))

'''TimeStamp'''
slip_label = Label(root, text='TimeStamp:')
slip_label.place(x=0, y=290, anchor="w")
slip_label.config(font=("Courier", 20))

'''Longitude'''
slip_label = Label(root, text='Longitude:')
slip_label.place(x=0, y=340, anchor="w")
slip_label.config(font=("Courier", 20))

'''Latitude'''
slip_label = Label(root, text='Latitude:')
slip_label.place(x=0, y=390, anchor="w")
slip_label.config(font=("Courier", 20))

#----------------------------------------------------------------------#
#                        BUTTON FUNCTIONS                              #
#----------------------------------------------------------------------#

def displayJFKInfo():
    ''' Grabbing data'''
    direction = None
    status = None
    eta = 0
    vessel_coordinates = get_coordinates(JOHN_F_KENNEDY)
    speed = get_knots(JOHN_F_KENNEDY)
    
    # Determine boat status
    if(speed < 1):
        status = 'Docked'
    elif(speed < .25):
        status = "Docking"
    else:
        status = "In Route"
    
    if(get_destination(JOHN_F_KENNEDY) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(JOHN_F_KENNEDY) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed > 0):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))
    
def displayJohnANobleInfo():
    '''Change Vessel Name'''
    vessel_label = Label(root, text='Vessel:')
    vessel_label = Label(root, text='Vessel: John A Noble   ')
    vessel_label.place(x=WIDTH/2-60, y=20, anchor="w")
    vessel_label.config(font=("Courier", 10))
    
    ''' Grabbing data'''
    direction = None
    status = None
    eta = 0
    vessel_coordinates = get_coordinates(JOHN_A_NOBLE)
    speed = get_knots(JOHN_A_NOBLE)
    
    # Determine boat status
    if(speed < 1):
        status = 'Docked'
    elif(speed < .25):
        status = "Docking"
    else:
        status = "In Route"
        
    
    if(get_destination(JOHN_A_NOBLE) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(JOHN_A_NOBLE) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed < 5 or speed > 1):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))
    
def displaySamuelNewHouseInfo():
    '''Change Vessel Name'''
    vessel_label = Label(root, text='Vessel:')
    vessel_label = Label(root, text='Vessel: Samuel Newhouse   ')
    vessel_label.place(x=WIDTH/2-60, y=20, anchor="w")
    vessel_label.config(font=("Courier", 10))
    
    ''' Grabbing data'''
    direction = None
    status = None
    eta = 0
    vessel_coordinates = get_coordinates(SAMUEL_I_NEWHOUSE)
    speed = get_knots(SAMUEL_I_NEWHOUSE)
    
    # Determine boat status
    if(speed < 1):
        status = 'Docked'
    elif(speed < .25):
        status = "Docking"
    else:
        status = "In Route"
    
    if(get_destination(SAMUEL_I_NEWHOUSE) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(SAMUEL_I_NEWHOUSE) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed > 0):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))
    
def displayGuyMolinariInfo():
    '''Change Vessel Name'''
    vessel_label = Label(root, text='Vessel:')
    vessel_label = Label(root, text='Vessel: Guy Molinari   ')
    vessel_label.place(x=WIDTH/2-60, y=20, anchor="w")
    vessel_label.config(font=("Courier", 10))
    
    ''' Grabbing data'''
    direction = None
    status = None
    eta = 0
    vessel_coordinates = get_coordinates(GUY_V_MOLINARI)
    speed = get_knots(GUY_V_MOLINARI)
    
    # Determine boat status
    if(speed < 1):
        status = 'Docked'
    elif(speed < .25):
        status = "Docking"
    else:
        status = "In Route"
    
    if(get_destination(GUY_V_MOLINARI) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(GUY_V_MOLINARI) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed > 0):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))

def displayAliceAustenInfo():
    '''Change Vessel Name'''
    vessel_label = Label(root, text='Vessel:')
    vessel_label = Label(root, text='Vessel: Alice Austen   ')
    vessel_label.place(x=WIDTH/2-60, y=20, anchor="w")
    vessel_label.config(font=("Courier", 10))
    
    ''' Grabbing data'''
    direction = None
    status = None
    eta = 0
    vessel_coordinates = get_coordinates(ALICE_AUSTEN)
    speed = get_knots(ALICE_AUSTEN)
    
    # Determine boat status
    if(speed < .25):
        status = 'Docked'
    elif(speed < 1):
        status = "Docking"
    else:
        status = "In Route"
    
    if(get_destination(ALICE_AUSTEN) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(ALICE_AUSTEN) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed > 0):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))

def displayAndrewBarberiInfo():
    '''Change Vessel Name'''
    vessel_label = Label(root, text='Vessel:')
    vessel_label = Label(root, text='Vessel: Andrew Barberi   ')
    vessel_label.place(x=WIDTH/2-60, y=20, anchor="w")
    vessel_label.config(font=("Courier", 10))
    
    ''' Grabbing data'''
    direction = None
    status = None
    eta = 0
    vessel_coordinates = get_coordinates(ANDREW_J_BARBERI)
    speed = get_knots(ANDREW_J_BARBERI)
    
    # Determine boat status
    if(speed < 1):
        status = 'Docked'
    elif(speed < .25):
        status = "Docking"
    else:
        status = "In Route"
    
    if(get_destination(ANDREW_J_BARBERI) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(ANDREW_J_BARBERI) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed > 0):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))
    
def displaySpiritOfAmericaInfo():

    ''' Grabbing data'''
    #direction = None
    #status = None
    eta = 0
    vessel_coordinates = get_coordinates(SPIRIT_OF_AMERICA)
    speed = get_knots(SPIRIT_OF_AMERICA)
    
    # Determine boat status
    if(speed < 1):
        status = 'Docked'
    elif(speed < .25):
        status = "Docking"
    else:
        status = "In Route"
    
    if(get_destination(SPIRIT_OF_AMERICA) == 'ST GEORGE'):
        miles = get_miles(vessel_coordinates, stGeorge)
        direction = 'St George'
    elif(get_destination(SPIRIT_OF_AMERICA) == 'WHITEHALL'):
        miles = get_miles(vessel_coordinates, whiteHall)
        direction = 'Whitehall'
    
    if(speed == 0 or miles < .1):
        '''Status'''
        status_label = Label(root, text=status)
        status_label.place(x=220, y=100, anchor="w")
        status_label.config(font=("Courier", 10))
    elif (miles < .15):
        status = 'Docking'
    
    if(speed > 0):
        eta = (miles/speed)
        eta = str((miles/speed) * 100)
        eta = eta[:2]
        eta = eta.strip('.')

    '''Status'''
    status_label = Label(root, text=status)
    status_label.place(x=220, y=100, anchor="w")
    status_label.config(font=("Courier", 10))
    
    '''Estimated Time of Arrival'''
    eta_label = Label(root, text= str(eta) + ' minutes')
    eta_label.place(x=220, y=140, anchor="w")
    eta_label.config(font=("Courier", 10))
    
    '''MPH'''
    mph_label = Label(root, text=str(speed) + 'mph')
    mph_label.place(x=220, y=190, anchor="w")
    mph_label.config(font=("Courier", 10))
    
    '''Destination'''
    destination_label = Label(root, text=direction)
    destination_label.place(x=220, y=240, anchor="w")
    destination_label.config(font=("Courier", 10))
    
    '''Slip #'''
    slip_label = Label(root, text='None')
    slip_label.place(x=220, y=290, anchor="w")
    slip_label.config(font=("Courier", 10))
    
    '''Latitude'''
    lat_label = Label(root, text=vessel_coordinates[0])
    lat_label.place(x=220, y=340, anchor="w")
    lat_label.config(font=("Courier", 10))
    
    '''Longitude'''
    longitude_label = Label(root, text=vessel_coordinates[1])
    longitude_label.place(x=220, y=390, anchor="w")
    longitude_label.config(font=("Courier", 10))

#----------------------------------------------------------------------#
#                           START THE GUI                              #
#----------------------------------------------------------------------#    
# Run GUI
root.mainloop()
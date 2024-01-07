#this script is written from something off github and James' hacking

import nau7802py #we need this to read the data from the qwiicScale
import time #we need this to do timer functions like wait a second
import qwiic #we need this to control the mux
import csv #we need CSV to write to a CSV file
from datetime import datetime #needed to write date and time to CSV
import requests


myScale = nau7802py.NAU7802() # Create instance of the NAU7802 class

#mux calls the MUX controller logic written by SparkFun
mux = qwiic.QwiicTCA9548A()

# Create an array from 0 to 7
numbers = list(range(8))

#define some global variables we will need later
globalInt = 0 #this is an Integer (number) that we need to start at 0 and will change to count through each Scale
data_pack = [] #this dataPack will hold the data from each scale before we post to a spreadsheet

# Loop through each number and print the message
for muxChannel in numbers:
    globalInt = muxChannel
    #first we are going to disable all channels on the mux
    mux.disable_channels([0,1,2,3,4,5,6,7])
    #we wait a second
    #time.sleep (1)
    #enable the current muxChannel of the array
    mux.enable_channels(muxChannel)
    #test print to display
    #print("I am at", globalInt)

    if not myScale.begin():
        print("Scale #" + str(globalInt) + " not detected. Please check wiring.")
        #time.sleep(1)
    else:
        #print("Scale #" + str(globalInt) + " connected!")
        #time.sleep(1)
        
        myScale.setGain(nau7802py.NAU7802_Gain_Values['NAU7802_GAIN_2']) # Gain can be set to 1, 2, 4, 8, 16, 32, 64, or 128.
        myScale.setSampleRate(nau7802py.NAU7802_SPS_Values['NAU7802_SPS_40']) # Sample rate can be set to 10, 20, 40, 80, or 320Hz
        myScale.calibrateAFE() # Does an internal calibration. Recommended after power up, gain changes, sample rate changes, or channel changes.
        
        currentReading = myScale.getReading();
        #print("Scale #" + str(globalInt) + " connected! - Value of scale: ", currentReading)
        #print('Reading: ', currentReading)
        #time.sleep(1)

        #set the current date and time
        current_datetime = datetime.now()
        #set the computer style datetime to human readable for our records
        human_readable_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        #get the current scale reading
        currentReading = myScale.getReading()
        #print the response to screen
        print('Date: ' + str(human_readable_datetime) + ' - Scale #' + str(muxChannel) + ', Reading: ' + str(currentReading))       
        #sleep or wait for 1 second and go again
        #time.sleep(1)


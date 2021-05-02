"""
Get Notfied when vaccine is available for 18+.
"""

import requests
import datetime
import time
from notify_run import Notify


notify = Notify()

# Suscribe on below URL to get notification
#https://notify.run/c/yntGnyLN93ukc43k 

todayDate = datetime.datetime.now()

PINCODE = 396445
DATE = "" +str( todayDate.day) + "-" + str(todayDate.month) + "-" + str(todayDate.year)
AGE = 18

slotsData = ""

# print("Enter PINCODE")
# PINCODE = int(input())
# print("Enter AGE")
# AGE = int(input())

def notifyUser(notificationData):
    notify.send(notificationData)


def checkvaccine():
    response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(PINCODE) + "&date=" + DATE)

    #print(response.json())

    vaccineSlots = response.json()
    slotAvailabe = True
    centerNumber = 1
    for center in vaccineSlots['centers']:
        for session in center['sessions']:
            if session['min_age_limit'] <= AGE:

                if len(session['slots']) > 0:
                    if slotAvailabe==True:
                        print("\nThe available slots are...\n")
                        slotsData = "Vaccine are availabe for age " + str(AGE) + " at these centers..."
                        slotAvailabe = False
                    
                    slotsData += "\n" + str(centerNumber) + ")  " + center['name']
                    print("Center Name    ",center['name'])
                    print("Minimum Age    ",session['min_age_limit'])
                    print("Slots avilabe  ",session['slots'])
                    print("-----------------------------------")

    if slotAvailabe:
        print("\nNO Slot Availabe for age " + str(AGE) +" on " + str(datetime.datetime.now()))
        #notifyUser("\nNO Slot Availabe for age " + str(AGE) +" on " + str(datetime.datetime.now()))
        return False
    else:
        notifyUser(slotsData)
    
    return True

while True:
    if checkvaccine():
        break
    time.sleep(3600)
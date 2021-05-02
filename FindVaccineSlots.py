import requests
import datetime

todayDate = datetime.datetime.now()

PINCODE = 396445
DATE = "" +str( todayDate.day) + "-" + str(todayDate.month) + "-" + str(todayDate.year)
AGE = 45

# print("Enter PINCODE")
# PINCODE = int(input())
# print("Enter AGE")
# AGE = int(input())


response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(PINCODE) + "&date=" + DATE)

#print(response.json())

vaccineSlots = response.json()
slotAvailabe = True

for center in vaccineSlots['centers']:
    for session in center['sessions']:
        if session['min_age_limit'] <= AGE:

            if len(session['slots']) > 0:
                if slotAvailabe==True:
                    print("\nThe available slots are...\n")
                    slotAvailabe = False

                print("Center Name    ",center['name'])
                print("Minimum Age    ",session['min_age_limit'])
                print("Slots avilabe  ",session['slots'])
                print("-----------------------------------")

if slotAvailabe:
    print("\nNO Slot Availabe")
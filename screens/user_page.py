# Author: Ronak

from state import __state
from features.booking import new_booking, see_current_bookings, cancel_booking
from features.feedback import give_feedback
from features.issue import create_issue
from features.personal_information import personal_information
import os

def user_page(db):
    while(True):
        print("[1] Make new booking")
        print("[2] See current bookings")
        print("[3] Cancel booking")
        print("[4] Provide feedback")
        print("[5] Manage personal information")
        print("[6] Create an issue")
        print("[7] Exit\n")

        try:
            option = int(input("Choose an option: "))
            print()
        except:
            print("Invalid option selected!!!")
            continue

        current_user_id = __state['current_user_id']

        if(option == 1):
            new_booking(db, current_user_id)
        elif(option == 2):
            see_current_bookings(db, current_user_id)
        elif(option == 3):
            cancel_booking(db, current_user_id)
        elif(option == 4):
            give_feedback(db, current_user_id)
        elif(option == 5):
            SECRET_KEY = os.getenv('SECRET_KEY').encode("utf-8")
            personal_information(db, current_user_id, SECRET_KEY)
        elif(option == 6):
            create_issue(db, current_user_id)
        elif(option == 7):
            return

        print('\n')
        break

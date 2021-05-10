# Author: Karishma and Ronak

from state import __state
from features.admin import see_open_issues, see_latest_bookings, export_data_csv, resolve_open_issues, booking_analitics_by_date, booking_analitics_by_location, booking_analitics_by_price, issue_analitics
from recovery import import_data_csv

def admin_page(db):
    while (True):
        print("[1] See Open Issues")
        print("[2] Resolve Open Issues")
        print("[3] See Latest 15 Bookings")
        print("[4] Exporting All Tables in CSV")
        print("[5] Import Data from CSV files")
        print("[6] Booking Analytics & Reports")
        print("[7] Exit\n")

        try:
            option = int(input("Choose an option: "))
            print()
        except:
            print("Invalid option selected!!!")
            continue

        current_user_id = __state['current_user_id']

        if (option == 1):
            see_open_issues(db, current_user_id)
        elif (option == 2):
            resolve_open_issues(db, current_user_id)
        elif (option == 3):
            see_latest_bookings(db, current_user_id)
        elif (option == 4):
            export_data_csv(db, current_user_id)
        elif (option == 5):
            import_data_csv()
        elif (option == 6):
            booking_analitics_by_date(db, current_user_id)
            booking_analitics_by_location(db, current_user_id)
            booking_analitics_by_price(db, current_user_id)
            issue_analitics(db, current_user_id)
        elif (option == 7):
            return

        print('\n')

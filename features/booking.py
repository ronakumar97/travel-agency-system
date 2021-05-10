# Author: Ronak

from classes.booking import Booking
from transform import make_changes
from input_checks import booking_inputs
from datetime import datetime
from features.payment import payment

# Create a new booking method
def new_booking(db, user_id):
    while(True):
        start_location = input("From (Enter the city name): ").upper()
        end_location = input("To (Enter the destination name) : ").upper()
        start_date = input("Start Date: (In YYYY-MM-DD format): ")
        end_date = input("End Date(Do not enter the details for one way travel): (In YYYY-MM-DD format): ")
        type = input("Type: (AIR/RAIL/CAR): ")
        number = int(input("Number of people: "))

        errors = booking_inputs(db, start_location, end_location, start_date, end_date, type)

        if(errors != True):
            print('Errors : ' + str(errors))
            continue

        break

    price = make_changes(db, start_location, end_location, start_date, end_date, type, number)

    print("\nThe Booking Amount for the transaction is -> {}\n".format(price))

    booking = Booking(user_id, start_location, end_location, price, start_date, end_date, type, number)

    payment_result = payment(booking.user_id, price)

    if(payment_result == False):
        print("Error in Payment. Please Try Again...")
        return

    print("Payment Successful...")

    result = insert(db, "BOOKING", booking)

    if(result is not False):
        print("Booking confirmed... Booking ID is {}".format(result))

def see_current_bookings(db, user_id):
    current_bookings = get_current_bookings(db, user_id)
    number = 1
    for booking in current_bookings:
        start_location = booking[0]
        end_location = booking[1]
        print(str(number) + ") " + start_location + " --> " + end_location)
        number += 1

def cancel_booking(db, user_id):
    current_bookings = get_current_bookings(db, user_id)
    number = 1
    for booking in current_bookings:
        start_location = booking[0]
        end_location = booking[1]
        print(str(number) + ") " + start_location + " --> " + end_location)
        number += 1

    while (True):
        try:
            option = int(input("Choose the option to cancel the booking: "))
        except:
            print("Invalid option selected!!!")
            continue

        if (option > len(current_bookings)):
            print('ERROR: Wrong Option selected')
            continue
        break

    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM BOOKING WHERE BookingID={}".format(current_bookings[option-1][2]))
        db.commit()
        print('Cancelled Booking...')
    except:
        print("DB Error!!!")

def get_current_bookings(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT StartLocation, EndLocation, BookingID FROM BOOKING WHERE UserID={}".format(user_id))
    bookings = cursor.fetchall()
    return bookings

def insert(db, table_name, booking):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO " + table_name + "(UserID, StartLocation, EndLocation, Type, Price, StartDate, EndDate, Status, Number, Timestamp) VALUES (?,?,?,?,?,?,?,?,?,?)", (booking.user_id, booking.start_location, booking.end_location, booking.type, booking.price, booking.start_date, booking.end_date, 'CONFIRMED', booking.number, datetime.now()))
        db.commit()
    except:
        print("DB Error!!!")
        return False
    return cursor.lastrowid

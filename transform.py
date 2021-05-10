# Author: Ronak

from haversine import haversine
from state import __price

# Computes Booking price
def compute_price(distance, type, number):
    if(type == 'AIR'):
        return __price['AIR'] * int(distance) * number
    if (type == 'RAIL'):
        return __price['RAIL'] * int(distance) * number
    if (type == 'CAR'):
        return __price['CAR'] * int(distance) * number

def make_changes(db, start_location, end_location, start_date, end_date, type, number):
    cursor = db.cursor()
    cursor.execute("SELECT Coordinates FROM LOCATION WHERE City = ?", (start_location,))
    start_location = cursor.fetchone()
    cursor.execute("SELECT Coordinates FROM LOCATION WHERE City = ?", (end_location,))
    end_location = cursor.fetchone()
    distance = haversine(eval(start_location[0]), eval(end_location[0]))
    print('\nDistance is ' + str(distance))
    price = compute_price(distance, type, number)
    if(end_date != ''):
        price = price * 2
    return price


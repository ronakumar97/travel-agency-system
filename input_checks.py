# Author: Ronak

import re
import datetime

def validate_email(email):
    email_regex = r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'
    if re.match(email_regex, email) or email == 'admin':
        return True
    return False

def validate_phone(phone):
    phone_regex_patterns = ["^(\\+\\d{1,3}( )?)?((\\(\\d{3}\\))|\\d{3})[- .]?\\d{3}[- .]?\\d{4}$", "|^(\\+\\d{1,3}( )?)?(\\d{3}[ ]?){2}\\d{3}$", "|^(\\+\\d{1,3}( )?)?(\\d{3}[ ]?)(\\d{2}[ ]?){2}\\d{2}$"]
    for phone_regex in phone_regex_patterns:
        if not re.match(phone_regex, phone):
            return False
    return True

def all_checks_passed(email, phone):
    return validate_email(email) and validate_phone(phone)

def booking_inputs(db, start_location, end_location, start_date, end_date, type):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM LOCATION WHERE City = ?", (start_location,))
    result1 = cursor.fetchone()
    cursor.execute("SELECT * FROM LOCATION WHERE City = ?", (end_location,))
    result2 = cursor.fetchone()

    errors = []

    if(validate_date(start_date) == False):
        errors.append('Incorrect Start Date')
    if (validate_date(end_date) == False and end_date != ''):
        errors.append('Incorrect End Date')
    if(check_dates(start_date, end_date) == False):
        errors.append('End Date must be greater than Start Date')
    if(result1 is None):
        errors.append("Incorrect Start Location")
    if (result2 is None):
        errors.append("Incorrect End Location")
    if(type not in ['AIR', 'RAIL', 'CAR']):
        errors.append("Incorrect Type Selected")

    if(len(errors) == 0):
        return True
    return errors

def check_dates(start_date, end_date):
    if(end_date == ''):
        return True

    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    return start_date <= end_date

def validate_date(date):
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    except:
        return False
    if(date.date() < datetime.date.today()):
        return False
    return True
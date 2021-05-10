# Author: Karishma and Ronak

import pandas as pd
import matplotlib.pyplot as plt

def see_open_issues(db, user_id):
    open_issue = fetch_open_issues(db, user_id)
    number = 1
    for issues in open_issue:
        issue_new = issues[1]
        issue_date = issues[2]
        print(str(number) + ": Issue Date: " + issue_date + " Issue: " + issue_new)
        number += 1

def see_latest_bookings(db, user_id):
    all_latest_bookings = fetch_latest_bookings(db, user_id)
    number = 1
    for latest_booking in all_latest_bookings:
        StartLocation = latest_booking[0]
        EndLocation = latest_booking[1]
        Type = latest_booking[2]
        Price = latest_booking[3]
        StartDate = latest_booking[4]
        EndDate = latest_booking[5]
        Status = latest_booking[6]
        print(str(number) + ": ( " + StartLocation + " --> " + EndLocation + " ) Booking Type: " + Type + " Price: " + str(Price) + " Dates: (" + StartDate + " --> " + EndDate+ " )" + " Status: " + Status)
        number += 1

def resolve_open_issues(db, user_id):
    open_issue = fetch_open_issues(db, user_id)
    number = 1
    for issues in open_issue:
        issue_new = issues[1]
        issue_date = issues[2]
        print(str(number) + ": Issue Date: " + issue_date + " Issue: " + issue_new)
        number += 1

    while(True):
        try:
            option = int(input("Choose an option: "))
            print()
        except:
            print("Invalid option selected!!!")
            continue
        if (option > len(open_issue)):
            print('ERROR: Wrong Option selected')
            continue

        break

    try:
        cursor = db.cursor()
        issue_id = open_issue[option-1][0]
        cursor.execute("UPDATE ISSUE SET Resolved = ? WHERE IssueID = ?", ("YES", issue_id))
        db.commit()
        print('Issue Marked as Resolved...')
    except:
        print('DB Error!!!')


def fetch_open_issues(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT IssueID, Issue, Timestamp FROM ISSUE WHERE Resolved='NO'")
    issues = cursor.fetchall()
    return issues

def fetch_latest_bookings(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT StartLocation, EndLocation, Type, Price, StartDate, EndDate, Status FROM BOOKING ORDER BY Timestamp DESC LIMIT 15")
    latest_bookings = cursor.fetchall()
    return latest_bookings

def export_data_csv(db, user_id):
    all_bookings = fetch_all_bookings(db, user_id)
    df = pd.DataFrame(all_bookings, columns=['BookingID', 'UserID', 'StartLocation', 'EndLocation', 'Type', 'Price', 'StartDate', 'EndDate', 'Status', 'Number', 'Timestamp'])
    df.to_csv('BOOKING.csv', index=False, header=True)

    all_issues = fetch_all_issues(db, user_id)
    df = pd.DataFrame(all_issues, columns=['IssueID', 'UserID', 'Issue', 'Resolved', 'Timestamp'])
    df.to_csv('ISSUE.csv', index=False, header=True)

    all_accounts = fetch_all_accounts(db, user_id)
    df = pd.DataFrame(all_accounts, columns=['AccountID', 'UserID', 'AccountNumber', 'Balance', 'CardNumber', 'CVV', 'Expiry', 'Password'])
    df.to_csv('ACCOUNT.csv', index=False, header=True)

    all_feedbacks = fetch_all_feedbacks(db, user_id)
    df = pd.DataFrame(all_feedbacks, columns=['FeedbackID', 'UserID', 'Feedback'])
    df.to_csv('FEEDBACK.csv', index=False, header=True)

    all_locations = fetch_all_locations(db, user_id)
    df = pd.DataFrame(all_locations, columns=['LocationID', 'City', 'Country', 'Coordinates'])
    df.to_csv('LOCATION.csv', index=False, header=True)

    all_users = fetch_all_users(db, user_id)
    df = pd.DataFrame(all_users, columns=['UserID', 'Email', 'Password', 'Phone', 'Name'])
    df.to_csv('USER.csv', index=False, header=True)

    print('Data exported successfully...')

def fetch_all_bookings(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT BookingID, UserID, StartLocation, EndLocation, Type, Price, StartDate, EndDate, Status, Number, Timestamp FROM BOOKING")
    all_bookings = cursor.fetchall()
    return all_bookings

def fetch_all_issues(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT IssueID, UserID, Issue, Resolved, Timestamp FROM ISSUE")
    all_issues = cursor.fetchall()
    return all_issues

def fetch_all_accounts(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT AccountID, UserID, AccountNumber, Balance, CardNumber, CVV, Expiry, Password FROM ACCOUNT")
    all_accounts = cursor.fetchall()
    return all_accounts

def fetch_all_feedbacks(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT FeedbackID, UserID, Feedback FROM FEEDBACK")
    all_feedbacks = cursor.fetchall()
    return all_feedbacks

def fetch_all_locations(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT LocationID, City, Country, Coordinates FROM LOCATION")
    all_locations = cursor.fetchall()
    return all_locations

def fetch_all_users(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT UserID, Email, Password, Phone, Name FROM USER")
    all_users = cursor.fetchall()
    return all_users

def booking_analitics_by_date(db, user_id):
    all_bookings_date = fetch_totalBooking_dates(db, user_id)

    total_booking = [None] * len(all_bookings_date)
    dates = [None] * len(all_bookings_date)
    number = 0
    for booking_data in all_bookings_date:
        total_booking[number] = booking_data[0]
        dates[number] = booking_data[1]
        number += 1

    plt.scatter(dates, total_booking)
    plt.xlabel("Dates", fontsize=16)
    plt.ylabel("Total Booking", fontsize=16)
    plt.title("Total Booking over Dates", fontsize=25)
    plt.show()

def booking_analitics_by_location(db, user_id):
    all_bookings_location = fetch_totalBooking_location(db, user_id)

    total_booking = [None] * len(all_bookings_location)
    location = [None] * len(all_bookings_location)
    number = 0
    for booking_data in all_bookings_location:
        total_booking[number] = booking_data[0]
        location[number] = booking_data[1]
        number += 1

    plt.scatter(location, total_booking)
    plt.xlabel("Location", fontsize=16)
    plt.ylabel("Total Booking", fontsize=16)
    plt.title("Total Booking over Location", fontsize=25)
    plt.show()

def booking_analitics_by_price(db, user_id):
    all_bookings_price_date = fetch_totalPrice_dates(db, user_id)

    total_booking_price = [None] * len(all_bookings_price_date)
    dates = [None] * len(all_bookings_price_date)
    number = 0
    for booking_data in all_bookings_price_date:
        total_booking_price[number] = booking_data[0]
        dates[number] = booking_data[1]
        number += 1

    plt.scatter(dates, total_booking_price)
    plt.xlabel("Dates", fontsize=16)
    plt.ylabel("Total Booking Price", fontsize=16)
    plt.title("Total Booking Price over Date", fontsize=25)
    plt.show()

def issue_analitics(db, user_id):
    total_Issue_resolved = fetch_totalIssue_resolved(db, user_id)
    total_issues_count = [None] * len(total_Issue_resolved)
    issue_status = [None] * len(total_Issue_resolved)
    number = 0
    for issues in total_Issue_resolved:
        total_issues_count[number] = issues[0]
        issue_status[number] = issues[1]
        number += 1

    plt.scatter(issue_status, total_issues_count)
    plt.pie(total_issues_count, labels=issue_status, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Total Number of Issues By their Status")
    plt.show()

def fetch_totalBooking_dates(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT count(BookingID), date(Timestamp)  FROM BOOKING group by date(Timestamp)")
    booking_date = cursor.fetchall()
    return booking_date

def fetch_totalBooking_location(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT count(BookingID), EndLocation   FROM BOOKING group by EndLocation")
    booking_location = cursor.fetchall()
    return booking_location

def fetch_totalPrice_dates(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT sum(price), date(Timestamp)  FROM BOOKING group by date(Timestamp)")
    booking_price_date = cursor.fetchall()
    return booking_price_date

def fetch_totalIssue_resolved(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT count(IssueID), Resolved  FROM ISSUE group by Resolved")
    total_issue_resolved = cursor.fetchall()
    return total_issue_resolved
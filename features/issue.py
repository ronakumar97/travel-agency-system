# Author: Ronak

from classes.issue import Issue
from datetime import datetime

def create_issue(db, user_id):
    issue = input("Type in your issue: ")

    issue = Issue(user_id, issue)

    result = insert(db, "ISSUE", issue)

    if (result is not False):
        print("Issue saved...")

def insert(db, table_name, issue):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO " + table_name + "(UserID, Issue, Resolved, Timestamp) VALUES (?,?,?,?)", (issue.user_id, issue.issue, issue.resolved, datetime.now()))
        db.commit()
    except:
        print("DB Error!!!")
        return False
    return True
# Author: Ronak

from classes.feedback import Feedback

def give_feedback(db, user_id):
    feedback = input("Type in your feedback: ")

    feedback = Feedback(user_id, feedback)

    result = insert(db, "FEEDBACK", feedback)

    if (result is not False):
        print("Feedback saved...")

def insert(db, table_name, feedback):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO " + table_name + "(UserID, Feedback) VALUES (?, ?)", (feedback.user_id, feedback.feedback))
        db.commit()
    except:
        print("DB Error!!!")
        return False
    return True

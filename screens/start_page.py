# Author: Vincent

import bcrypt
from state import __state
from input_checks import all_checks_passed

def start_page(db, SECRET_KEY):
    while(True):
        print("[1] Login")
        print("[2] Create Account")
        print("[3] Exit")
        print()
        try:
            option = int(input("Choose an option: "))
            print()
        except:
            print("Invalid option selected!!!")
            continue

        if(option == 1):
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            cur = db.cursor()
            cur.execute("SELECT * FROM USER WHERE email = ?", (email,))

            user = cur.fetchone()

            if(user is None or not bcrypt.checkpw(password.encode("utf-8"), user[2])):
                print("ERROR: Invalid Credentials.")
            else:
                print("You are now logged in as {}\n".format(email))
                __state['current_user_id'] = user[0]
                __state['current_email'] = email
                if(email == 'admin@holidaytravelagency.com'):
                    __state['is_admin'] = True

        elif(option == 2):
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            phone = input("Enter Phone Number: ")
            name = input("Enter your Name: ")

            if(all_checks_passed(email, phone) == False):
                print("ERROR: Incorrect details!!. Please Fill Again")
                continue

            hashed = bcrypt.hashpw(password.encode("utf-8"), SECRET_KEY)

            cur = db.cursor()

            cur.execute("SELECT * FROM USER WHERE email = ?", (email,))
            user = cur.fetchone()
            if(user is None):
                cur.execute("INSERT INTO USER(email, password, phone, name) VALUES (?, ?, ?, ?)", (email, hashed, phone, name))
                db.commit()
                print("Account created successfully...\n")
            else:
                print("ERROR: Email already registered.")

        elif(option == 3):
            return

        else:
            print("ERROR: Invalid option selected!!!")

        break

    cur.close()
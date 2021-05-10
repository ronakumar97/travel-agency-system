import bcrypt
from db_operations import get_connection
import os
import input_checks

def personal_information(db, user_id, SECRET_KEY):
    while(True):
        print("[1] Changing Password")
        print("[2] Changing Phone Number")
        print("[3] Changing Name")
        print("[4] Exit")
        conn = get_connection()
        cur = conn.cursor()
        try:
            option = int(input("Choose an option: "))

        except:
            print("Invalid option selected!!!")
            continue

#Changing Password
        if(option == 1):

            updating_password = input("Enter your new password ")
            updated_hashed = bcrypt.hashpw(updating_password.encode("utf-8"), SECRET_KEY)
            cur.execute(" UPDATE USER SET PASSWORD = ? WHERE UserID = ? ", (updated_hashed, user_id))
            conn.commit()
            print("Your password is updated\n")

#Changing Phone
        elif(option == 2):

            updating_phone = input("Enter your new phone number ")
            if input_checks.validate_phone(updating_phone)== True:
                cur.execute(" UPDATE USER SET Phone = ? WHERE UserID = ? ", (updating_phone,user_id))
                conn.commit()
                print("Your Phone number is updated\n")
            else:
                print("Invalid Phone number Format")
                continue

#Changing Name
        elif (option == 3):

            updating_name = input("Enter your new Name ")
            cur.execute(" UPDATE USER SET Name = ? WHERE UserID = ? ", (updating_name,user_id))
            conn.commit()
            print("Your Name is updated\n")

#Exit
        elif (option == 4):
            exit()
        else:
            print("You have opted the wrong option")
            continue

    cur.close()
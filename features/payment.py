# Author: Jay

from db_operations import get_connection
import bcrypt
import os

# Payment method
def payment(UserId, amount):
    conn = get_connection()
    cur = conn.cursor()
    sql = 'SELECT AccountID FROM ACCOUNT WHERE UserID = ?'
    cur.execute(sql, (UserId, ))
    data = cur.fetchall()
    if len(data) == 0:
        print('Add money using Account Number and Card details.')
        while True:
            try:
                acc_num =int(input('Enter your Account Number(System doesnt allow numbers starting from "0") : \n'))
                card_num = int(input('Enter your 16 digit credit or debit card number in numeric format(System doesnt allow numbers starting from "0") \n'))
                _cvv = int(input('Enter 3 digit cvv number (System doesnt allow numbers starting from "0")  \n'))
                _expiry = input('Enter card expiry date in MM/YY format \n')
                a = _expiry.split("/")
                month,year= a[0],a[1]
                password = int(input('enter your four digit pin (System doesnt allow numbers starting from "0") \n'))
            except:
                print("Wrong inputs")
                continue
            break
        card_num = str(card_num)
        _cvv = str(_cvv)
        _expiry = str(_expiry)
        password = str(password)
        if len(card_num) == 16  and len(_cvv) == 3  and (len(_expiry) == 3 or len(_expiry) == 5) and int(month) <= 12 and int(year) >= 21 and len(password) == 4: # Check the expiry date part
            card_num = int(card_num)
            _cvv = int(_cvv)
            _expiry = int(month + year)
            pwd = int(password)
            sql = 'INSERT INTO ACCOUNT (UserID, AccountNumber, Balance, CardNumber, CVV, Expiry, Password) VALUES (?,?,?,?,?,?,?)'
            cur.execute(sql, (
                UserId,
                acc_num,
                0.0,
                card_num,
                _cvv,
                _expiry,
                bcrypt.hashpw(str(pwd).encode("utf-8"), os.getenv('SECRET_KEY').encode("utf-8")),
                ))
            conn.commit()
            balance = 0.0
            req = amount - balance
            print('Required amount to be added for transaction : ' + str(req))
            added_bal = float(input('Enter money you want to add : '))
            added_bal = added_bal + balance
            if added_bal < amount:
                Required_amount = amount - added_bal
                print('Amount not sufficient, You need to add ' + Required_amount + ' to complete Transaction.')
                additional_amount = int(input('Enter money you want to add : '))
                added_bal = added_bal + additional_amount
            sql = 'UPDATE ACCOUNT SET Balance=? WHERE UserID = ?'
            cur.execute(sql, (added_bal-amount, UserId))
            conn.commit()
            return True
        else:
            print("Enter the correct values!!! \n This might be due to following reasons \n 1.Incorrect cvv ,account details. Please enter them in correct format") #TODO: Make the function
            return False
    else:
        sql = 'SELECT Balance FROM ACCOUNT WHERE UserID = ?'
        cur.execute(sql, (UserId, ))
        for r in cur:
            balance = int(r[0])
        if balance < amount:
            req = amount - balance
            print('Required amount to be added for transaction : ' + str(req))
            added_bal = int(input('Enter money you want to add : '))
            added_bal = added_bal + balance
            if added_bal < amount:
                Required_amount = amount - added_bal
                print('Amount not sufficient, You need to add ' + str(Required_amount) + ' to complete Transaction.')
                additional_amount = int(input('Enter money you want to add : '))
                added_bal = added_bal + additional_amount
            sql = 'UPDATE ACCOUNT SET Balance=? WHERE UserID = ?'
            cur.execute(sql, (added_bal-amount, UserId))
            conn.commit()
            return True
        else:
            print('Sufficient Balance For Transaction.\nDo you want to Proceed ? (yes/no)')
            d = input()
            if d.lower() == 'yes':
                remaining_bal = balance - amount
                sql = 'UPDATE ACCOUNT SET Balance=? WHERE UserID = ?'
                cur.execute(sql, (remaining_bal, UserId))
                conn.commit()
                return True
            else:
                return False

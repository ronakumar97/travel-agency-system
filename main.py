# Author: Ronak

import os
from db_operations import get_connection
from screens.welcome_page import welcome_page
from screens.start_page import start_page
from screens.user_page import user_page
from screens.admin_page import admin_page
from state import __state
from dotenv import load_dotenv
load_dotenv()

def main():
    # Gets Secret Key from the .env file
    SECRET_KEY = os.getenv('SECRET_KEY').encode("utf-8")
    db = get_connection()
    # Shows different screens based upon whether the user is admin or normal user
    welcome_page()
    start_page(db, SECRET_KEY)
    if(__state['current_user_id'] != None):
        admin_page(db) if __state['is_admin'] == True else user_page(db)

if __name__ == '__main__':
    main()

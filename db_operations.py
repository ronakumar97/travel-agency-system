# Author: Ronak

import sqlite3
import os

def get_connection():
    connection = sqlite3.connect(os.getenv('DB_URL'))
    return connection

def get_recovery_connection():
    connection = sqlite3.connect(os.getenv('REP_DB_URL'))
    return connection
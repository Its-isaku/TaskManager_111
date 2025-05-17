
#? library imports
import sqlite3
from flask import g  #* g = Global context object |

#? This is the database URI. It is used to connect to the database.
DATABASE_URI = "main.db"

#? * This function is used to get a database connection.
def get_db():
    # * Sets the database connection.
    db = getattr(g, "_database", None)
    
    # * If the connection does not exist, create a new one.
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URI)
    return db
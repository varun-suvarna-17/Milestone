import sqlite3
from utils.logger import logger  

def get_connection():
    try:
        conn = sqlite3.connect('company.db')
        return conn 
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        return None
    finally:
        logger.info("Database connection attempted")

def close_connection(conn):
    conn.close()
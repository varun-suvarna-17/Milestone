from db.connection import get_connection, close_connection
from utils.logger import logger

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = get_connection()

        if not self.conn:
            logger.error("Database connection failed")
            return None

        self.cursor = self.conn.cursor()
        logger.info("DatabaseManager connected successfully")
        return self.cursor

    def commit(self):
        if self.conn:
            self.conn.commit()
            logger.info("Database changes committed")

    def close(self):
        if self.conn:
            close_connection(self.conn)
            logger.info("Database connection closed")
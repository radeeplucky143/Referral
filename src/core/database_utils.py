import os
import sqlite3
from core.yaml_utils import Yaml
from core.logger_utils import Logger


class Database:

    def __init__(self):
        self.config = Yaml().load_yaml()
        self.conn = sqlite3.connect(self.config['database']['name'])
        self.cursor = self.conn.cursor()
        self.parent_dir = os.path.dirname(os.path.dirname(__file__))
        self.logger = Logger(__name__, self.parent_dir).create_log_file()
        self.logger.info(f"connection established to database {self.config['database']['name']}")

    def execute(self, command):
        try:
            self.logger.info(f'Executing command: {command}')
            self.cursor.execute(command)
            self.conn.commit()
            self.logger.info("commiting to the database.")
        except Exception as err:
            self.logger.error(f"Execution failed while executing the command: {err}")

    def close_connection(self):
        self.conn.close()
        self.logger.info("Connection to the database closed.")

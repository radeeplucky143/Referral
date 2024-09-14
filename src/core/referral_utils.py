from core.logger_utils import Logger
from api.models import MiningUser
from core.yaml_utils import Yaml
from core.database_utils import Database
import random
import string
import os


class Referral:

    def __init__(self):
        self.parent_dir = os.path.dirname(os.path.dirname(__file__))
        self.logger = Logger(__name__, self.parent_dir).create_log_file()
        self.config = Yaml().load_yaml()
        self.logger.info("config file loaded successfully.")


    def generate_referral_code(self, user: MiningUser, length=8):
        """Generates a 8 digit referral code consiting upper case alphabets and digits.

        Returns:
            A random string of uppercase letters and digits.
        """
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))

        database = Database()
        values = (user.user_name, user.email, code)
        insertion_cmd = self.config['database']['commands']['users_table_insertion'].format(values)
        database.execute(insertion_cmd)
        database.close_connection()

        self.logger.info(f"Referral code generated for {user.user_name}: {code}")
        return code

from core.logger_utils import Logger
import random
import string
import os

def generate_referral_code(length=8):
    """Generates a 8 digit referral code consiting upper case alphabets and digits.

    Returns:
        A random string of uppercase letters and digits.
    """
    parent_dir = os.path.dirname(os.getcwd())
    logger = Logger(__name__, parent_dir).create_log_file()
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    logger.info(f"Referral code generated: {code}")
    return code

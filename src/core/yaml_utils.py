import os
import yaml
from core.logger_utils import Logger

class Yaml:

    def __init__(self):
        self.parent_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_name = os.path.join(self.parent_dir, 'config', 'config.yaml')
        self.data = None
        self.logger = Logger(__name__, self.parent_dir).create_log_file()

    def load_yaml(self):
        try:
            with open(self.file_name, 'r') as f:
                self.logger.info(f'Loading the {self.file_name} file')
                self.data = yaml.safe_load(f)
                return self.data

        except yaml.YAMLError as e:
            self.logger.error(f"Error parsing YAML file: {e}")

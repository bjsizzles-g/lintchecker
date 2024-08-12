import os
import yaml
import logging
from lightspeed_lint.rules import load_rules

class Linter:
    def __init__(self, directory):
        self.directory = directory
        self.rules = load_rules()

    def run(self):
        logging.info(f"Starting linting in directory: {self.directory}")
        self.check_top_level_files()
        yaml_files = self.find_yaml_files(self.directory)
        for file_path in yaml_files:
            self.lint_file(file_path)

    def check_top_level_files(self):
        top_level_files = ['site.yaml', 'privileged-playbook.yaml', 'playbook.yaml']
        found_files = [f for f in top_level_files if os.path.exists(os.path.join(self.directory, f))]
        if not found_files:
            logging.error("No top-level playbook file found!")
        else:
            logging.info(f"Found top-level file(s): {', '.join(found_files)}")

    def find_yaml_files(self, directory):
        yaml_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.yaml') or file.endswith('.yml'):
                    yaml_files.append(os.path.join(root, file))
        return yaml_files

    def lint_file(self, file_path):
        logging.info(f"Linting file: {file_path}")
        with open(file_path, 'r') as f:
            try:
                content = yaml.safe_load(f)
            except yaml.YAMLError as e:
                logging.error(f"Error parsing YAML in file {file_path}: {e}")
                return

        for rule in self.rules:
            if rule.match_file(file_path):
                logging.error(f"Rule {rule.id}: {rule.shortdesc} triggered in {file_path}")


import re
from lightspeed_lint.rules.rule_base import RuleBase

class NoHardcodedIPs(RuleBase):
    id = 'LIGHTSPEED001'
    shortdesc = 'No hardcoded IP addresses'
    description = 'Detects hardcoded IP addresses in YAML files'
    tags = ['best practices', 'security']

    ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

    def match_file(self, file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            if self.ip_pattern.search(content):
                return True
        return False

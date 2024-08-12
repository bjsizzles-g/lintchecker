
class RuleBase:
    id = 'BASE'
    shortdesc = 'Base Rule'
    description = 'Base class for all lint rules'
    tags = []

    def match_file(self, file_path):
        raise NotImplementedError("Subclasses must implement match_file() method")

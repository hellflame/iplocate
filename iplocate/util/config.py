import json


class Config:
    def __init__(self, path):
        self.config_path = path
        self.config = {}

    def save(self):
        with open(self.config_path, 'w') as handle:
            handle.write(json.dumps(self.config, indent=2))

    def load(self):
        with open(self.config_path) as handle:
            self.config = json.loads(handle.read())
        return self.config






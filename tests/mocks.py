from get_cli.storage import FileStorage


class FileStorageMock(FileStorage):
    def __init__(self, data: dict):
        self.data = data

    def update(self, key_values: dict):
        self.data.update(key_values)

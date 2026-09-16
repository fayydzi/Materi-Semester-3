import hashlib
import json
import datetime


class Block:

    def __init__(
        self, index: int, data: dict, previous_hash: str = ""
    ):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(
            {
                "index": self.index,
                "timestamp": self.timestamp,
                "data": self.data,
                "previous_hash": self.previous_hash,
            },
            sort_keys=True,
        ).encode()
        return hashlib.sha256(block_string).hexdigest()
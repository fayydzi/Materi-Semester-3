from block import Block


class Blockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(
            index=0,
            data={"message": "Genesis Block Hak Cipta & Royalty Musik"},
            previous_hash="0",
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data: dict):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=latest_block.hash,
        )
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
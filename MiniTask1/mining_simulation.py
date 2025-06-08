# ==============================
# File: mining_simulation.py
# ==============================

import hashlib
import time

#Structure of a Block
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index                        # Position of the block in the chain
        self.timestamp = time.time()              # Time of creation
        self.data = data                          # Block content (e.g., transaction info)
        self.previous_hash = previous_hash        # Hash of the previous block in the chain
        self.nonce = 0                            # Number that will be adjusted to mine a valid hash
        self.hash = self.compute_hash()           # Hash of the current block

    def compute_hash(self):
        # Concatenate all the block's values into a single string and return its SHA-256 hash
        block_contents = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Adjust the nonce until the hash starts with a certain number of zeros,
        representing the mining difficulty level.
        """
        prefix = "0" * difficulty
        start_time = time.time()
        print(f"⛏️ Starting mining process with difficulty level {difficulty}...")

        # Keep incrementing nonce until the hash meets the required difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()

        end_time = time.time()
        print(f"\n✅ Block successfully mined!")
        print(f"🔢 Nonce value found: {self.nonce}")
        print(f"🕒 Mining took: {end_time - start_time:.2f} seconds")
        print(f"🔗 Valid hash: {self.hash}")

# Set the mining difficulty (increase this number for more computational effort)
difficulty = 5  # You can try 6 or more, but it will take longer to mine

# Create a new block and attempt to mine it
new_block = Block(1, "Mining with higher Proof-of-Work", "0")
new_block.mine_block(difficulty)

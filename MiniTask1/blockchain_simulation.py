# ===============================
# File: blockchain_simulation.py
# ===============================


import hashlib
import time

#Structure of a Block
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index                    # Position of the block in the chain
        self.timestamp = timestamp            # Time when the block is created
        self.data = data                      # The actual data (e.g:- transactions)
        self.previous_hash = previous_hash    # Hash of the previous block
        self.nonce = 0                        # Number used for mining
        self.hash = self.compute_hash()       # Calculate the hash of this block

    def compute_hash(self):
        # Concatenate all block fields and return a SHA-256 hash
        block_contents = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_contents.encode()).hexdigest()

# Create the first block (Genesis Block)
genesis_block = Block(0, time.time(), "Genesis Block", "0")
blockchain = [genesis_block]

# Add two more blocks, each referring to the previous block's hash
second_block = Block(1, time.time(), "Block 1 Data", blockchain[-1].hash)
blockchain.append(second_block)

third_block = Block(2, time.time(), "Block 2 Data", blockchain[-1].hash)
blockchain.append(third_block)

# Show the current blockchain
print("===== Blockchain Before Tampering =====")
for block in blockchain:
    print(f"Block {block.index} | Hash: {block.hash} | Previous Hash: {block.previous_hash}")

# Simulate tampering with Block 1's data
print("\n===== Tampering with Block 1 =====")
blockchain[1].data = "Tampered Data"                  # Change the data
blockchain[1].hash = blockchain[1].compute_hash()     # Recalculate its hash

# Show the blockchain after tampering
print("\n===== Blockchain After Tampering =====")
for block in blockchain:
    print(f"Block {block.index} | Hash: {block.hash} | Previous Hash: {block.previous_hash}")

# Validate chain integrity
print("\n===== Chain Validation Check =====")
for i in range(1, len(blockchain)):
    if blockchain[i].previous_hash != blockchain[i - 1].hash:
        print(f"❌ Chain broken after Block {i - 1}! Block {i}'s prev_hash does not match Block {i - 1}'s hash!")
        print(f"    Block {i}'s Previous Hash: {blockchain[i].previous_hash}")
        print(f"    But Block {i - 1}'s Hash:  {blockchain[i - 1].hash}")
        break
else:
    print("✅ All blocks are correctly linked. The chain is valid.")

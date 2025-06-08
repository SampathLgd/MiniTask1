# ==============================
# File: consensus_demo.py
# ==============================

import random

print("=== Consensus Mechanism Simulation ===\n")

# --- Proof of Work (PoW) Simulation ---
# Create 3 miners with random computational power (e.g., hash rate)
pow_validators = [
    {"name": "MinerA", "power": random.randint(50, 200)},
    {"name": "MinerB", "power": random.randint(50, 200)},
    {"name": "MinerC", "power": random.randint(50, 200)},
]

# Select the miner with the highest computational power (simulating mining competition)
selected_pow = max(pow_validators, key=lambda v: v["power"])

print("🔧 Proof of Work (PoW) Result:")
print(f"Selected Miner: {selected_pow['name']} with computational power: {selected_pow['power']}")
print("Logic: The miner with the highest computational power wins the right to add the next block.\n")

# --- Proof of Stake (PoS) Simulation ---
# Create 3 stakers with random stake amounts (e.g., coins locked up)
pos_validators = [
    {"name": "StakerA", "stake": random.randint(10, 100)},
    {"name": "StakerB", "stake": random.randint(10, 100)},
    {"name": "StakerC", "stake": random.randint(10, 100)},
]

# Select the staker with the highest stake (more stake means more chance to validate)
selected_pos = max(pos_validators, key=lambda v: v["stake"])

print("💰 Proof of Stake (PoS) Result:")
print(f"Selected Staker: {selected_pos['name']} with stake: {selected_pos['stake']}")
print("Logic: The validator with the largest stake is chosen to create the next block.\n")

# --- Delegated Proof of Stake (DPoS) Simulation ---
# Define 3 delegates; simulate voting from 10 voters
delegates = ["DelA", "DelB", "DelC"]
votes = random.choices(delegates, k=10)

# Count votes per delegate
vote_counts = {delegate: votes.count(delegate) for delegate in delegates}

# Select the delegate with the highest number of votes
selected_dpos = max(vote_counts, key=vote_counts.get)

print("🗳️ Delegated Proof of Stake (DPoS) Result:")
print(f"Votes: {vote_counts}")
print(f"Selected Delegate: {selected_dpos} with {vote_counts[selected_dpos]} votes")
print("Logic: The delegate who receives the most votes from token holders gets to validate the next block.\n")

# --- Summary ---
print("💡 Summary of Consensus Mechanisms:")
print("PoW  → Validator with highest computational power wins.")
print("PoS  → Validator with highest stake wins.")
print("DPoS → Delegate with most votes wins.")

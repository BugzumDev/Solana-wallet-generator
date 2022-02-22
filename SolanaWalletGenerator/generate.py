# Solana Wallet Generator
# Made by: BugzumDev
from solana.publickey import PublicKey
from solana.account import Account
import json

# Generate account and save keys to a variable
new_account = Account()
public_key = str(new_account.public_key())
private_key = str(new_account.keypair())

# Remove unnesesary characters
private_key = private_key.replace("b", "").replace("'", "")

# Save keys to wallet.json
with open("wallet.json", "w") as record:
    record.write("{" + "\n")
    record.write('  "public_key": ' + '"' + str(public_key) + '",' + "\n")
    record.write('  "private_key": ' + '"' + str(private_key) + '"' + "\n")
    record.write("}")

# Main text
print("Solana Wallet Generator")
print("Made by: BugzumDev")

print()

# Display public key and private key
print("Public key: " + str(public_key))
print("Private key: " + str(private_key))

print()

# Information about keys
print("Public key: This is where you can send SOL or other tokens to the wallet.")
print("Private key: This is where you can get funds from the wallet. (DO NOT SHARE!!!)")
print()
print("The keys are also saved inside 'wallet.json'.")

print()

input("Press enter to exit...")
exit()
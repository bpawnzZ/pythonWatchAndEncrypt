from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Use the key to create a Fernet object
cipher_suite = Fernet(key)

# Write the key to a file
with open('ferret.key', 'wb') as key_file:
    key_file.write(key)

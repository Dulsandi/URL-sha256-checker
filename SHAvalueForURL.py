import hashlib

# Input URL from the user
url = input("Enter the URL: ")

# Encode the URL to bytes
encoded_url = url.encode()

# Calculate SHA-256
sha256_hash = hashlib.sha256(encoded_url).hexdigest()

# Print the result
print("SHA-256 Hash:", sha256_hash)

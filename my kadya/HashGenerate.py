# code for generating hash values

import hashlib

# Create a new SHA-1 hash object
h = hashlib.sha3_512()

# Open the file in binary mode
with open('E:\/file_detection\my kadya\media\sampleSubmission.csv', 'rb') as f:
    chunk = 0
    # Read the file in 1024-byte chunks
    while chunk != b'':
        chunk = f.read(1024)
        # Add each chunk of data to the hash object
        h.update(chunk)

# Get the hexadecimal representation of the hash value
hex_hash = h.hexdigest()
print(hex_hash)
print(type(hex_hash))

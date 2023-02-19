# test to check the similarity percent gives just 5% similarity

import hashlib

# Open the first file and read its contents
with open("E:\/file_detection\my kadya\media\sample-img1.png", 'rb') as f1:
    file1_contents = f1.read()

# Open the second file and read its contents
with open("E:\/file_detection\my kadya\media\sample-img1.1.png", 'rb') as f2:
    file2_contents = f2.read()

# Calculate the hash values of the file contents using SHA1
hash1 = hashlib.sha3_256(file1_contents).hexdigest()
hash2 = hashlib.sha3_256(file2_contents).hexdigest()

# Compare the hash values and calculate the similarity percentage
similarity = 0
for i, c in enumerate(hash1):
    if c == hash2[i]:
        similarity += 1

similarity_percentage = similarity / len(hash1) * 100

print("Similarity Percentage: ", similarity_percentage, "%")

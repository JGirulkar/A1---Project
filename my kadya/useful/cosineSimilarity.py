import hashlib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def file_similarity(file1, file2):
    with open(file1, 'rb') as f1:
        hash1 = hashlib.sha3_256(f1.read()).hexdigest()
    with open(file2, 'rb') as f2:
        hash2 = hashlib.sha3_256(f2.read()).hexdigest()

    hash_vector1 = np.array([ord(char) for char in hash1])
    hash_vector2 = np.array([ord(char) for char in hash2])

    cos_sim = cosine_similarity(hash_vector1.reshape(
        1, -1), hash_vector2.reshape(1, -1))
    similarity_percentage = cos_sim[0][0] * 100

    print(
        f"The cosine similarity between the two files is {cos_sim[0][0]:.2f}")
    print(
        f"The similarity percentage between the two files is {similarity_percentage:.2f}%")


file_similarity(
    "E:\/file_detection\my kadya\media\sample-img1.1.png", "E:\/file_detection\my kadya\media\sampleSubmission.csv")

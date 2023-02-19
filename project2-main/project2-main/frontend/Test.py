import hashlib
import difflib

with open("E:\/file_detection\my kadya\media\doc.docx", 'rb') as f1:
    hash1 = hashlib.sha3_256(f1.read()).hexdigest()
with open("E:\/file_detection\my kadya\media\doc-tampered.docx", 'rb') as f2:
    hash2 = hashlib.sha3_256(f2.read()).hexdigest()


def file_similarity(hash1, hash2):
    jaccard = len(set(hash1).intersection(set(hash2))) / \
        len(set(hash1).union(set(hash2)))
    similarity_percentage = jaccard * 100

    matcher1 = difflib.SequenceMatcher(None, hash1, hash2).ratio()
    print(f"sequence matcher score is: {matcher1: .2f}")

    print(f"The Jaccard score between the two files is {jaccard:.2f}")
    print(
        f"The similarity percentage between the two files is {similarity_percentage:.2f}%")


file_similarity(hash1, hash2)

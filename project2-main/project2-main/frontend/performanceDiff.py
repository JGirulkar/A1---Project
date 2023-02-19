import hashlib
import time

sha1 = hashlib.sha1()
sha3 = hashlib.sha3_512()

with open("E:\/file_detection\my kadya\media\doc-tampered.docx", "rb") as f:
    start_time = time.time()
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        sha1.update(chunk)
    print("SHA-1 computation time: ", time.time() - start_time)

    start_time = time.time()
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        sha3.update(chunk)
    print("SHA-3 computation time: ", time.time() - start_time)

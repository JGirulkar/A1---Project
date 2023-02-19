import jaccard_index


def percentSimilar(conn, file_hash):
    with conn.cursor() as cursor:
        cursor.execute("SELECT hash_values FROM file_data")
        data = cursor.fetchall()

    max_match = 0
    max_match_hash = None

    for row in data:
        jaccard = jaccard_index.jaccard_index(file_hash, row[0])
        if jaccard > max_match:
            max_match = jaccard
            max_match_hash = row[0]

    if max_match == 0:
        print("Exact file not found in the database")
    else:
        print(
            f"The closest match is {max_match_hash} with a Jaccard index of {max_match:.2f}")

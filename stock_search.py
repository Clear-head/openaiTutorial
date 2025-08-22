import meilisearch


client = meilisearch.Client("http://localhost:7700", "5lHwGjUFfJaiLdFRYGSm5IlefYBq5UvbyAcmjh1-Qso")


def stock_search(qry):
    return client.index("nasdaq").search(qry)

from search_notes import documents, retrieve_document


def test_kafka():
    res = retrieve_document("Kafka", documents)
    assert res == "Kafka is a platform for event streaming."

def test_redis():
    res = retrieve_document("redis", documents)
    assert res == "Redis is an in-memory data store used for caching."

def test_redis_case_insensitive():
    res = retrieve_document("Redis", documents)
    assert res == "Redis is an in-memory data store used for caching."

def test_fast_api_case_insensitive():
    res = retrieve_document("FASTapi", documents)
    assert res == "FastAPI is a Python framework for APIs."

def test_empty_str():
    res = retrieve_document("", documents)
    assert res is None

def test_related_words_api():
    res = retrieve_document("API", documents)
    assert res == "FastAPI is a Python framework for APIs."

def test_related_words_redis():
    res = retrieve_document("What stores data in memory?", documents)
    assert res == "Redis is an in-memory data store used for caching."


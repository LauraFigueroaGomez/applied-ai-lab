from search_notes import documents, retrieve_document


def test_kafka():
    res = retrieve_document("Kafka", documents)
    assert res == "Kafka is a platform for event streaming."

def test_redis():
    res = retrieve_document("redis", documents)
    assert res == "Redis is an in-memory data store used for caching."

def test_redis_case_sensitive():
    res = retrieve_document("Redis", documents)
    assert res == "Redis is an in-memory data store used for caching."

def test_fast_api_case_sensitive():
    res = retrieve_document("FASTapi", documents)
    assert res == "FastAPI is a Python framework for APIs."

def test_empty_str():
    res = retrieve_document("", documents)
    assert res == None

def test_str_not_found():
    res = retrieve_document("API", documents)
    assert res == None





documents = {
    "FastAPI": "FastAPI is a Python framework for APIs.",
    "Redis": "Redis is an in-memory data store used for caching.",
    "Kafka": "Kafka is a platform for event streaming."
}


def retrieve_document(query: str, documents: dict[str, str]) -> str | None:
    # 1. Normalize the query
    q = query.lower() #ex: 'Redis'

    # 2. Loop through documents.items()
    for title, text in documents.items():
        # 3. Check for a case-insensitive match
        if title.lower() == q:
            # 4. Return the matching text
            return text

    # 5. Return None if nothing matches
    return None

    











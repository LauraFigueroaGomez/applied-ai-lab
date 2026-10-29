
documents = {
    "FastAPI": "FastAPI is a Python framework for APIs.",
    "Redis": "Redis is an in-memory data store used for caching.",
    "Kafka": "Kafka is a platform for event streaming."
}

related_words = {
    "FastAPI": ["api", "endpoint"],
    "Redis": ["cache", "caching", "memory"],
    "Kafka": ["streaming", "events"]
}


def retrieve_document(query:str, documents: dict[str, str]) -> str | None:
    # CONVERT the query to lowercase
    q = query.lower()

    # FOR each document:
    for title, text in documents.items():
        # print(title, text)
        # IF its title appears in the query:
        if title.lower() in q:
            # RETURN that document
            return text
    
    # FOR each group of related words:
    for word, related_word_list in related_words.items():
        for w in related_word_list:
            # print(word, w)
            # IF the query contains a word from that group:
            if w in q:
                # FIND a document associated with that group
                # RETURN that document
                return documents[word]
        
    # IF nothing matches:
    return None



print("Res1:", retrieve_document("FastAPI", documents))
print("Res2:", retrieve_document("Tell me about Redis", documents))
print("Res3:", retrieve_document("What is Kafka?", documents))
print("Res4:", retrieve_document("api", documents))
print("Res5:", retrieve_document("What stores data in memory?", documents))
# print("Res4:", retrieve_document("api", documents))
# print("Res4:", retrieve_document("api", documents))












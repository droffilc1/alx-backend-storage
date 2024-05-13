#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: pymongo collection object
    Returns: Lists of documents
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    docs = mongo_collection.find()
    return docs

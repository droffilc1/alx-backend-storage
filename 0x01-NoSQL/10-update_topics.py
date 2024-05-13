#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics approached in the school
    """
    query = {"name": name}
    updated_data = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, updated_data)

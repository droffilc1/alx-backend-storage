#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic: topic searched
    Returns the list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})

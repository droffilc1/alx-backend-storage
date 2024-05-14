#!/usr/bin/env python3
""" 101-students """


def top_students(mongo_collection):
    """Returns all students sorted by average score
    Args:
      mongo_collection: pymongo collection object
    Returns all students sorted by average score
    """
    student_score = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        }, {"$sort": {"averageScore": -1}}])
    return student_score

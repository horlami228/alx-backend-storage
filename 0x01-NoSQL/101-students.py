#!/usr/bin/env python3

"""Students sorted by average score"""


def top_students(mongo_collection):
    """average score"""

    top_students = mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},

        {"$sort": {"averageScore": -1}}
    ])

    return top_students

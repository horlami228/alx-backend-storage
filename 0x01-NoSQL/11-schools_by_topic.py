#!/usr/bin/env python3

"""find schools"""


def schools_by_topic(mongo_collection, topic):
    """Python function that returns the list of school having a 
    specific topic"""

    school = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(school)

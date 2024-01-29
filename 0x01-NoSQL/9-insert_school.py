#!/usr/bin/env python3

"""insert a new document to the collection"""

def insert_school(mongo_collection, **kwargs):
    """insert into collection"""

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

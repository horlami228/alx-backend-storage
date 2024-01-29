#!/usr/bin/env python3

"""
    This list all documents in a collection
"""

def list_all(mongo_collection):
    """This function returns a list of 
        collection documents
    """
    if mongo_collection.count_documents({}) != 0:
        documents = mongo_collection.find()
        return documents
    else:
        return []
    
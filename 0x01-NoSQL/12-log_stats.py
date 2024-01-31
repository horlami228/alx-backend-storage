#!/usr/bin/env python3

"""Stats about the nginx logs stored"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")

    nginx_collection = client.logs.nginx

    # Get all documents counts

    documents_count = nginx_collection.count_documents({})
    get_count = nginx_collection.count_documents({"method": "GET"})
    post_count = nginx_collection.count_documents({"method": "POST"})
    put_count = nginx_collection.count_documents({"method": "PUT"})
    patch_count = nginx_collection.count_documents({"method": "PATCH"})
    delete_count = nginx_collection.count_documents({"method": "DELETE"})
    status_count = nginx_collection.count_documents({"path": "/status"})

    # print(get_count, get_post, get_put, get_patch, get_delete)
    # print(status)

    print(f"{documents_count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_count}\n\tmethod POST: {post_count}\
          \n\tmethod PUT: {put_count}\n\tmethod PATCH: {patch_count}\
          \n\tmethod DELETE: {delete_count}")
    print(f"{status_count} status check")

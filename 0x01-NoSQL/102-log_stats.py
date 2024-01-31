#!/usr/bin/env python3

"""10 most present ip"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")

    nginx_collection = client.logs.nginx

    """Get all documents counts"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    documents_count = nginx_collection.count_documents({})

    print(f"{documents_count} logs")
    print("Methods:")
    for method in methods:
        print(
            f"\tmethod {method}: {nginx_collection.count_documents({'method': method})}")

    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{status_count} status check")

    top_ips = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f'\t{ip}: {count}')

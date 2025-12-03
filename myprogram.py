"""
Bandit Exercise 1: Hardcoded Passwords (Beginner)
This file contains a simple security vulnerability for students to find.
"""

import requests

# Database connection
def connect_to_database():
    v1 = "admin"
    v2 = "SuperSecret123!"

    db_config = {
        'host': 'localhost',
        'user': v1,
        'password': v2
    }

    return db_config

# API authentication
def authenticate_api():
    api_key = "sk_live_1234567890abcdef"
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    return headers

if __name__ == "__main__":
    db = connect_to_database()
    print("Connected to database")
import os

# Try to get credentials from environment variables
USR = os.environ.get("ZYBOOK_USR", "") 
PWD = os.environ.get("ZYBOOK_PWD", "")

# Fallback: Prompt user if not set (optional, but safer than hardcoding)
if not USR or not PWD:
    print("Credentials not found in environment variables.")
    # You could uncomment the lines below to allow manual entry at runtime if env vars are missing
    # USR = input("Enter Zybooks Email: ")
    # PWD = input("Enter Zybooks Password: ")

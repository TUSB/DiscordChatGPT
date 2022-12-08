import json
import os

# Check if config.json exists
from colorama import Fore

if not os.path.exists("config.json"):
    print(">> config.json is missing. Please create it.")
    print(f"{Fore.RED}>> Exiting...")
    exit(1)

# Read config.json
with open("config.json", "r") as f:
    config = json.load(f)
    # Check if email & password are in config.json
    if "email" not in config or "password" not in config:
        print(">> config.json is missing email or password. Please add them.")
        print(f"{Fore.RED}>> Exiting...")
        exit(1)

    # Get email & password
    email = config["email"]
    password = config["password"]
    token = config["token"]

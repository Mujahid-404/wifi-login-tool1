import requests
import socket
import time
import json
import os

CREDENTIAL_FILE = "wifi_profiles.json"
LOG_FILE = "login_log.txt"

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def load_credentials():
    if os.path.exists(CREDENTIAL_FILE):
        with open(CREDENTIAL_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_credentials(data):
    with open(CREDENTIAL_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def log_event(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{time.ctime()}: {message}\n")

def perform_login(network_name, url):
    credentials = load_credentials()
    if network_name not in credentials:
        print(f"[!] No credentials found for '{network_name}'")
        return False

    data = credentials[network_name]
    try:
        response = requests.post(url, data=data, timeout=5)
        if response.ok:
            print("[+] Login successful!")
            log_event(f"Login success for {network_name}")
            return True
        else:
            print("[-] Login failed.")
            log_event(f"Login failed for {network_name}")
    except Exception as e:
        print(f"[!] Exception during login: {e}")
        log_event(f"Exception for {network_name}: {e}")
    return False

def main():
    while not is_connected():
        print("[*] Not connected. Trying to login...")
        captive_url = "http://neverssl.com"
        try:
            r = requests.get(captive_url, timeout=5, allow_redirects=True)
            if r.url != captive_url:
                # Redirected to login page
                network = input("Enter network name (as saved): ")
                login_url = r.url
                perform_login(network, login_url)
        except Exception as e:
            print(f"[!] Could not detect captive portal: {e}")
        time.sleep(10)

if __name__ == "__main__":
    main()
    #!/usr/bin/env python3
import json
import os

CONFIG_DIR = os.path.expanduser("~/.config/wifi-login-tool")
CREDENTIAL_FILE = os.path.join(CONFIG_DIR, "wifi_profiles.json")
os.makedirs(CONFIG_DIR, exist_ok=True)

def load_profiles():
    if os.path.exists(CREDENTIAL_FILE):
        with open(CREDENTIAL_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_profiles(profiles):
    with open(CREDENTIAL_FILE, 'w') as f:
        json.dump(profiles, f, indent=4)

def add_profile():
    profiles = load_profiles()
    name = input("Enter network name: ")
    username = input("Username: ")
    password = input("Password: ")
    profiles[name] = {"username": username, "password": password}
    save_profiles(profiles)
    print("[+] Profile saved.")

def list_profiles():
    profiles = load_profiles()
    for name in profiles:
        print(f" - {name}")

def delete_profile():
    profiles = load_profiles()
    name = input("Enter network name to delete: ")
    if name in profiles:
        del profiles[name]
        save_profiles(profiles)
        print("[+] Profile deleted.")
    else:
        print("[-] Profile not found.")

if __name__ == "__main__":
    print("1. Add Profile\n2. List Profiles\n3. Delete Profile")
    choice = input("Choice: ")
    if choice == "1":
        add_profile()
    elif choice == "2":
        list_profiles()
    elif choice == "3":
        delete_profile()
        requests
        #!/bin/bash

echo "[*] Installing requirements..."
pkg install python -y
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Starting Smart Auto Login..."
python3 smart_auto_login.py
## 📲 Termux Installation

```bash
pkg update && pkg upgrade
pkg install git python -y
git clone https://github.com/Mdnoyon14/wifi-login-tool
cd wifi-login-tool
bash run.sh
```bash
git add .
git commit -m "Added Termux compatible smart auto login tool"
git push origin main
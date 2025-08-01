import hashlib
import os
import json

def calculate_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

HASHES_FILE = 'hashes.json'

def load_hashes():
    if os.path.exists(HASHES_FILE):
        with open(HASHES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASHES_FILE, 'w') as f:
        json.dump(hashes, f)

print("File Integrity Checker")
mode = input("Choose mode (store/check): ").strip().lower()

if mode == "store":
    files = input("Enter comma-separated file paths to track: ").split(",")
    hashes = load_hashes()
    for file in files:
        file = file.strip()
        if os.path.exists(file):
            hashes[file] = calculate_hash(file)
            print(f"✅ Hash stored for {file}")
        else:
            print(f"❌ File not found: {file}")
    save_hashes(hashes)

elif mode == "check":
    files = input("Enter comma-separated file paths to check: ").split(",")
    hashes = load_hashes()
    for file in files:
        file = file.strip()
        if file in hashes:
            current_hash = calculate_hash(file)
            if current_hash == hashes[file]:
                print(f"✅ No change detected: {file}")
            else:
                print(f"⚠️ File changed: {file}")
        else:
            print(f"⚠️ No stored hash for: {file}")

else:
    print("❌ Invalid mode. Choose 'store' or 'check'.")

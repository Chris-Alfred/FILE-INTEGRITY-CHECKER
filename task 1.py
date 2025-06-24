import hashlib
import os
import json

# File to store hashes
HASH_DB = "file_hashes.json"

def calc_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def save_hash(target_path):
    file_hashes = {}

    if os.path.isfile(target_path):
        relative_path = os.path.relpath(target_path)
        hash_val = calc_hash(target_path)
        if hash_val:
            print(f"Saving hash for: {relative_path} -> {hash_val}")
            file_hashes[relative_path] = hash_val
    else:
        for root, _, files in os.walk(target_path):
            for filename in files:
                full_path = os.path.join(root, filename)
                relative_path = os.path.relpath(full_path)
                hash_val = calc_hash(full_path)
                if hash_val:
                    print(f"Saving hash for: {relative_path} -> {hash_val}")
                    file_hashes[relative_path] = hash_val

    with open(HASH_DB, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print("Initial hashes saved.")

def check_integrity():
    try:
        with open(HASH_DB, "r") as f:
            old_hashes = json.load(f)
    except FileNotFoundError:
        print("No saved hash database found. Please run in 'save' mode first.")
        return

    print("Checking file integrity...")
    print(f"Loaded hashes: {list(old_hashes.keys())}")

    for relative_path, old_hash in old_hashes.items():
        full_path = os.path.join(os.getcwd(), relative_path)
        new_hash = calc_hash(full_path)
        print(f"Checking {relative_path}...")

        if not new_hash:
            print(f"File missing: {relative_path}")
        elif new_hash != old_hash:
            print(f"File changed: {relative_path}")
        else:
            print(f"File OK: {relative_path}")

if __name__ == "_main_":
    import argparse

    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("mode", choices=["save", "check"], help="save: store file hashes, check: verify integrity")
    parser.add_argument("--dir", help="Directory or file to scan (required for save)")

    args = parser.parse_args()

    if args.mode == "save":
        if not args.dir:
            print("Please provide a file or directory with --dir to save hashes.")
        else:
            save_hash(args.dir)
    elif args.mode == "check":
        check_integrity()
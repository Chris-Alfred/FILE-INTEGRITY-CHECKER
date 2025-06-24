# FILE-INTEGRITY-CHECKER

NAME : CHRIS ALFRED

COMPANY : CODTECH

INTERN ID : CT04DN749

DOMAIN : Cyber Security & Ethical Hacking 

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

DESCRIPTION :

This Python script is a basic File Integrity Checker that helps detect unauthorized or unexpected changes in files by calculating and storing SHA-256 hashes. It operates in two modes: "save" and "check". In save mode, the script takes a file or directory path as input and calculates the SHA-256 hash for each file, storing the results in a JSON file (file_hashes.json). These hashes act as digital fingerprints, capturing the file's state at a specific moment. In check mode, the script loads the previously stored hashes and compares them with newly computed hashes of the current files. It reports if any file is missing, altered, or unchanged, helping users verify the integrity of their files over time. The code uses Python’s hashlib for secure hashing, os for file traversal, and json for storing the hash database. This tool is particularly useful for monitoring critical files, detecting tampering, or ensuring backups haven't been corrupted. It must be run with command-line arguments, but note that the entry point currently uses if __name__ == "_main_": which should be corrected to if __name__ == "__main__": for proper functionality.

# OUTPUT :


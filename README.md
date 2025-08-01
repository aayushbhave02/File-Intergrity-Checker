 ## Project Title: File Integrity Checker Using Python ##

# Project Description:

This project implements a File Integrity Checker tool using Python. Its primary purpose is to track changes to important files and detect tampering or corruption, which is crucial in cybersecurity for ensuring data integrity.
The tool uses SHA-256 hashing to create unique digital fingerprints of files. It can store the current state of files and later verify if they’ve been modified, deleted, or remain unchanged. It works in two modes:
Store: Saves the hash values of the selected files.
Check: Compares the current hashes with the saved ones to detect changes.

This project introduces students to hashing algorithms, file handling, and integrity verification, which are essential topics in cybersecurity.

# Key Objectives:
- Detect any unauthorized or unexpected changes to critical files.
- Maintain a secure list of known-good file hashes.
- Alert the user when discrepancies are found.
- Provide a simple way to "store" and "check" file integrity.

# Features:

- Supports secure hash algorithm (SHA-256).
- “Store” mode: Generates and stores the file's hash in a local record file (e.g., notes.txt).
- “Check” mode: Compares the current file hash to the stored hash to detect changes.
- Clean and user-friendly command-line interface.
- Supports multiple file entries.
- Error handling for missing files, unsupported modes, or mismatches
  
# Skills Demonstrated:

- Python scripting and automation
- Use of hashing libraries (hashlib)
- file read/write operations
- Dictionary handling and string parsing
- Command-line interaction and validation

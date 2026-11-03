# file-integrity-checker
File integrity monitoring tool, built in Python to verify data integrity and detect changes.

A lightweight Python tool designed to verify data.

## Context & Purpose
In cybersecutiry, Integrity is one of the foundational pillars of the CIA Triad (Confidentiality, Integrity, Availabality).

This tool performs basic File Integrity Monitoring (FIM). By calculating a unique SHA-256 cryptographic hash of a file, it creates a digital fingerprint. Any unauthorized modification - even altering a singles character or byte - drastically changes the output hash (avalanche effect), alerting administrators to potential tampering. 

## Features 

- **SHA-256 Hashing:** Uses Python-s native `hashlib` library to generate secure fingerprints.
- **Memory Efficient:** Reads files in chunks (4096 bytes) to handle larger files without consuming excessive RAM.
- **Zero External Dependencies:** Runs natively with any standard Python 3 installation.

- ## Usage

- 1. Clone this repository:
  ```bash
     git clone [https://github.com/SEU-USUARIO/file-integrity-checker.git](https://github.com/SEU-USUARIO/file-integrity-checker.git)
     cd file-integrity-checker

- 2. Run the integrity checker.
   ```bash
   python checker.py
  

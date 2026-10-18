# 🔐 Python Hash Identifier & Dictionary Auditor

A lightweight Python cryptography tool designed for CTFs and authorized security labs (such as TryHackMe's *Crack the Hash*). It automatically identifies common hash formats (`MD5`, `SHA-1`, `SHA-256`) and performs dictionary auditing using wordlists like `rockyou.txt`.

## 🚀 Features
- **Auto Hash Detection:** Identifies MD5 (32-char), SHA-1 (40-char), and SHA-256 (64-char) hashes automatically.
- **Fast Dictionary Auditing:** Compares target hashes against large wordlists using Python's built-in `hashlib`.
- **Encoding Resilient:** Uses `latin-1` encoding to smoothly read complex wordlists like `rockyou.txt` without crashing.

## 🛠️ Usage
Run the script in your terminal:
```bash
python3 hash_tool.py

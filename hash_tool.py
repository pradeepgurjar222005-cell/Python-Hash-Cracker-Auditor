import hashlib
import re

print("=" * 60)
print("   🛡️ PYTHON HASH IDENTIFIER & PASSWORD SECURITY AUDITOR 🛡️")
print("=" * 60)

def identify_hash(hash_str):
    hash_str = hash_str.strip()
    if hash_str.startswith(("$2a$", "$2b$", "$2y$")):
        return "bcrypt (Strong - Recommended for password storage)"
    elif hash_str.startswith("$argon2"):
        return "Argon2 (Very Strong - Modern Standard)"
    elif len(hash_str) == 32 and re.fullmatch(r"[0-9a-fA-F]{32}", hash_str):
        return "MD5 / NTLM (Weak - Vulnerable to fast GPU auditing)"
    elif len(hash_str) == 40 and re.fullmatch(r"[0-9a-fA-F]{40}", hash_str):
        return "SHA-1 (Weak - Deprecated for cryptographic security)"
    elif len(hash_str) == 64 and re.fullmatch(r"[0-9a-fA-F]{64}", hash_str):
        return "SHA-256 (Fast Hash - Requires salting/key stretching for passwords)"
    else:
        return "Unknown or Custom Hash Format"

def check_password_policy(password):
    score = 0
    feedback = []
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Increase length to at least 12 characters.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include numbers.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters.")
    return score, feedback

choice = input("Choose Mode: [1] Identify Hash Security  [2] Audit Password Strength: ").strip()

if choice == "1":
    sample_hash = input("Enter hash string to analyze: ")
    print(f"\n[*] Analysis Result: {identify_hash(sample_hash)}")
elif choice == "2":
    pwd = input("Enter a sample password to test policy compliance: ")
    score, tips = check_password_policy(pwd)
    print(f"\n[*] Security Score: {score}/4")
    print(f"[*] SHA-256 Preview: {hashlib.sha256(pwd.encode()).hexdigest()}")
    if tips:
        print("[!] Recommendations:")
        for tip in tips:
            print(f"    - {tip}")
    else:
        print("[+] Password meets strong security standards!")

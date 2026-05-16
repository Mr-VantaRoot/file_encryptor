
import os
import argparse
import hashlib
from base64 import urlsafe_b64encode, urlsafe_b64decode

def derive_key(password):
    return hashlib.sha256(password.encode()).digest()

def xor_bytes(data, key):
    result = bytearray()
    for i, b in enumerate(data):
        result.append(b ^ key[i % len(key)])
    return bytes(result)

def encrypt_file(filepath, password):
    key = derive_key(password)
    with open(filepath, "rb") as f:
        data = f.read()
    if not data:
        print("[ERROR] File is empty.")
        return
    encrypted = xor_bytes(data, key)
    encoded = urlsafe_b64encode(encrypted)
    out_path = filepath + ".enc"
    with open(out_path, "wb") as f:
        f.write(encoded)
    print(f"[✅] Encrypted → {out_path} ({len(encoded)} bytes)")

def decrypt_file(filepath, password):
    if not filepath.endswith(".enc"):
        print("[ERROR] File must have .enc extension.")
        return
    key = derive_key(password)
    with open(filepath, "rb") as f:
        encoded = f.read()
    if not encoded:
        print("[ERROR] Encrypted file is empty.")
        return
    try:
        encrypted = urlsafe_b64decode(encoded)
    except Exception:
        print("[ERROR] Invalid encrypted file format.")
        return
    decrypted = xor_bytes(encrypted, key)
    out_path = filepath.replace(".enc", ".decrypted")
    with open(out_path, "wb") as f:
        f.write(decrypted)
    print(f"[✅] Decrypted → {out_path} ({len(decrypted)} bytes)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Encryption & Decryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="encrypt or decrypt")
    parser.add_argument("file", help="Path to the file")
    parser.add_argument("-p", "--password", required=True, help="Password")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[ERROR] File not found: {args.file}")
    elif args.action == "encrypt":
        encrypt_file(args.file, args.password)
    elif args.action == "decrypt":
        decrypt_file(args.file, args.password)

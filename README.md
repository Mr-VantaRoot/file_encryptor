# 🔒 Python File Encryption & Decryption Tool

A simple command-line tool that encrypts and decrypts any file using a password you choose. Built with pure Python — no external libraries needed.

---

## Features

- **Encrypt any file** — works on `.txt`, `.pdf`, `.jpg`, `.csv`, and more
- **Decrypt back to original** — get your file back with the same password
- **Password-based key** — uses SHA-256 to derive a secure key from your password
- **XOR encryption** — fast and lightweight symmetric cipher
- **No external libraries** — pure Python standard library only

---

## Requirements

- Python 3.6+
- No pip installs needed

---

## How to Use — Step by Step

### Step 1 — Create a file you want to encrypt

Make a text file with anything inside it:

```bash
echo "This is my secret message" > secret.txt
```

Or just create `secret.txt` manually and type something in it. Save it.

---

### Step 2 — Encrypt the file

Run this command, replacing `mypassword` with any password you want:

```bash
python file_encryptor.py encrypt secret.txt -p mypassword
```

**What happens:**
- A new file called `secret.txt.enc` is created in the same folder
- This is your encrypted file — it looks like random garbage if you open it
- Your original `secret.txt` is NOT deleted — you can delete it manually if you want

**Output you will see:**
```
[✅] Encrypted → secret.txt.enc (44 bytes)
```

---

### Step 3 — Decrypt the file

To get your original file back, run:

```bash
python file_encryptor.py decrypt secret.txt.enc -p mypassword
```

> ⚠️ The password MUST be exactly the same as the one you used to encrypt. If even one character is different, the output will be unreadable garbage.

**What happens:**
- A new file called `secret.txt.decrypted` is created
- Open it and you will see your original content back

**Output you will see:**
```
[✅] Decrypted → secret.txt.decrypted (26 bytes)
```

---

## Full Example

```bash
# 1. Create a file
echo "Hello, this is secret!" > secret.txt

# 2. Encrypt it
python file_encryptor.py encrypt secret.txt -p mypassword123
# → creates secret.txt.enc

# 3. Decrypt it
python file_encryptor.py decrypt secret.txt.enc -p mypassword123
# → creates secret.txt.decrypted

# 4. Check the content
cat secret.txt.decrypted
# Output: Hello, this is secret!
```

---

## Common Mistakes

| Mistake | What happens | Fix |
|--------|--------------|-----|
| Different password on decrypt | Output is unreadable garbage | Use the exact same password |
| Trying to decrypt a non-.enc file | Error message | Only decrypt files ending in `.enc` |
| Forgetting your password | Cannot recover the file | There is no way to recover without the password |
| Opening .enc file in a text editor | Looks like random characters | That is normal — it is encrypted |

---

## How It Works

1. **Key generation** — your password is hashed with SHA-256 to create a 256-bit key
2. **XOR encryption** — every byte in the file is XOR'd with the key, making it unreadable
3. **Base64 encoding** — the encrypted bytes are encoded to Base64 for safe file storage
4. **Decryption** — the same process in reverse: Base64 decode → XOR with same key → original file

---

## Important Notes

- The password is **never stored anywhere** — you must remember it
- The tool works on **any file type**, not just text files
- Encrypted files have the `.enc` extension
- Decrypted files have the `.decrypted` extension

---

## Disclaimer

This tool is for **educational purposes**. Do not use it to encrypt files you cannot afford to lose without keeping a backup and remembering your password.

---


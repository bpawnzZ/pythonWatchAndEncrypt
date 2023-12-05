#**README: Monitor Folder and Automate encryption of any New files to to specified location**

This repository contains scripts for encrypting and decrypting files using the Fernet symmetric encryption algorithm. The scripts utilize the watchdog library to monitor specified directories for new file creations, automatically encrypting or decrypting new files as they are added.

**Encrypting Files**

The `encrypt.py` script encrypts files in a specified directory and saves the encrypted files to an output directory. It utilizes the Fernet symmetric encryption algorithm to secure the files, ensuring that only authorized users with the encryption key can decrypt them.

**Usage:**

```bash
python encrypt.py -k KEY_PATH -d WATCH_PATH -o OUTPUT_PATH [-r]
```

**Flags:**

* `-k` or `--key_path`: Path to the encryption key file.
* `-d` or `--watch_path`: Path to the directory to watch for new files.
* `-o` or `--output_path`: Path to the output directory for encrypted files.
* `-r` or `--delete_unencrypted`: Optional flag to delete the original unencrypted file after encryption.

**Decrypting Files**

The `decrypt.py` script decrypts encrypted files in a specified directory and saves the decrypted files to an output directory. It utilizes the same Fernet symmetric encryption algorithm used for encryption, ensuring that only authorized users with the decryption key can decrypt the files.

**Usage:**

```bash
python decrypt.py -k KEY_PATH -d WATCH_PATH -o OUTPUT_PATH
```

**Flags:**

* `-k` or `--key_path`: Path to the decryption key file.
* `-d` or `--watch_path`: Path to the directory to watch for new encrypted files.
* `-o` or `--output_path`: Path to the output directory for decrypted files.

**Generating Encryption Keys**

The `genKey.py` script generates a new encryption key for use in both encryption and decryption processes. The generated key is saved to a file named `ferret.key`.

**Usage:**

```bash
python genKey.py
```

**Security Considerations**

It is crucial to secure the encryption key (chAndEncrypt

# decrypt.py
import os
import time
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DecryptHandler(FileSystemEventHandler):
    def __init__(self, key_path, watch_path, output_path):
        self.key_path = key_path
        self.watch_path = watch_path
        self.output_path = output_path

    def on_created(self, event):
        if not event.is_directory:
            with open(self.key_path, 'rb') as key_file:
                key = key_file.read()
            fernet = Fernet(key)

            with open(event.src_path, 'rb') as file:
                encrypted = file.read()

            decrypted = fernet.decrypt(encrypted)

            output_file_path = os.path.join(self.output_path, os.path.basename(event.src_path)[4:])
            with open(output_file_path, 'wb') as output_file:
                output_file.write(decrypted)

def main(key_path, watch_path, output_path):
    event_handler = DecryptHandler(key_path, watch_path, output_path)
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Decrypt files in a directory.')
    parser.add_argument('-k', '--key_path', required=True, help='Path to the decryption key.')
    parser.add_argument('-d', '--watch_path', required=True, help='Path to the directory to watch.')
    parser.add_argument('-o', '--output_path', required=True, help='Path to the output directory.')
    args = parser.parse_args()

    main(args.key_path, args.watch_path, args.output_path)

import os
import time
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class EncryptHandler(FileSystemEventHandler):
    def __init__(self, key_path, watch_path, output_path, delete_unencrypted):
        self.key_path = key_path
        self.watch_path = watch_path
        self.output_path = output_path
        self.delete_unencrypted = delete_unencrypted

    def on_created(self, event):
        if not event.is_directory:
            with open(self.key_path, 'rb') as key_file:
                key = key_file.read()
            fernet = Fernet(key)

            with open(event.src_path, 'rb') as file:
                original = file.read()

            encrypted = fernet.encrypt(original)

            output_file_path = os.path.join(self.output_path, 'enc.' + os.path.basename(event.src_path))
            with open(output_file_path, 'wb') as output_file:
                output_file.write(encrypted)

            if self.delete_unencrypted:
                os.remove(event.src_path)

def main(key_path, watch_path, output_path, delete_unencrypted):
    event_handler = EncryptHandler(key_path, watch_path, output_path, delete_unencrypted)
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
    parser = argparse.ArgumentParser(description='Encrypt files in a directory.')
    parser.add_argument('-k', '--key_path', required=True, help='Path to the encryption key.')
    parser.add_argument('-d', '--watch_path', required=True, help='Path to the directory to watch.')
    parser.add_argument('-o', '--output_path', required=True, help='Path to the output directory.')
    parser.add_argument('-r', '--delete_unencrypted', action='store_true', help='Delete the original unencrypted file.')
    args = parser.parse_args()

    main(args.key_path, args.watch_path, args.output_path, args.delete_unencrypted)

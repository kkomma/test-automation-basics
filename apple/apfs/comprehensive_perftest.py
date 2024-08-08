import time
from cryptography.fernet import Fernet

from apple.apfs.apfs_ops import APFS, APFSFile
from apple.apfs.copy_files import clone_file
from apple.apfs.space_sharing import APFSContainer

# Combined performance test for all features
container = APFSContainer(total_space=10**8)  # 100MB container
volume1 = container.create_volume()
volume2 = container.create_volume()

# File operations
start_time = time.time()
file1 = APFSFile("file1.txt", "A" * 10**6, Fernet.generate_key())  # 1MB file
file2 = APFSFile("file2.txt", "B" * 2 * 10**6, Fernet.generate_key())  # 2MB file
volume1.add_file(file1)
volume2.add_file(file2)
end_time = time.time()
print(f"Time taken for file operations: {end_time - start_time} seconds")

# Cloning
start_time = time.time()
cloned_file = clone_file(file1)
end_time = time.time()
print(f"Time taken to clone file: {end_time - start_time} seconds")

# Snapshot creation
start_time = time.time()
apfs = APFS()
apfs.add_file("file1.txt", "A" * 10**6)
apfs.create_snapshot()
end_time = time.time()
print(f"Time taken to create snapshot: {end_time - start_time} seconds")

# Snapshot restoration
apfs.add_file("file2.txt", "B" * 10**6)
start_time = time.time()
apfs.restore_snapshot(0)
end_time = time.time()
print(f"Time taken to restore snapshot: {end_time - start_time} seconds")

# Encryption/Decryption
key = Fernet.generate_key()
data = "A" * 10**6

start_time = time.time()
file = APFSFile("encrypted_file.txt", data, key)
end_time = time.time()
print(f"Time taken to encrypt data: {end_time - start_time} seconds")

start_time = time.time()
decrypted_data = file.decrypt_data()
end_time = time.time()
print(f"Time taken to decrypt data: {end_time - start_time} seconds")

# Space sharing check
print(f"Total Used Space: {container.used_space} bytes out of {container.total_space} bytes")

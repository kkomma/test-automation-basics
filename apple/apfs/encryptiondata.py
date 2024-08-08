from cryptography.fernet import Fernet
import time

class APFSFile:
    def __init__(self, name, data, key):
        self.name = name
        self.key = key
        self.fernet = Fernet(key)
        self.data = self.fernet.encrypt(data.encode())

    def decrypt_data(self):
        return self.fernet.decrypt(self.data).decode()

# Performance test for encryption/decryption
key = Fernet.generate_key()
data = "A" * 10**6  # 1MB data

# Encryption
start_time = time.time()
file = APFSFile("encrypted_file.txt", data, key)
end_time = time.time()
print(f"Time taken to encrypt data: {end_time - start_time} seconds")

# Decryption
start_time = time.time()
decrypted_data = file.decrypt_data()
end_time = time.time()
print(f"Time taken to decrypt data: {end_time - start_time} seconds")
print("Decryption successful:", decrypted_data == data)

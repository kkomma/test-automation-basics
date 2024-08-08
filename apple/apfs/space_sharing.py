from cryptography.fernet import Fernet
from apple.apfs.copy_files import APFSFile

class APFSContainer:
    def __init__(self, total_space):
        self.total_space = total_space
        self.used_space = 0
        self.volumes = []

    def create_volume(self):
        volume = APFSVolume(self)
        self.volumes.append(volume)
        return volume

class APFSVolume:
    def __init__(self, container):
        self.container = container
        self.files = []

    def add_file(self, file):
        self.files.append(file)
        self.container.used_space += len(file.data)

# Test case
container = APFSContainer(total_space=1000)
volume1 = container.create_volume()
volume2 = container.create_volume()

file1 = APFSFile("file1.txt", "Data for file 1", Fernet.generate_key())
file2 = APFSFile("file2.txt", "Data for file 2", Fernet.generate_key())

volume1.add_file(file1)
volume2.add_file(file2)

print("Total Used Space:", container.used_space)
print("Volume 1 Files:", [file.name for file in volume1.files])
print("Volume 2 Files:", [file.name for file in volume2.files])

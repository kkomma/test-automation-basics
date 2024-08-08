import copy

class APFS:
    def __init__(self):
        self.files = {}
        self.snapshots = []

    def add_file(self, name, data):
        self.files[name] = data

    def create_snapshot(self):
        self.snapshots.append(copy.deepcopy(self.files))

    def restore_snapshot(self, index):
        self.files = copy.deepcopy(self.snapshots[index])

# Test case
apfs = APFS()
apfs.add_file("file1.txt", "Data for file 1")
apfs.create_snapshot()
apfs.add_file("file2.txt", "Data for file 2")
print("Current Files:", apfs.files)
apfs.restore_snapshot(0)
print("Files after restoring snapshot:", apfs.files)

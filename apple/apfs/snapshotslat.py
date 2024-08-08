class APFSFileSystem:
    def __init__(self):
        self.data_blocks = {}
        self.snapshots = []
        self.current_state = {}

    def write_file(self, filename, data):
        self.data_blocks[filename] = data
        self.current_state[filename] = data

    def create_snapshot(self):
        snapshot = self.current_state.copy()
        self.snapshots.append(snapshot)

    def modify_file(self, filename, new_data):
        if filename in self.data_blocks:
            self.data_blocks[filename] = new_data
            self.current_state[filename] = new_data

    def delete_snapshot(self, index):
        del self.snapshots[index]

# Example usage
fs = APFSFileSystem()
fs.write_file("file1.txt", "This is some initial data.")
fs.create_snapshot()  # Snapshot 1
fs.modify_file("file1.txt", "This is some modified data.")
fs.create_snapshot()  # Snapshot 2

print("Current State:", fs.current_state)
print("Snapshots:", fs.snapshots)

import os
import tempfile

def test_file_system():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "test_file")
        with open(file_path, "w") as f:
            f.write("Test content")
        assert os.path.exists(file_path)
        assert os.path.getsize(file_path) > 0

if __name__ == "__main__":
    test_file_system()
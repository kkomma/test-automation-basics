import subprocess

def test_macos_kernel():
    try:
        # Run a command to check the macOS kernel version
        result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            kernel_version = result.stdout.strip()
            print(f"macOS kernel version: {kernel_version}")
        else:
            print("Failed to retrieve macOS kernel version.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the test
test_macos_kernel()
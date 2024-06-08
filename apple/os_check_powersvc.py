import subprocess

# Check if the service is running
# cmd = "launchctl list | grep com.apple.PerfPowerServices"
# output = subprocess.check_output(cmd, shell=True)

# if "com.apple.PerfPowerServices" in output.decode("utf-8"):
#     print("Service is running")
# else:
#     print("Service is not running")

# Check power settings
cmd = "pmset -g"
output = subprocess.check_output(cmd, shell=True)

print(output.decode("utf-8"))
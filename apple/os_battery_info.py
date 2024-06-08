import subprocess
import plistlib
import json

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, check=True, capture_output=True)
    return result.stdout.decode('utf-8')
    # return plistlib.load(result.stdout.decode('utf-8'))

def get_battery_info():
    """Get battery information from the connected iOS device."""
    # Get the device UDID
    udid_command = "idevice_id -l"
    udid = run_command(udid_command).strip()
    print('uuid::', udid)
    # Get battery information using ideviceinfo
    info_command = f"ideviceinfo -u {udid} -q com.apple.mobile.battery"
    battery_info_plist = run_command(info_command)
    print('battery_info_plist::', battery_info_plist)
    key_value_pairs = battery_info_plist.split("\n")
    print("key_value_pairs",key_value_pairs)
    # Create a dictionary to hold the parsed data
    data_dict = {}
    # Parse each key-value pair and add it to the dictionary
    for pair in key_value_pairs[:-1]:
        key, value = pair.split(": ")
        data_dict[key] = value

    return data_dict

def main():
    try:
        print("Battery Information11:")
        battery_info = get_battery_info()
        print("Battery Information:")
        for key, value in battery_info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

import psutil
import os,sys

def get_cpu_usage():
  cpu_times = psutil.cpu_times()
  cpu_usage = cpu_times.user + cpu_times.system
  return cpu_usage

# Example Usage
cpu_usage = get_cpu_usage()
print(f"CPU Usage: {cpu_usage}%")


def get_memory_usage():
  mem = psutil.virtual_memory()
  return mem.used / mem.total * 100

# Example Usage
memory_usage = get_memory_usage()
print(f"Memory Usage: {memory_usage:.2f}%")

def get_disk_usage(path):
  disk_usage = psutil.disk_usage(path)
  return disk_usage.used / disk_usage.total * 100

# Example Usage
disk_usage = get_disk_usage("/")
print(f"Disk Usage (/): {disk_usage:.2f}%")

def get_uptime():
  uptime = psutil.boot_time()
  return uptime

# Example Usage
uptime_seconds = get_uptime()
uptime_days = int(uptime_seconds / (60 * 60 * 24))
print(f"Uptime: {uptime_days} days")

print('sensor battery::', psutil.sensors_battery())

print("this os::",sys.platform.startswith("darwin"))
print('pids::', psutil.pids()[-5:])
print('pids::', psutil.Process(psutil.pids()[-1]))

POSIX = os.name == "posix"
WINDOWS = os.name == "nt"
LINUX = sys.platform.startswith("linux")
MACOS = sys.platform.startswith("darwin")
OSX = MACOS  # deprecated alias
FREEBSD = sys.platform.startswith(("freebsd", "midnightbsd"))
OPENBSD = sys.platform.startswith("openbsd")
NETBSD = sys.platform.startswith("netbsd")
BSD = FREEBSD or OPENBSD or NETBSD
SUNOS = sys.platform.startswith(("sunos", "solaris"))
AIX = sys.platform.startswith("aix")


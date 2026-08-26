import os 

def get_system_info():
    hostname = os.uname().nodename
    os_name = os.uname().sysname
    os_version = os.uname().release

    with open("/proc/cpuinfo", "r") as f:
        cpu_info = f.read()
        model_name = "Unknown"
        for line in cpu_info.splitlines():
            if line.startswith("model name"):
                model_name = line.split(":")[1].strip()
                break

    return {
        "hostname": hostname,
        "os_name": os_name,
        "os_version": os_version,
        "cpu_model": model_name
    }

if __name__ == "__main__":
    system_info = get_system_info()
    print(f"Hostname: {system_info['hostname']}")
    print(f"OS Name: {system_info['os_name']}")
    print(f"OS Version: {system_info['os_version']}")
    print(f"CPU Model: {system_info['cpu_model']}")
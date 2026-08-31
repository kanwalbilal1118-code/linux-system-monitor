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
    with open("/proc/meminfo", "r") as f:
        mem_info = f.read()
        total_memory = "Unknown"
        memory_available = "Unknown"
        for line in mem_info.splitlines():
            if line.startswith("MemTotal"):
                total_memory = float(line.split(":")[1].strip().split()[0])
                total_memory = total_memory / 1024 / 1024  # Convert to GB
            elif line.startswith("MemAvailable"):
                memory_available = float(line.split(":")[1].strip().split()[0])
                memory_available = memory_available / 1024 / 1024  # Convert to GB
               
    return {
        "hostname": hostname,
        "os_name": os_name,
        "os_version": os_version,
        "cpu_model": model_name,
        "total_memory": total_memory,
        "memory_available": memory_available
    }

if __name__ == "__main__":
    system_info = get_system_info()
    print(f"Hostname: {system_info['hostname']}")
    print(f"OS Name: {system_info['os_name']}")
    print(f"OS Version: {system_info['os_version']}")
    print(f"CPU Model: {system_info['cpu_model']}")
    print(f"Total Memory: {system_info['total_memory']:.2f} GB")
    print(f"Available Memory: {system_info['memory_available']:.2f} GB")
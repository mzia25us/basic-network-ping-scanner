import os
import platform
import socket
import subprocess
import time


def is_valid_network_prefix(prefix):
    parts = prefix.split(".")
    if len(parts) != 3:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        value = int(part)
        if value < 0 or value > 255:
            return False

    return True


def is_valid_host_range(start, end):
    return 1 <= start <= 254 and 1 <= end <= 254 and start <= end


def ping_host(ip_address):
    system_name = platform.system().lower()

    if system_name == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip_address]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip_address]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False


def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return "Unknown"
    except Exception:
        return "Unknown"


def save_results(results, filename="scan_results.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Network Ping Scanner Results\n")
        file.write("=" * 35 + "\n\n")

        for result in results:
            file.write(f"IP Address: {result['ip']}\n")
            file.write(f"Hostname:   {result['hostname']}\n")
            file.write("-" * 35 + "\n")

    print(f"\nResults saved to {filename}")


def main():
    print("=== Network Ping Scanner ===\n")

    network_prefix = input("Enter network prefix (example: 192.168.1): ").strip()

    if not is_valid_network_prefix(network_prefix):
        print("Invalid network prefix. Please use format like 192.168.1")
        return

    try:
        start_host = int(input("Enter start host number (1-254): ").strip())
        end_host = int(input("Enter end host number (1-254): ").strip())
    except ValueError:
        print("Host range must be numbers.")
        return

    if not is_valid_host_range(start_host, end_host):
        print("Invalid host range.")
        return

    print("\nScanning network...\n")
    start_time = time.time()

    active_hosts = []
    total_scanned = 0

    for host in range(start_host, end_host + 1):
        ip_address = f"{network_prefix}.{host}"
        total_scanned += 1

        print(f"Checking {ip_address}...", end=" ")

        if ping_host(ip_address):
            hostname = get_hostname(ip_address)
            print("ACTIVE")
            active_hosts.append({
                "ip": ip_address,
                "hostname": hostname
            })
        else:
            print("No response")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n=== Scan Summary ===")
    print(f"Hosts scanned: {total_scanned}")
    print(f"Active hosts:  {len(active_hosts)}")
    print(f"Time taken:    {elapsed_time:.2f} seconds")

    if active_hosts:
        print("\n=== Active Devices Found ===")
        for host in active_hosts:
            print(f"{host['ip']} | Hostname: {host['hostname']}")
        save_results(active_hosts)
    else:
        print("\nNo active devices found.")


if __name__ == "__main__":
    main()
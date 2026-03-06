# Network Ping Scanner (Python)

A simple Python network utility that scans a range of IP addresses on a local network and identifies which devices are active using ICMP ping requests.

This project was created as part of personal learning while exploring networking concepts and automation with Python.

---

## Overview

This tool scans a user-defined IP range and reports which hosts respond to a ping request. It can also attempt to resolve hostnames for active devices and generate a summary of the scan.

The project demonstrates how Python can interact with system networking tools to perform basic network discovery tasks.

---

## Features

* Scan a custom IP range on a local network
* Detect active devices using ICMP ping
* Attempt hostname resolution using reverse DNS lookup
* Cross-platform support for Windows, Linux, and macOS
* Displays scan progress
* Summary statistics after scanning
* Saves results to a text file

---

## Technologies Used

* Python
* ICMP (Ping)
* DNS hostname resolution
* Basic network scanning concepts

---

## How to Run

1. Clone the repository

```
git clone https://github.com/mzia25us/network-ping-scanner.git
```

2. Navigate to the project folder

```
cd network-ping-scanner
```

3. Run the script

```
python ping_scanner.py
```

4. Enter the network prefix and host range when prompted.

Example:

```
Network prefix: 192.168.0
Start host: 1
End host: 50
```

---

## What This Project Demonstrates

* Network discovery using ICMP ping
* Automating system commands with Python
* Basic input validation
* Handling network responses and errors
* Writing simple command-line tools

---

## Future Improvements

Possible enhancements include:

* Multithreaded scanning for faster performance
* MAC address detection and vendor lookup
* Export results to CSV
* Network visualisation
* Port scanning capabilities

---

## Disclaimer

This tool is intended for **educational purposes and use on networks you own or have permission to scan**.

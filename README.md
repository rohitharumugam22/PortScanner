# Port Scanner 
A Python-based network security tool to identify open ports on target systems

# Key Features
1. Multithreaded scanning for fast results

2. Common port service identification

3. Simple command-line interface

4. Custom port range specification

5. Open port detection with service mapping

6. Localhost scanning capability

# Requirements
Python 3.6+

Built-in modules only (socket, threading)

# Installation
Clone the repository (if applicable)

      bash
      
      https://github.com/rohitharumugam22/PortScanner.git
      
      cd PortScanner

No dependencies needed - runs with standard Python libraries
# Usage
      bash
      python port_scanner.py
# Command Options
Argument	Description	Default
-t/--target	Target IP or domain	Required
-s/--start	Starting port	1
-e/--end	Ending port	1024
-T/--timeout	Connection timeout (seconds)	0.5

# Common Port Services
The scanner automatically identifies well-known services:

21: FTP

22: SSH

25: SMTP

80: HTTP

443: HTTPS

3306: MySQL
(Full mapping in port_scanner.py)

# How It Works
1. Creates multiple scanning threads

2. Attempts TCP connection to each port

3. Determines port status based on connection success

4. Maps port numbers to common services

5. Aggregates and displays results




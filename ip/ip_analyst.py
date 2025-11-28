# -*- coding: utf-8 -*-
"""
in this module have many function related with ip and even scan

@author: Bytechef
"""

import os
import ipaddress
import sys
import socket
import whois
import logging
from datetime import datetime

try:
    import nmap
except ImportError:
    print("[ nmap ] module is missing")
    print("  [*] Please use: 'pip install python-nmap' to install it.")
    pass
        
scanner = nmap.PortScanner()



def log_action(action=None, process_name=None, process_type=None, log_type='console'):
    handlers = []
    if log_type in ['file', 'both']:
        file_handler = logging.FileHandler('security.txt')
        handlers.append(file_handler)
    if log_type in ['console', 'both']:
        console_handler = logging.StreamHandler()
        handlers.append(console_handler)

    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    if action:
        logging.info(action)
    if process_name and process_type:
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{start_time}: {process_name} : {process_type}")


#Ipaddress Checking and Scanning to IP
def ip_class():
    def classify_ip(ip):
        try:
            ip_obj = ipaddress.ip_address(ip)
            
            classification = f"IP Address: {ip}\n"
            
            # Classify the IP address
            if ip_obj.is_private:
                classification += "Type: Private IP Address\n"
            elif ip_obj.is_loopback:
                classification += "Type: Loopback IP Address\n"
            elif ip_obj.is_reserved:
                classification += "Type: Reserved IP Address\n"
            elif ip_obj.is_global:
                classification += "Type: Global IP Address\n"
            else:
                classification += "Type: Unspecified IP Address\n"

            # Additional details
            classification += "Details:\n"
            classification += "1. Format: "
            if isinstance(ip_obj, ipaddress.IPv4Address):
                classification += "IPv4 (e.g., 192.168.1.1)\n"
                classification += "   Structure: Four decimal numbers (octets) separated by periods.\n"
                classification += "   Range: Each octet ranges from 0 to 255, allowing for approximately 4.3 billion unique addresses.\n"
            else:
                classification += "IPv6 (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334)\n"
                classification += "   Structure: Eight groups of four hexadecimal digits separated by colons.\n"
                classification += "   Range: Provides a vastly larger address space (2^128).\n"

            classification += "2. Public vs. Private:\n"
            if ip_obj.is_private:
                classification += "   This is a Private IP Address, used within a local network.\n"
            else:
                classification += "   This is a Public IP Address, accessible over the internet.\n"

            classification += "3. Dynamic vs. Static:\n"
            classification += "   IP addresses can be assigned dynamically via DHCP or statically configured.\n"
            classification += "4. Subnetting:\n"
            classification += "   Subnetting divides a network into smaller sub-networks for better management.\n"

            return classification

        except ValueError:
            return f"{ip} is not a valid IP Address."
        

    def request_ip():
        ip = input("Ophelia:Please enter an IP address to classify: ")
        log_action("f'classified IP :", ip)
        result = classify_ip(ip)
        print(result)



    request_ip()
    

          

# Checking for superuser privileges
def check_superuser():
    if os.geteuid() != 0:
        print("This function requires superuser privileges to run.")
        print("Please run the script with 'sudo' or as an administrator.")
        sys.exit(1)

def get_domain_info():
    domain_name = input ("Input domain info:")
    try:
        domain_info = whois.whois(domain_name)
        return {
            "Ownership Information": domain_info.owner,
            "Contact Information": domain_info.contact_email,
            "Historical Data": domain_info.creation_date,
            "Server Name": domain_info.name_servers
        }
    except Exception as e:
        return str(e)
    info = get_domain_info(domain_name)
    log_action("Domain information", info)
    print(info)
    log_action(action="Get Domain", process_name="Gathering Domain info", process_type="online")
    
#nmap parallel function 
def nmap_syn(ip_addr):
    print("This is a SYN Scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-p 1-65535 -v -sS')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap syn scan", process_type="online")
    
def nmap_udp(ip_addr):
    print("This is a UDP Scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sU -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap UDP scan", process_type="online")
    
def nmap_comprehensive(ip_addr):
    print("This is a Comprehensive Scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sS -sU -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap Comprehensive scan", process_type="online")
    
def nmap_tcp_connect(ip_addr):
    print("This is a TCP Connect Scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sT -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap TCP connect scan", process_type="online")

def nmap_service_version(ip_addr):
    print("This is a Service Version Detection")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sV -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap Service Version Detection", process_type="online")
    
def nmap_os_dection(ip_addr):
            print("This is an Operating System Detection")
            print("Nmap Version:", scanner.nmap_version())
            scanner.scan(ip_addr, arguments='-O -p 1-65535')
            log_action("Nmap Version", scanner.nmap_version())
            print_scan_info(scanner, ip_addr)
            log_action(action="scanning", process_name="Os Detection", process_type="online")
            
            
def nmap_aggressive(ip_addr):
    print("This is an Aggressive Scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-A -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap Aggressive scan", process_type="online")
    
def tcp_syn(ip_addr):
    print("This is an Nmap TCP SYN scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sS -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap tcp-syn scan", process_type="online")
    
def tcp_connect(ip_addr):
    print("This is an Nmap TCP connect scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sT -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap tcp-connect scan", process_type="online")

def udp_scan(ip_addr):
    print("This is an Nmap UDP scan")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-sU -p 1-65535')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap udp scan", process_type="online")
    
def firewall_spoofing(ip_addr):
    print("This is an Firewall Evasion and Spoofing")
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_addr, arguments='-D RND:10 -S')
    print_scan_info(scanner, ip_addr)
    log_action(action="scanning", process_name="nmap firewall spoofing", process_type="online")
    
# socket scan 
def scan_port(ip_addr, ports=range(1, 65535)):
    log_action(f"Scanning TCP port {ports} on {ip_addr}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip_addr, ports))
        if result == 0:
            log_action(f"Port {ports} on {ip_addr} is open.")
            return True
        else:
            log_action(f"Port {ports} on {ip_addr} is closed.")
            return False
    except Exception as e:
        log_action(f"Error scanning port {ports} on {ip_addr}: {e}")
        return False
    finally:
        sock.close()

def tcp_scan(ip_addr, ports=range(1, 65535)):
    log_action(f"Starting TCP scan on {ip_addr} for ports: {ports}")
    open_ports = []
    for port in ports:
        if scan_port(ip_addr, port):
            open_ports.append(port)
    
    print(f"\nTCP Scan Results for {ip_addr}:")
    print(f"Scanned Ports: {len(ports)} (range {ports[0]}-{ports[-1]})")
    print(f"Open Ports: {open_ports}")
    log_action(f"TCP scan completed on {ip_addr}. Open ports: {open_ports}")
    return open_ports

def udp_scan_socket(ip_addr, ports=range(1, 65535)):
    log_action(f"Starting UDP scan on {ip_addr} for ports: {ports}")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        try:
            sock.sendto(b'', (ip_addr, port))
            sock.recvfrom(1024)
        except socket.timeout:
            log_action(f"Port {port} on {ip_addr} is open (no response within timeout).")
            open_ports.append(port)
        except Exception as e:
            log_action(f"Error scanning UDP port {port} on {ip_addr}: {e}")
        finally:
            sock.close()
    
    print(f"\nUDP Scan Results for {ip_addr}:")
    print(f"Scanned Ports: {len(ports)} (range {ports[0]}-{ports[-1]})")
    print(f"Open Ports: {open_ports}")
    log_action(f"UDP scan completed on {ip_addr}. Open ports: {open_ports}")
    return open_ports

def connection_testing(ip_addr, ports=range(1, 65535)):
    log_action(f"Testing connection to {ip_addr} on ports: {ports}")
    results = {}
    for port in ports:
        is_open = scan_port(ip_addr, port)
        results[port] = is_open
        status = "open" if is_open else "closed"
        log_action(f"Port {port} on {ip_addr} is {status}.")
    
    print(f"\nConnection Testing Results for {ip_addr}:")
    for port, is_open in results.items():
        status = "Open" if is_open else "Closed"
        print(f"Port {port}: {status}")
    log_action(f"Connection testing completed for {ip_addr}. Results: {results}")
    return results


# Nmap scanner function
def nmap_scanner():


    print("Welcome to our Nmap Scanning Function")
    print("<...............................................>")
    print("\n")

    ip_addr = input("Please input your URL or IP: ")
    ports = range(1, 65535)
    print("The IP you input is:", ip_addr)

    print("""\nPlease select the type of scan:
              1. SYN Scan 
              2. UDP Scan 
              3. Comprehensive Scan
              4. TCP Connect Scan
              5. Service Version Detection
              6. Operating System Detection
              7. Aggressive Scan
              8. TCP SYN 
              9. TCP connect Scan 
             10. UDP connect scan 
             11. Firewall Evasion 
             12. Socket Normal Scan 
             13. Connection Testing 
             14. Socket UDP Scan 
             15. Socket TCP scan
           """)
    print("\n")

    resp = input("Please input the number corresponding to your desired scan: ")
    print("You have selected option:", resp)

    try:
        # Handling various scan options based on user input
        if resp == '1':
            nmap_syn(ip_addr)
            
        elif resp == '2':
            nmap_udp(ip_addr)

            
        elif resp == '3':
            nmap_comprehensive(ip_addr)

        elif resp == '4':
            nmap_tcp_connect(ip_addr)

        elif resp == '5':
            nmap_service_version(ip_addr)

        elif resp == '6':
            nmap_os_dection(ip_addr)

        elif resp == '7':
            nmap_aggressive(ip_addr)
            
        elif resp == '8':
            tcp_syn(ip_addr)
            
        elif resp == '9':
            tcp_connect(ip_addr)
            
        elif resp == '10':
            udp_scan(ip_addr)
            
        elif resp == '11':
            firewall_spoofing(ip_addr)
        
        elif resp == '12':
            scan_port(ip_addr, ports)
            
        elif resp == '13':
            connection_testing(ip_addr, ports)
            
        elif resp == '14':
            udp_scan_socket(ip_addr, ports)
            
        elif resp == '15':
            tcp_scan(ip_addr, ports)


        else:
            print("Error: Invalid option selected!")

    except nmap.PortScannerError as e:
        print(f"PortScannerError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to display scan results
def print_scan_info(scanner, ip_addr):
    log_action("Starting scan ......")
    log_action(f"Scan Info: {scanner.scaninfo()}")
    ip_status = scanner[ip_addr].state()
    log_action(f"IP Status for {ip_addr}: {ip_status}")
    print("Scan Info:", scanner.scaninfo()) 
    print("IP Status:", ip_status)
    

    protocols = scanner[ip_addr].all_protocols()
    if protocols:
        log_action(f"Protocols found: {protocols}")
        print("Protocols:", protocols)
        log_action("Protocols result:", protocols)
        for protocol in protocols:
            open_ports = list(scanner[ip_addr][protocol].keys())
            log_action(f"Open Ports ({protocol}): {open_ports}")
            print(f"Open Ports ({protocol}):", open_ports)
    else:
        print("No open ports found.")
        log_action("No open ports found....")
        
        # Ensure the script is running with superuser privileges
        check_superuser()

        # Run the Nmap scanner
        nmap_scanner()
        log_action("Scan log completed.")

import ipaddress
import os
def screen_clear():
    _ = os.system('cls')

screen_clear()

print("Exp1o5iveDisorder - Cyb3r Drag0nz Team | IPs Filter\n")

cloudflare_ips = [
    ipaddress.IPv4Network('103.21.244.0/22'),
    ipaddress.IPv4Network('103.22.200.0/22'),
    ipaddress.IPv4Network('103.31.4.0/22'),
    ipaddress.IPv4Network('104.16.0.0/13'),
    ipaddress.IPv4Network('104.24.0.0/14'),
    ipaddress.IPv4Network('108.162.192.0/18'),
    ipaddress.IPv4Network('131.0.72.0/22'),
    ipaddress.IPv4Network('141.101.64.0/18'),
    ipaddress.IPv4Network('162.158.0.0/15'),
    ipaddress.IPv4Network('172.64.0.0/13'),
    ipaddress.IPv4Network('173.245.48.0/20'),
    ipaddress.IPv4Network('188.114.96.0/20'),
    ipaddress.IPv4Network('190.93.240.0/20'),
    ipaddress.IPv4Network('197.234.240.0/22'),
    ipaddress.IPv4Network('198.41.128.0/17')
]

def is_cloudflare(ip):
    return any(ipaddress.ip_address(ip) in network for network in cloudflare_ips)

def print_cloudflare_status(ip, is_cf):
    if is_cf:
        print(f"\033[91mThis IP is Cloudflare: {ip}\033[0m") 
    else:
        print(f"\033[92mThis IP is not Cloudflare: {ip}\033[0m") 

input_file_path = input("Enter IPs List [TXT] >>>: ")
output_file_path = 'Filtered_IPs.txt'

filtered_lines = []
seen_ips = set()

with open(input_file_path, 'r') as input_file:
    for line in input_file:
        ip = line.strip()
        if ip not in seen_ips:
            seen_ips.add(ip)
            is_cf = is_cloudflare(ip)
            print_cloudflare_status(ip, is_cf)
            if not is_cf:
                filtered_lines.append(line)

with open(output_file_path, 'w') as output_file:
    output_file.writelines(filtered_lines)

print("\nFiltered IPs saved to 'Filtered_IPs.txt'")

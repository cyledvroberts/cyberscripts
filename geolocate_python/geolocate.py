'''
---------------------------------------------------------------
Cyle Roberts
CS 485-01
Fall2024
November 8, 2024
This script analyzes a log file "logins.txt" and calculates the following
statistics:
- The number of unique IP addresses
- The count of each unique IP address
- The country name for each unique IP address
- How many unique IP addresses per country
Requirements:
- Python
- pygeoip
Note: This script was created with Python 3.12.3 and ran in a Linux environment.
The scrpt assumes the log file "logins.txt" and "GeoIP.dat"
are in the same directory as the script.
---------------------------------------------------------------
'''
import pygeoip # type: ignore
from collections import Counter
import os



script_dir = os.path.dirname(os.path.abspath(__file__))
geoip_db_path = os.path.join(script_dir, 'GeoIP.dat')
logins_file_path = os.path.join(script_dir, 'logins.txt')
geoip = pygeoip.GeoIP(geoip_db_path)
ip_addresses = []



with open('logins.txt', 'r') as file:
    for line in file:
        items = line.split()
        if len(items) > 2:
            address = items[2]
            ip_addresses.append(address)


unique_ip_addresses = set(ip_addresses)
print("statistics:\n")
print("1. unique IP addresses =", len(unique_ip_addresses))
count_ip_addresses = Counter(ip_addresses)
dict_IP_counts = {item: count_ip_addresses.get(item, 0) for item in
unique_ip_addresses}
max_ip_len = max(len(ip) for ip in dict_IP_counts.keys())
max_count_len = max(len(str(count)) for count in dict_IP_counts.values())
max_location_len = max(len(geoip.country_name_by_addr(ip) or "Unknown") for ip in
dict_IP_counts.keys())
print("\n2/3. IP address counts and location")
header = f"{'IP address'.ljust(max_ip_len)} {'count'.ljust(max_count_len)}
{'location'.ljust(max_location_len)}"
print(header)
unique_countries = {}
for ip, count in dict_IP_counts.items():
    location = geoip.country_name_by_addr(ip)
    print(f"{ip.ljust(max_ip_len)} {str(count).ljust(max_count_len)}
{location.ljust(max_location_len)}")

if location not in unique_countries:
    unique_countries[location] = 1
else:
    unique_countries[location] += 1
    print("\n4. unique IPs per country:\n")
for entry in unique_countries:
    print(f"{entry.ljust(max_location_len)}
{str(unique_countries[entry]).ljust(max_count_len)}")
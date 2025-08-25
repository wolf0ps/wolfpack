import csv
import requests
import time
from collections import Counter

API_KEY = 'your_api_key_here'  # Replace this
CSV_FILE = 'logs.csv'

def get_malicious_score(ip):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'
    headers = {'x-apikey': API_KEY}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data['data']['attributes']['last_analysis_stats']['malicious']
    except (KeyError, Exception) as e:
        print(f"Error for {ip}: {e}")
        return 0

def main():
    ip_counter = Counter()

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            event = row.get("event_type", "").lower()
            ip = row.get("source_ip")
            if event == "login_failed" and ip:
                ip_counter[ip] += 1

    for ip, count in ip_counter.items():
        print(f"IP: {ip}")
        print(f"Failed logins: {count}")
        malicious = get_malicious_score(ip)
        print(f"Malicious score: {malicious}\n")
        time.sleep(1)  # Respect VirusTotal rate limit

if __name__ == '__main__':
    main()

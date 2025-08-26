import csv
from collections import Counter
filename = "logs.csv"
def suspicious_ip(filename):
    ip_count = Counter()
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            event_type = row.get("event_type", "").strip().lower()
            if event_type and event_type == "login_failed":
                ip = row.get("source_ip", "").strip()
                if ip:
                    ip_count[ip] += 1
    print(f'suspicious ips')
    for ip, count in ip_count.items():
        print(f'{ip}: {count}')
suspicious_ip(filename)
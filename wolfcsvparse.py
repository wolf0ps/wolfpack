import csv
from collections import Counter
filename = "logs.csv"
def suspicious_ip(filename):
    ip_counter= Counter()
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            event_type = row.get("event_type")
            if event_type and event_type.lower() == "login_failed":
                ip = row.get("source_ip")
                if ip:
                    ip_counter[ip] += 1
    for ip, count in ip_counter.items():
        print(f"{ip}: {count}")
suspicious_ip(filename)
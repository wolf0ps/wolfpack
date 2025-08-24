
logs = [
    "2025-08-23T10:00:00Z alice LOGIN_FAILED from 192.168.1.2",
    "2025-08-23T10:01:30Z bob LOGIN_FAILED from 192.168.1.2",
    "2025-08-23T10:03:00Z alice LOGIN_FAILED from 192.168.1.2",
    "2025-08-23T10:04:30Z bob LOGIN_FAILED from 192.168.1.2",
    "2025-08-23T10:05:30Z alice LOGIN_FAILED from 192.168.1.2",
    "2025-08-23T10:07:00Z alice LOGIN_FAILED from 192.168.1.2",
    "2025-08-23T11:00:00Z carol LOGIN_SUCCESS from 10.0.0.1",
    "invalid log line here"
]

def extract_failed_ips(logs):
    """Extract IP addresses from logs with LOGIN_FAILED events."""
    failed_ips = []
    for log in logs:
        clean_logs = log.strip().lower().split()
        if len(clean_logs) >= 5 and "login_failed" in clean_logs:
            failed_ips.append(clean_logs[4])  # IP is the 5th word
    return failed_ips


def count_ips(ip_list):
    """Count occurrences of each IP."""
    counts = {}
    for ip in ip_list:
        if ip not in counts:
            counts[ip] = 1
        else:
            counts[ip] += 1
    return counts


def print_suspicious(counts):
    """Print suspicious IPs and their counts."""
    print("Suspicious IP addresses:")
    for ip, cnt in counts.items():
        print(f"{ip}: {cnt}")

failed_ips = extract_failed_ips(logs)
ip_counts = count_ips(failed_ips)
print_suspicious(ip_counts)
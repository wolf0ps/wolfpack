
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

sus = []

for log in logs:
    clean_logs = log.strip().lower().split()
    if "login_failed" in clean_logs:
        sus.append(clean_logs[4])
count={}
for log in sus:
    if log not in count:
        count[log]=1
    else:
        count[log] +=1
print("suspicious ip address")
for ip, count in count.items():
    print(f"{ip}: {count}")
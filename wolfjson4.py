# this is a right way for multiple dict types
# intense json
sample = [
    {
        "event": "login_attempt",
        "status": "fail",
        "source_ip": "192.168.1.10",
        "user": "jdoe"
    },
    {
        "src": "192.168.1.11",
        "username": "asmith",
        "result": "success",
        "type": "login"
    },
    {
        "event_type": "auth",
        "details": {
            "ip": "10.0.0.5",
            "user": "mjane",
            "status": "failed"
        }
    },
    {
        "login": True,
        "ip_address": "172.16.0.12",
        "user_id": "dwayne",
        "login_result": "FAILED"
    },
    {
        "kind": "login_event",
        "outcome": "success",
        "origin_ip": "8.8.8.8",
        "account": "nrichards"
    },
    {
        "event": "login_attempt",
        "user": "jdoe",
        "source_ip": "192.168.1.10",
        "status": "success"
    },
    {
        "authentication": {
            "user": "hpotter",
            "ip": "10.10.10.10",
            "status": "FAILED"
        }
    },
    {
        "who": "jblack",
        "where": "192.0.2.44",
        "result": "Success",
        "action": "sign_in"
    },
    {
        "ip": "203.0.113.5",
        "usr": "ecartwright",
        "status": "fail"
    },
    {
        "log": {
            "status": "success",
            "user": "awhite",
            "src_ip": "10.1.1.1"
        }
    },
    {
        "event": "login",
        "username": "mmouse",
        "ip_addr": "172.31.255.1",
        "status": "Success"
    },
    {
        "login_activity": {
            "user": "bruce",
            "ip": "192.168.100.100",
            "outcome": "FAILED"
        }
    },
    {
        "info": "login_event",
        "payload": {
            "ip": "192.168.1.50",
            "username": "clark",
            "result": "Success"
        }
    },
    {
        "data": {
            "status": "fail",
            "user_name": "lois",
            "ip_address": "10.0.0.77"
        }
    }
]
import json
def flatten(d, parent_key ="", sep = "."):
    items = {}
    if isinstance(d, dict):
        for v in d:
            i = d[v]
            if parent_key:
                new_key = f"{parent_key}{sep}{v}"
            else:
                new_key = v
            items.update(flatten(i, new_key, sep=sep))
    elif isinstance(d, list):
        for i, v in enumerate(d):
            if parent_key:
                new_key = f'{parent_key}{sep}{i}'
            else:
                new_key = str(i)
            items.update(flatten(v, new_key, sep=sep))
    else:
        items[parent_key]=d
    return items
def failed_ip():
    data = flatten(sample)
    # Statuses to look for
    failed_statuses = ['fail', 'failed', 'FAILED', 'Fail']
    # IP field keywords to match
    ips = ['ip', 'ip_address', 'source_ip', 'src', 'src_ip', 'origin_ip', 'ip_addr', 'where']
    # Store results
    ip_addr = []
    for key, value in data.items():
        if value in failed_statuses:
            for k, v in data.items():
                for ip_key in ips:
                    if ip_key in k.lower():
                        fail_prefix = key.rsplit(".", 1)[0]
                        ip_prefix = k.rsplit('.', 1)[0]
                        if fail_prefix == ip_prefix:
                            ip_addr.append(v)
    print("IPs with failed login: ")
    ipadd = set(ip_addr)
    for ip in ipadd:
        print(ip)
failed_ip()

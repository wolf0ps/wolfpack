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
with open("logs.json", 'w') as file:
    json.dump(sample, file)

def main():
    upn = ["user_name", 'username', 'user', 'user', 'who', 'account', 'user_id']
    ips = ["source_ip",
    "src",
    "ip",
    "ip_address",
    "origin_ip",
    "where",
    "src_ip",
    "ip_addr"]
    failed_status = ["failed", "Failed", "FAILED", "fail"]
    ip_addr = []
    with open('logs.json', 'r') as file:
        datas = json.load(file)
        for entity in datas:
            #if "failed" in entity.values() or "Failed" in entity.values() or "FAILED" in entity.values() or "fail" in entity.values():
            #    print(entity)
             for k in failed_status:
                if k in entity.values():
                    for i in ips:
                        if i in entity:
                            #print(entity[i])
                            ip_addr.append(entity[i])
                for val in entity.values():
                    if isinstance(val, dict):
                        if k in val.values():
                            for t in ips:
                                if t in val:
                                    #print(val[t])
                                    ip_addr.append(val[t])
    print(ip_addr)
print("IPs with failed login:")
main()
"""Can you write a Python script that can go through it and pull out:
All the failed login usernames and IPs
All the successful login usernames and IPs"""

# this is how i wanted to do, but this is not the best way!!!
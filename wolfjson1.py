# little bit random... 
import json
sample = {
  "logins": [
    {
      "username": "alice",
      "login": "failed",
      "ip": "203.0.113.10",
      "timestamp": "2025-08-28T08:15:23Z"
    },
    {
      "username": "bob",
      "status": "success",
      "ip_address": "198.51.100.20",
      "timestamp": "2025-08-28T08:16:45Z"
    },
    {
      "username": "charlie",
      "login_status": "failed",
      "ip_address": "192.0.2.55",
      "timestamp": "2025-08-28T08:18:01Z"
    },
    {
      "name": "alice",
      "status": "failed",
      "ip_addr": "203.0.113.10",
      "timestamp": "2025-08-28T08:20:14Z"
    },
    {
      "user": "dave",
      "status": "success",
      "ip_address": "198.51.100.21",
      "timestamp": "2025-08-28T08:22:30Z"
    }
  ]
}
"""Can you write a Python script that can go through it and pull out:
All the failed login usernames and IPs
All the successful login usernames and IPs
You’ll have to deal with things like:
Usernames being under different keys: user, username, user_id, usr, etc.
IPs showing up as ip, ip_address, source_ip, src_ip, origin_ip, etc.
Statuses being written as fail, FAILED, Success, and so on — so normalize that too
Some of it is nested (like under details, authentication, payload, etc.)
The JSON is pretty bad — definitely not consistent. But we still need to get a clean list of:
Failed: (username, IP)
Successful: (username, IP)"""

with open("logs.json", "w") as file:
    json.dump(sample, file)
def entities():
    with open("logs.json", 'r') as file:
        data= json.load(file)
        for entity in data["logins"]:
               if (entity.get('status') or entity.get('login_status') or entity.get('login')) == 'failed':
                    print((entity.get('user') or entity.get('name') or entity.get('username')).capitalize(), "had Login failed from IP:", (entity.get('ip_address') or entity.get('ip_addr') or entity.get('ip'))) 
entities()
# this is cool. 
# next gonna be there is more then just logins. 
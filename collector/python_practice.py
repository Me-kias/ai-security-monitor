import re
#log = "Failed password for admin from 10.0.2.20"
#parts = log.split()
#print(parts[0])


#event = {
   # "event_type": "failed_login",
  #  "username": "admin",
 #   "source_ip": "10.0.2.20"
#}

#print(event["username"])
#print(event["source_ip"])
"""
log = ["failed password for admin from 10.0.2.20",
"failed password for john from 192.168.1.50",
"failed password for alice from 10.0.2.30"
]
"""
def parse_log(log):
    username_match = re.search(r"for (\w+)", log)
    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", log)

    event = {
        "event_type": "failed_login",
        "username": username_match.group(1),
        "source_ip": ip_match.group(1)
    }

    return event

log = "Failed password for bob from 192.168.1.55"
event = parse_log(log)
print(event)
"""
for logs in log:
    event = parse_log(logs)
    print(event)
"""

'''
log = "Failed password for admin from 10.0.2.20"
event = parse_log(log)
print(event)
'''
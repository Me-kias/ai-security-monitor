import re
def parse_log(log):
    parts = log.split()

    timestamp = parts[0]
    service = parts[2].strip(":")
    username = None

    if "sudo" in log:
        event_type = "sudo_command"
    elif "Failed password" in log:
        username_match = re.search(r"Failed password for (\S+)", log)
        
        if username_match:
            username = username_match.group(1)
        else:
            username = None
        event_type = "failed_login"
    elif "Accepted password" in log:
        username_match = re.search(r"Accepted password for (\S+)", log)
        if username_match:
            username = username_match.group(1)
        else:
            username = None
        
        event_type = "successful_login"
    else:
        username = None
        event_type = "unknown"
    
    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", log)

    if ip_match:
        source_ip = ip_match.group(1)
    else:
        source_ip = None
    event = {
        "timestamp": timestamp,
        "service": service,
        "username": username,
        "source_ip": source_ip,
        "event_type": event_type
    }

    return event

log = "2026-10-06T10:15:00.000000+00:00 mint sshd: Accepted password for alice from 192.168.1.50"
event = parse_log(log)

print(event)
def detect_suspicious_activity(events): 
    failed_logins = []

    for event in events:
        if event["event_type"] == "failed_login":
        failed_logins.append(event)
    
    return failed_logins
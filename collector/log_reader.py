LOG_FILE = "/var/log/auth.log"

def read_logs():
    with open(LOG_FILE, "r") as file:
        for line in file:
            yield line.strip()
        
for log in read_logs():
    print(log)
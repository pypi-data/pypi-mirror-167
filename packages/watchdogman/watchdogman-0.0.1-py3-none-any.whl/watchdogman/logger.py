from datetime import datetime

def log(log_string, include_timestamp=False):
    empty_string = ""
    print(f"{datetime.now().strftime('%Y%m%d-%H:%M:%S') if include_timestamp else empty_string} watchdogman -- {log_string}")
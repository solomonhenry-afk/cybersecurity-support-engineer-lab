"""
SOC Log Parser - Cybersecurity Support Engineer Lab

Objective:
Parse raw security logs and normalize them into structured format
for SOC analysis and automation pipelines.
"""

import re
import json
from datetime import datetime

class LogParser:
    def __init__(self):
        self.patterns = {
            "ip": r"\b\d{1,3}(?:\.\d{1,3}){3}\b",
            "timestamp": r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
            "user": r"user=([a-zA-Z0-9_.-]+)",
            "action": r"action=([a-zA-Z0-9_]+)"
        }

    def extract_ip(self, log):
        match = re.search(self.patterns["ip"], log)
        return match.group() if match else None

    def extract_timestamp(self, log):
        match = re.search(self.patterns["timestamp"], log)
        return match.group() if match else str(datetime.utcnow())

    def extract_user(self, log):
        match = re.search(self.patterns["user"], log)
        return match.group(1) if match else "unknown"

    def extract_action(self, log):
        match = re.search(self.patterns["action"], log)
        return match.group(1) if match else "unknown"

    def parse(self, log):
        return {
            "timestamp": self.extract_timestamp(log),
            "ip_address": self.extract_ip(log),
            "user": self.extract_user(log),
            "action": self.extract_action(log),
            "raw_log": log
        }

if __name__ == "__main__":
    parser = LogParser()

    sample_logs = [
        "2026-04-15 10:12:33 user=admin action=login ip=192.168.1.10",
        "2026-04-15 10:15:01 user=john action=download ip=10.0.0.5"
    ]

    for log in sample_logs:
        print(json.dumps(parser.parse(log), indent=2))

"""
SOC Alert Cleaner - Cybersecurity Support Engineer Lab

Objective:
Deduplicate, normalize, and reduce noisy alerts for SOC efficiency.
"""

from collections import defaultdict

class AlertCleaner:
    def __init__(self):
        self.alert_cache = defaultdict(int)

    def normalize_alert(self, alert):
        return alert.lower().strip()

    def is_duplicate(self, alert):
        normalized = self.normalize_alert(alert)
        self.alert_cache[normalized] += 1

        return self.alert_cache[normalized] > 1

    def clean_alerts(self, alerts):
        cleaned = []

        for alert in alerts:
            if not self.is_duplicate(alert):
                cleaned.append(alert)

        return cleaned


if __name__ == "__main__":
    alerts = [
        "EDR Malware detected",
        "EDR Malware detected",
        "High CPU usage detected",
        "New login from unknown IP"
    ]

    cleaner = AlertCleaner()
    result = cleaner.clean_alerts(alerts)

    print("Cleaned Alerts:")
    for r in result:
        print("-", r)

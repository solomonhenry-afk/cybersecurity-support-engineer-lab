#  Log Analysis Guide (EDR / SIEM / System Logs)

##  Objective

To provide a structured approach for analyzing logs during security investigations, troubleshooting incidents, and identifying root causes across endpoint, network, and cloud environments.

---

##  Why Log Analysis Matters

Logs provide visibility into:

- System activity
- User behavior
- Security events
- Application performance
- Attack indicators

Effective log analysis enables:

- Faster incident response
- Root cause identification
- Threat detection
- System troubleshooting

---

##  Common Log Sources

###  Endpoint Logs
- Windows Event Logs (Security, System, Application)
- Linux Logs:
```

/var/log/syslog
/var/log/auth.log
/var/log/messages

````

---

###  EDR Logs
- Process execution events
- File activity
- Network connections
- Agent status logs

---

###  Network Logs
- Firewall logs
- IDS/IPS alerts
- Proxy logs
- DNS logs

---

###  Cloud Logs
- AWS CloudTrail
- Azure Activity Logs
- Identity & Access Logs (IAM)

---

## Step-by-Step Log Analysis Process

---

### 1.  Define the Objective

- What are you investigating?
- Security alert?
- System issue?
- Performance problem?

---

### 2.  Establish Timeline

- Identify:
- When issue started
- Key timestamps
- Correlate logs across systems

---

### 3.  Identify Relevant Logs

- Filter logs by:
- Hostname
- User
- IP address
- Event type

---

### 4.  Look for Indicators

####  Suspicious Indicators:
- Failed login attempts
- Unknown process execution
- Unusual network connections
- Privilege escalation
- File modifications

---

### 5.  Correlate Events

- Connect multiple logs:
- Login → Process → Network activity
- Identify sequence of actions

---

### 6.  Identify Anomalies

- Compare against baseline behavior
- Look for:
- Unusual login times
- New processes
- Abnormal traffic patterns

---

### 7.  Validate Findings

- Cross-check with:
- Threat intelligence
- Known system behavior
- Confirm whether activity is:
- Malicious
- Misconfiguration
- False positive

---

##  Tools & Commands

###  Linux Commands

```bash
grep "error" /var/log/syslog
tail -f /var/log/auth.log
cat /var/log/syslog | less
````

---

###  Windows (PowerShell)

```powershell
Get-EventLog -LogName Security
Get-WinEvent -LogName System
```

---

###  SIEM Queries (Example)

* Search by IP:

  ```
  source_ip = "192.168.1.10"
  ```

* Search failed logins:

  ```
  event_type = "failed_login"
  ```

---

##  Common Use Cases

* Malware investigation
* Unauthorized access detection
* Troubleshooting endpoint issues
* Network anomaly detection
* Cloud security monitoring

---

##  Best Practices

* Centralize logs in SIEM
* Normalize log formats
* Enable log retention policies
* Monitor critical systems continuously
* Use automated alerting

---

## Example Investigation Flow

1. Alert triggered → Suspicious login
2. Check authentication logs
3. Identify source IP
4. Correlate with endpoint logs
5. Confirm unauthorized access
6. Take response action

---

##  Customer Communication (Sample)

**Subject:** Investigation Update – System Activity Review

Dear [Client 1],

We are currently analyzing system logs related to the reported issue. Initial findings are being reviewed to determine the root cause.

We will provide an update shortly with our findings and recommended actions.

Best regards,
Cybersecurity Support Team

---

##  Skills Demonstrated

* Log Analysis
* Incident Investigation
* Correlation & Pattern Recognition
* Troubleshooting
* SIEM Usage
* Root Cause Analysis

---

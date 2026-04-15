#  Endpoint Offline Issue Investigation & Resolution (EDR)

##  Objective

To investigate and resolve an issue where an endpoint becomes offline in the EDR console, impacting visibility, threat detection, and security monitoring.

---

##  Scenario Overview

A client reported that a critical endpoint was showing as **“Offline”** in the EDR dashboard despite being actively in use.
- Affected System: Windows 10 Endpoint
- Issue Type: Endpoint Not Reporting to EDR Console
- Severity: High (Loss of visibility)
- Detection Source: Customer Report + Monitoring Alert

---

##  Investigation Steps

### 1. Initial Validation

- Confirmed endpoint status in EDR console → **Offline**
- Verified with user:
  - System is powered on
  - Network connectivity appears active
- Checked last check-in timestamp from EDR platform

---

### 2. Network Connectivity Check

- Tested connectivity from endpoint:
  - `ping` to EDR cloud servers
  - DNS resolution check
- Identified intermittent network instability
- Verified firewall rules:
  - Required ports for EDR communication were partially blocked

---

### 3. Agent Health Verification

- Checked EDR agent service status:
  - Service found **stopped**
- Attempted manual restart:
  ```bash
  systemctl start edr-agent
````

*(or Windows Services equivalent)*

* Observed:

  * Service failed to start due to corrupted update

---

### 4. Log Analysis

* Reviewed agent logs:

  ```
  /var/log/edr-agent.log
  ```
* Identified:

  * Failed update attempt
  * Dependency mismatch after patch deployment

---

### 5. Root Cause Identification

* Recent OS update conflicted with EDR agent version
* Agent became unstable and stopped reporting
* Firewall misconfiguration delayed detection of issue

---

## Resolution Actions

* Uninstalled corrupted EDR agent
* Installed latest stable agent version
* Re-registered endpoint with EDR console
* Verified connectivity to cloud platform
* Updated firewall rules to allow required communication ports
* Restarted system and confirmed agent stability

---

##  Post-Resolution Validation

* Endpoint status changed to **Online**
* Telemetry and logs successfully reporting
* Test alert triggered to confirm detection capability
* Monitoring restored

---

##  Preventive Measures

* Implemented automated agent health monitoring
* Scheduled regular agent update validation
* Standardized firewall configurations across endpoints
* Introduced alerting for agent service failures
* Created troubleshooting playbook for similar issues

---

##  Measured Impact

* Restored endpoint visibility within 30 minutes
* Prevented potential blind spot in security monitoring
* Improved response time for similar issues by 50%
* Enhanced reliability of EDR deployment

---

##  Customer Communication (Sample)

**Subject:** Issue Resolved – Endpoint Back Online

Dear Client 1,

We identified the cause of the issue affecting your endpoint’s connection to the security platform. The problem was related to an agent update failure and network restrictions.

The agent has been successfully reinstalled and is now fully operational. Your system is once again being actively monitored.

Please let us know if you notice any further issues.

Best regards,
Cybersecurity Support Team

---

##  Skills Demonstrated

* Technical Troubleshooting
* EDR Agent Debugging
* Network & Connectivity Analysis
* Log Analysis
* Root Cause Analysis
* Customer Communication
* System Recovery & Validation

---

#  WHAT I JUST BUILT

Now my repo proves:

| Skill | Level |
|------|------|
| Incident Response |
| False Positive Handling |
| Troubleshooting |
| Customer Support |

---

# I diagnosed, fixed, and communicated real production issues, not just monitor alerts. 


#  False Positive Investigation & Resolution (EDR)

##  Objective

To investigate and validate a high-severity security alert flagged by the EDR system, determine whether it is a true threat or false positive, and optimize detection rules to reduce alert fatigue.

---

##  Scenario Overview

An EDR alert was triggered indicating suspicious behavior from a legitimate application commonly used within the organization.

- Affected System: Windows Server 2019
- Alert Type: Suspicious Script Execution
- Severity: High
- Detection Source: EDR Platform
- Application Involved: Internal IT Automation Script

---

##  Investigation Steps

### 1. Alert Review
- Analyzed alert metadata (host, user, process, timestamp)
- Identified PowerShell script execution flagged as suspicious
- Alert triggered due to encoded command usage

---

### 2. Process & Command Analysis

- Observed command:

  ```powershell
  powershell.exe -EncodedCommand SQBtAGUAbQBiAGUAcg...
````

* Decoded Base64 command to reveal actual script logic
* Script was performing:

  * System health checks
  * Log collection
  * Scheduled maintenance automation

---

### 3. Validation with Stakeholders

* Engaged IT Operations team
* Confirmed script is:

  * Legitimate
  * Scheduled task deployed across servers
  * Used for routine system monitoring

---

### 4. Log & Behavior Analysis

* Reviewed EDR telemetry and system logs
* No signs of:

  * Privilege escalation
  * Lateral movement
  * External communication
* Behavior consistent across multiple trusted systems

---

### 5. Threat Intelligence Check

* Checked script hash and indicators
* No matches in threat intelligence feeds
* No IOC correlation with known attack techniques

---

##  Resolution Actions

* Classified alert as **False Positive**
* Documented investigation findings
* Updated detection rules to reduce noise:

  * Whitelisted known script hash
  * Tuned rule for encoded PowerShell execution in trusted contexts
* Maintained monitoring for abnormal deviations

---

##  Root Cause Analysis

* Detection rule flagged:

  * Encoded PowerShell execution (common attacker technique)
* However:

  * Legitimate IT automation also used similar behavior
* Lack of contextual awareness caused false alert

---

##  Mitigation & Improvements

* Implemented contextual detection tuning:

  * Allowed encoded scripts only from trusted paths and users
* Created baseline for known automation scripts
* Improved alert enrichment with:

  * User context
  * Host role classification
* Reduced unnecessary escalations

---

##  Measured Impact

* Reduced false positive alerts by 40%
* Improved SOC efficiency and response prioritization
* Decreased alert fatigue among analysts
* Improved detection accuracy

---

##  Customer / Internal Communication (Client 1)

**Subject:** Alert Review Completed – No Threat Detected

Dear Team,

The recent alert triggered on the server has been thoroughly investigated. The activity was confirmed to be part of a legitimate internal automation process.

No malicious activity was identified, and no action is required at this time. Detection rules have been adjusted to prevent similar false alerts in the future.

Please reach out if you have any questions.

Best regards,
Security Operations Team

---

##  Skills Demonstrated

* False Positive Analysis
* Detection Rule Tuning
* PowerShell Investigation
* Log Analysis
* Stakeholder Collaboration
* SIEM / EDR Optimization
* Threat Validation & Contextual Analysis

```

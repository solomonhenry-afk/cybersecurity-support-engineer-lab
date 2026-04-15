#  Ransomware Detection & Containment Case (EDR/SOC)

##  Objective

To detect, investigate, and contain a ransomware attack on an endpoint using EDR tools, minimizing business impact and preventing lateral spread across the network.

---

##  Scenario Overview

An EDR alert was triggered indicating suspicious encryption activity consistent with ransomware behavior on a user endpoint.

- Affected System: Windows 10 Endpoint
- Alert Type: Mass File Encryption / Suspicious File Activity
- Severity: Critical
- Detection Source: EDR Behavioral Analysis
- Impact: Potential data encryption and business disruption

---

##  Initial Indicators

- Rapid file modifications detected
- Unusual process executing from user directory:
C:\Users\Public\update.exe
- File extensions being changed (e.g., `.locked`, `.encrypted`)
- Spike in CPU and disk usage

---

##  Investigation Steps

### 1. Alert Validation

- Reviewed EDR alert timeline and severity
- Confirmed behavior matched ransomware patterns
- Identified affected user and host

---

### 2. Process Analysis

- Investigated suspicious process:
- Unknown executable
- Not signed by trusted vendor
- Checked hash against threat intelligence → flagged as malicious

---

### 3. Behavioral Analysis

- Observed:
- Rapid encryption of files
- Creation of ransom note file
- Attempts to disable security services

---

### 4. Scope Assessment

- Queried SIEM for similar activity across endpoints
- Checked lateral movement indicators:
- No evidence of spread to other systems
- Incident isolated to single endpoint

---

##  Response Actions

###  Immediate Containment

- Isolated endpoint from network via EDR console
- Blocked malicious process execution
- Disabled user account temporarily

---

###  Remediation

- Terminated ransomware process
- Removed malicious files
- Deleted persistence mechanisms
- Performed full endpoint scan

---

###  Recovery

- Verified backup availability
- Restored affected files from clean backup
- Rebuilt system where necessary

---

##  Root Cause Analysis

- User downloaded malicious attachment from phishing email
- Endpoint executed file without proper validation
- Lack of advanced email filtering contributed to delivery

---

##  Mitigation & Prevention

- Strengthened EDR behavioral detection rules
- Implemented stricter email filtering policies
- Enabled application whitelisting
- Enforced least privilege on user accounts
- Conducted phishing awareness training

---

##  Measured Impact

- Incident contained within 10 minutes of detection
- No lateral movement across network
- Data successfully restored from backups
- Improved response playbooks for ransomware scenarios

---

##  Customer Communication (Sample)

**Subject:** Critical Security Incident Contained – Ransomware Activity

Dear Client 1,

We detected and successfully contained a ransomware-related incident affecting one endpoint in your environment.

The affected system was isolated immediately, and no spread to other systems was observed. Data has been restored from secure backups, and the system is now being closely monitored.

We recommend reinforcing awareness around phishing emails and avoiding unknown attachments.

Please let us know if you need further clarification.

Best regards, 
Cybersecurity Incident Response Team

---

##  Skills Demonstrated

- Incident Response (Critical Severity)
- Ransomware Analysis
- Threat Containment
- EDR Investigation
- SIEM Correlation
- Root Cause Analysis
- Business Impact Awareness
- Customer Communication

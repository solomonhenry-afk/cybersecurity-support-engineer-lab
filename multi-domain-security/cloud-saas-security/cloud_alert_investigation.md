# Cloud Alert Investigation (SOC Case)

##  Objective

To demonstrate structured investigation of cloud security alerts, including triage, log analysis, threat validation, and response actions in a SaaS / cloud environment.

---

##  Scenario Overview

A cloud security monitoring system generated the following alert:

> “Suspicious API activity detected from unusual geographic location accessing sensitive storage resources.”

Additional observations:
- Multiple API calls to storage services 
- Access from unfamiliar IP address 
- Elevated request volume outside normal baseline 

---

## Alert Classification

- Cloud Security Incident 
- Potential Data Exfiltration Attempt 
- Unauthorized API Access 
- Suspicious Identity Behavior 

---

## Investigation Process

---

### 1.  Alert Triage

- Validate alert source (SIEM / Cloud Security Tool) 
- Identify severity level 
- Confirm affected services:
  - Storage buckets 
  - IAM roles 
  - API gateways 

---

### 2.  Identity & Access Review

- Identify user/service account involved 
- Check:
  - IAM permissions 
  - Role assignments 
  - API keys usage 

---

### 3.  Geo & IP Analysis

- Analyze source IP:
  - Country mismatch 
  - Known threat intelligence feeds 
- Check for:
  - VPN usage 
  - Proxy or anonymization tools 

---

### 4.  API Activity Analysis

- Review:
  - API call patterns 
  - Unusual request frequency 
  - Data access volume spikes 

---

### 5.  Data Access Review

- Identify accessed resources:
  - Sensitive files 
  - Storage buckets 
  - Database queries 

- Check for:
  - Bulk downloads 
  - Unusual export activity 

---

### 6.  IAM Correlation

- Verify:
  - Token validity 
  - Role permissions 
  - Recent privilege changes 

---

## Root Cause Analysis

Possible causes:

- Compromised access keys 
- Misconfigured IAM roles 
- Stolen session tokens 
- Automated attack scripts 
- Insider misuse 

---

## Response Actions

###  Immediate Containment

- Revoke compromised API keys 
- Disable affected IAM user/role 
- Block suspicious IP addresses 
- Terminate active sessions 

---

###  Investigation Continuation

- Deep log review (CloudTrail / Azure Logs) 
- Identify lateral movement attempts 
- Check other affected services 

---

###  Monitoring Enhancements

- Enable anomaly detection 
- Set API usage thresholds 
- Monitor high-risk IAM actions 

---

## Preventive Measures

- Rotate API keys regularly 
- Enforce least privilege access 
- Use temporary credentials (STS) 
- Enable MFA for privileged actions 
- Implement Zero Trust cloud model 

---

## Customer Communication

**Subject:** Cloud Security Alert – Investigation Completed 

Dear [Client 1],

We detected unusual API activity in your cloud environment involving access from an unfamiliar location.

###  Findings:
- Suspicious API calls detected 
- Access patterns deviated from normal baseline 

### Actions Taken:
- Compromised credentials revoked 
- Suspicious sessions terminated 
- Access restricted and secured 

###  Recommendations:
- Rotate API keys regularly 
- Enable MFA for all privileged accounts 
- Monitor cloud activity logs consistently 

We recommend continued monitoring to ensure environment security.

Best regards, 
Cybersecurity Support Team 

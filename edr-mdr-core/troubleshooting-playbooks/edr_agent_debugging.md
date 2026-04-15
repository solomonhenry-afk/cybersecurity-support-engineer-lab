#  EDR Agent Debugging Playbook (Endpoint Troubleshooting)

##  Objective

To provide a structured troubleshooting guide for diagnosing and resolving issues related to EDR agent failures, including offline endpoints, failed installations, and communication breakdowns.

---

##  Common Issues Covered

- Endpoint showing as **Offline**
- Agent not installed correctly
- Agent service not running
- No telemetry/logs being sent
- High CPU usage caused by agent
- Failed updates or corrupted agent

---

##  Step-by-Step Troubleshooting Guide

---

### 1.  Verify Endpoint Status

- Check endpoint in EDR console:
  - Online / Offline status
  - Last check-in time
- Confirm with user:
  - System is powered on
  - Network is active

---

### 2.  Check Network Connectivity

- Test internet access:
  ```bash
  ping google.com
````

* Verify DNS resolution:

  ```bash
  nslookup edr-server.com
  ```
* Ensure required ports are open (e.g., 443, 8443)
* Check firewall/proxy restrictions

---

### 3.  Validate Agent Service Status

#### On Linux:

```bash
systemctl status edr-agent
```

#### On Windows:

* Open Services (`services.msc`)
* Locate EDR Agent Service
* Check if:

  * Running
  * Set to Automatic

---

### 4.  Restart Agent Service

```bash
systemctl restart edr-agent
```

OR restart via Windows Services

* Re-check EDR console for status update

---

### 5.  Review Agent Logs

#### Common log locations:

* Linux:

  ```
  /var/log/edr-agent.log
  ```

* Windows:

  ```
  C:\ProgramData\EDR\logs\
  ```

#### Look for:

* Connection errors
* Authentication failures
* Update failures
* Dependency issues

---

### 6.  Check Agent Version

* Verify installed version:

  ```bash
  edr-agent --version
  ```
* Compare with latest supported version
* Identify compatibility issues with OS updates

---

### 7.  Reinstall Agent (If Needed)

* Uninstall existing agent
* Download latest version
* Reinstall with correct configuration
* Re-register endpoint with EDR console

---

### 8.  Validate Communication with EDR Server

* Ensure endpoint can reach:

  * EDR cloud servers
  * Update servers
* Test HTTPS connectivity:

  ```bash
  curl https://edr-server.com
  ```

---

### 9.  Performance Check (High CPU Issue)

* Identify resource usage:

  ```bash
  top
  ```
* Check if EDR agent is consuming excessive CPU
* Adjust scanning policies if needed

---

## Preventive Best Practices

* Enable automated agent health monitoring
* Schedule regular agent updates
* Standardize firewall and proxy configurations
* Maintain compatibility matrix for OS and agent versions
* Monitor agent performance metrics

---

##  Escalation Criteria

Escalate to engineering team if:

* Agent repeatedly crashes after reinstall
* Persistent communication failure
* Unknown errors in logs
* Suspected software bug

---

##  Customer Communication Template

**Subject:** EDR Agent Issue – Investigation in Progress

Dear Client 1,

We are currently investigating the issue affecting your endpoint’s security agent. Initial checks indicate a potential service or connectivity issue.

We are working to restore full functionality and will keep you updated shortly.

Thank you for your patience.

Best regards,
Cybersecurity Support Team

---

##  Skills Demonstrated

* Endpoint Troubleshooting
* EDR Agent Debugging
* Network Diagnostics
* Log Analysis
* Root Cause Identification
* Customer Support & Communication
* System Recovery Procedures

---


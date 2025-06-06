# VPN-Privacy-Lab

A hands-on exploration of VPNs, their effects on network behavior, and enhancements for anonymity and security online.

## 📌 Overview

This project involves setting up a VPN using **ProtonVPN (Free)** and performing a series of tests and enhancements to understand how VPNs affect IP addresses, DNS leaks, internet speed, browser fingerprinting, and more. It includes Python scripting and research-based visualization to reinforce learning.

---

## 🧪 Steps Followed

### ✅ STEP 1: Installed ProtonVPN
- Created a free account and installed the desktop client.
- Successfully signed in and prepared for testing.

### ✅ STEP 2: Connected to VPN Server
- Chose a server (e.g., Netherlands).
- Verified connection with **“Connected”** status.
- 📸 *Screenshot:* `vpn_connected.png`

### ✅ STEP 3: Checked IP Before & After VPN
- Visited [whatismyipaddress.com](https://whatismyipaddress.com)
- Captured public IP before and after connecting to VPN.
- 📸 *Screenshots:* `ip_before.png`, `ip_after.png`

### ✅ STEP 4: Ran Internet Speed Test
- Used [speedtest.net](https://speedtest.net)
- Compared internet speeds with and without VPN.
- 📸 *Screenshots:* `speedtest_before.png`, `speedtest_after.png`

### ✅ STEP 5: Performed DNS Leak Test
- Used [dnsleaktest.com](https://dnsleaktest.com)
- Confirmed that **DNS is not leaking**.
- 📸 *Screenshot:* `dns_leak.png`

### ✅ STEP 6: Browser Fingerprint Analysis
- Used [Cover Your Tracks](https://coveryourtracks.eff.org)
- Tested browser fingerprint before and after VPN connection.
- 📸 *Screenshots:* `fingerprint_before.png`, `fingerprint_after.png`

---

### 7. **Python Script: IP Checker**

Created a script `check_ip.py` to check the current external IP address programmatically:
```python
import requests
ip = requests.get("https://api64.ipify.org?format=json").json()
print(f"Your current IP: {ip['ip']}")
```
✅ File: `check_ip.py`

---

### 8. **VPN Tunneling Protocol Diagram**

Illustrated how VPN protocols (**OpenVPN**, **WireGuard**, **IKEv2/IPSec**) secure internet traffic  
✅ Image: `vpn_tunnel_diagram.png`

---

### 9. **Real-World VPN Use Cases**

Saved as `real_world_use_cases.md`, includes:

- **How journalists use VPNs to evade censorship**
- **How VPNs allow streaming geo-blocked content**

---

## 🔍 Key Observations

- **IP Masking:** VPN effectively masked the original IP address.
- **Speed Drop:** A moderate decrease in download/upload speeds was noted while using the VPN.
- **DNS Leak:** No DNS leaks occurred, verifying a secure tunnel.
- **Browser Fingerprint:** Some elements of the fingerprint changed, enhancing privacy but not fully anonymizing the browser.
- **Script Utility:** Python script simplifies automated IP checking.

---

## 💡 Unique Enhancements Summary

1. **Speed Test Comparison (Before/After)**
2. **DNS Leak Analysis**
3. **Browser Fingerprinting Review**
4. **Python IP Checker Script**
5. **VPN Tunnel Protocol Diagram**
6. **Real-World Use Cases**

---

## ✅ Conclusion

This project demonstrates how VPNs enhance privacy and security while offering valuable real-world applications. The steps and enhancements show how users can independently evaluate the effectiveness of a VPN beyond just IP masking.

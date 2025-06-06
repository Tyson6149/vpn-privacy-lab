# vpn-privacy-lab
Hands-on cybersecurity project exploring VPNs, encryption, tunneling protocols, and internet privacy through real-world testing and analysis.
# VPN-Privacy-Lab

This project demonstrates the practical use of a VPN (Virtual Private Network) using ProtonVPN along with several unique privacy and security enhancement tests. It includes visual evidence, a custom Python script, and real-world use cases to highlight how VPNs improve digital privacy.

## ✅ Steps Followed

### 1. **Installed ProtonVPN**
- Created a free account at [ProtonVPN](https://protonvpn.com/free-vpn)
- Installed the desktop client
- Successfully signed in and launched the application

### 2. **Connected to VPN Server**
- Connected to a ProtonVPN server using the "Quick Connect" feature  
- ✅ Screenshot: `vpn_connected.png`

### 3. **Checked IP Address (Before & After VPN)**
- Visited [WhatIsMyIPAddress](https://whatismyipaddress.com)
- ✅ `ip_before.png` – real IP without VPN  
- ✅ `ip_after.png` – masked IP after VPN connection

### 4. **Speed Test Analysis**
- Ran internet speed tests via [Speedtest.net](https://speedtest.net)
- ✅ `speedtest_before.png` – speed without VPN  
- ✅ `speedtest_after.png` – speed with VPN  
- Observed minor latency and bandwidth variation due to tunneling

### 5. **DNS Leak Test**
- Used [DNSLeakTest.com](https://dnsleaktest.com) while VPN was connected
- ✅ `dns_leak.png` confirms no DNS leak occurred

### 6. **Browser Fingerprint Test**
- Conducted fingerprinting test at [Cover Your Tracks](https://coveryourtracks.eff.org)
- ✅ `fingerprint_before.png` – fingerprint before VPN  
- ✅ `fingerprint_after.png` – fingerprint after VPN  
- Result: Browser fingerprint changed, improving anonymity

### 7. **Python Script: IP Checker**
Created a script `check_ip.py` to check the current external IP address programmatically:
```python
import requests
ip = requests.get("https://api64.ipify.org?format=json").json()
print(f"Your current IP: {ip['ip']}")
-💾 File: check_ip.py

### 8. **VPN Tunneling Protocol Diagram**
Illustrated how VPN protocols (OpenVPN, WireGuard, IKEv2/IPSec) secure internet traffic

✅ Image: vpn_tunnel_diagram.png

### 9. **Real-World VPN Use Cases**
Saved as real_world_use_cases.md, includes:

How journalists use VPNs to evade censorship

How VPNs allow streaming geo-blocked content


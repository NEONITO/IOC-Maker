# NEONITO IOC Conversion Script

This script enhances IOC processing by automating tasks such as defanging IP addresses and URL, accurately identifying hash types, and delivering a succinct summary, even when duplicates are present

- **Defang URLs:** Converts URLs to a defanged format for safe handling.

- **Defang IPs:** Enhances readability of IP addresses without altering their functionality.

- **Identify Hash Type:** Recognizes and labels the type of hash (MD5, SHA-1, SHA-256).

- **Generate Summary:** Produces a concise summary of unique URLs, IPs, and hash values.

# How to use 

Prepare Your IOC Data:

- **Create a text file IOC.txt containing your IOC data, including IP , URL , and hash**
- **run scirpt python ioc-neonito.py**

# Result 

Example IOC Data:
- **127.0.0.1**
- **http://example.com**
- **9a4fda54a2abebe4a90935f3f0b44902606ccb79fadba8349853daac6841e2ad**

IOC Result:
- **hxxps[:]//example[.]com**
- **127[.]0[.]0[.]1**
- **9a4fda54a2abebe4a90935f3f0b44902606ccb79fadba8349853daac6841e2ad - SHA-256**


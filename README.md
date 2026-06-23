# Python Subdomain Enumerator

## Overview

This repository contains a multithreaded Python-based Subdomain Enumeration tool designed to identify valid subdomains for a target domain using a wordlist and concurrent HTTP requests.

## Features

* HTTPS connectivity testing
* Status code validation
* Custom wordlist support
* Simple command-line interface

## Requirements

* Python 3.x
* requests library

## Usage

Place your subdomain wordlist in the project directory and run:

```bash
python subdomain_enum.py
```

Enter the target domain when prompted:

```bash
google.com
```

Example Output:

```bash
[+] Subdomain Discovered ----------> mail.google.com [Status: 200]
[+] Subdomain Discovered ----------> docs.google.com [Status: 200]

[*] Done! Found 2 subdomains.
```

## Skills Demonstrated

* Python Programming
* Reconnaissance Automation
* Security Tool Development

## Disclaimer

This tool is intended for educational, research, and authorized security testing purposes only. Users are responsible for complying with applicable laws and obtaining proper authorization before testing any target systems.

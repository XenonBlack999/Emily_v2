# Emily v2 --- Advanced AI Assistant for Cybersecurity (Free Version)

## Overview

Emily v2 is an enhanced Python-based cybersecurity assistant designed to
support penetration testers, students, and professionals by automating
essential security analysis tasks.

This upgraded version introduces: - Level-2 Vice Command System -
Extensible module-based scanning - Smarter suggestions for tools &
engines

Emily v2 helps users: - Scan websites for basic vulnerabilities -
Identify open ports & exposed services - Recommend tools based on scan
results - Learn cybersecurity workflows with simple explanations

Suitable for: - Beginner penetration testers - Students learning ethical
hacking - Cybersecurity enthusiasts - Developers automating basic
security checks

------------------------------------------------------------------------

## Level-2 Vice Command System

Emily v2 introduces a Vice Command System, which gives the user a more
structured and powerful way to interact with the assistant.

### Available Vice Commands

  -----------------------------------------------------------------------
  Command                     Description
  --------------------------- -------------------------------------------
  scan `<target>`{=html}      Scans the website or IP for ports & basic
                              vulnerabilities

  tools `<target>`{=html}     Suggests the best penetration testing tools
                              for this target

  report `<target>`{=html}    Generates a human-readable scan report

  help                        Shows available commands

  exit                        Closes the assistant
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Features

### 🔍 Website Scanner

-   Detects:
    -   Open ports
    -   Running services
    -   Banner grabbing
    -   Basic misconfigurations

### 🛠 Pen-Testing Engine Suggestions

Based on findings, Emily recommends: - Nmap - Nikto - OWASP ZAP -
Gobuster/Dirbuster - WafW00f - WhatWeb - SSLScan

### 👶 Beginner-Friendly Output

-   Clear explanation of each finding\
-   No confusing jargon

### 🔧 Extensible Architecture

-   Add modules
-   Integrate APIs
-   Upgrade engines easily

------------------------------------------------------------------------

## Requirements

-   Python 3.10+

-   Required Python packages:

        pip install python-nmap
        pip install requests
        pip install rich

------------------------------------------------------------------------

## Installation

1.  Clone the repository:

        git clone https://github.com/XenonBlack999/Emily_v2.git

2.  Navigate into the project folder:

        cd Emily_v2

3.  Install dependencies:

        pip install -r requirements.txt

------------------------------------------------------------------------

## Usage

Start Emily v2:

    python3 emily.py

Then use the vice commands:

    scan example.com
    tools example.com
    report example.com
    help
    exit

------------------------------------------------------------------------

## Project Structure

    Emily_v2/
    │── emily.py
    │── scanner/
    │── engines/
    │── reports/
    │── utils/
    │── README.md
    │── requirements.txt

------------------------------------------------------------------------

## Future Updates

-   API-based vulnerability database
-   CVE auto-matching\
-   Web UI dashboard\
-   Mobile companion app\
-   SQLi/XSS simulation engine\
-   Full automation mode

------------------------------------------------------------------------

## Disclaimer

This tool is intended for educational purposes and legal penetration
testing only.

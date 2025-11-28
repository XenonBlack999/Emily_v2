# -*- coding: utf-8 -*-
#browsing and installation unit 



import webbrowser
import os
import time


# Browsing section
def youtube():
    print("We are now starting to browse YouTube")
    os.system("firefox https://youtube.com/")

    



def osintframe():
    print("We are now starting to browse OSINT Framework")
    os.system("firefox https://osintframework.com/")




def dnslookup():
    print("We are now starting to browse DNS Lookup")
    os.system("firefox https://www.nslookup.io/")




def waybackmachine():
    print("We are now starting to browse Wayback Machine")
    os.system("firefox https://web.archive.org/")



def ip2location():
    print("We are now starting to browse IP2Location")
    os.system("firefox https://ip2location.com")




def rdpguard():
    print("We are now starting to browse RDPGuard")
    os.system("firefox https://rdpguard.com")




def hackergpt():
    print("We are now starting to browse Hacker GPT")
    os.system("firefox https://chat.hackerai.co/")


def wiki():
    print("We are now starting to browse Wikipedia")
    os.system("firefox https://en.wikipedia.org")

    
    

def panzer():
    print("We are now starting to browse PanzerRush Game")
    os.system("firefox https://www.panzerrush.com/?e=1")




def bmi():
    print("We are now starting to browse Microsoft Bin")
    os.system("firefox messenger.microsoft.com/")




def updater():
    log_action("Updating system")
    print("Now! We will update")
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system('clear')

 
    
 
def python3_error():
    os.system('sudo apt install python3-venv')
    os.system('python3 -m venv path/to/venv')
    os.system('source path/to/venv/bin/activate')
    print("Now ready to use!")

    
    


# Install section
def virtualbox_install():
    os.system("sudo apt update")
    os.system("sudo apt install virtualbox -y")
    os.system("sudo apt install virtualbox-dkms")
    os.system("sudo apt full-upgrade -y")
    os.system("sudo apt install build-essential dkms linux-headers-$(uname -r)")
    print("We installed VirtualBox on your Linux system")
    print("We will reboot")
    time.sleep(3)
    os.system("sudo apt purge virtualbox -y && reboot")




def telegram_install():
    print("You need to browse and download the file")
    print("We will start browsing the Telegram download website")
    os.system("firefox https://desktop.telegram.org/")



def spyder_install():
    print("Now! We will install Python Spyder")
    os.system("sudo apt install spyder")



def code_installer():
    print("Now! We will install Code-OS")
    os.system("sudo apt install code-os")



def rise_installer():
    print("Now! We will install Rise-UP VPN")
    os.system("sudo apt install rise-up")



def vlc_installer():
    print("Now! We will install VLC-bin")
    os.system("sudo apt install vlc-bin")
    
    
#Browsing Service 
#penetration search engine and other lis
def pentest_list():
    # List of services categorized by type
    services = [
        {
            "Category": "Search Engine",
            "Name": "Shodan",
            "URL": "https://www.shodan.io"
        },
        {
            "Category": "Search Engine",
            "Name": "Censys",
            "URL": "https://censys.com/"
        },
        {
            "Category": "Search Engine",
            "Name": "Onyphe",
            "URL": "https://www.onyphe.io/"
        },
        {
            "Category": "Search Engine",
            "Name": "Bin",
            "URL": "https://messenger.microsoft.com"
        },
        {
            "Category": "Search Engine",
            "Name": "ZoomEye",
            "URL": "https://www.zoomeye.hk/"
        },
        {
            "Category": "Search Engine",
            "Name": "Binary Edge",
            "URL": "https://www.binaryedge.io/"
        },
        {
            "Category": "Search Engine",
            "Name": "Wigle",
            "URL": "https://wigle.net/"
        },
        {
            "Category": "Search Engine",
            "Name": "Pulsedive",
            "URL": "www.pulsedive.com"
        },
        {
            "Category": "Search Engine",
            "Name": "Binary Edge",
            "URL": "www.binaryedge.io"
        },
        {
            "Category": "Search Engine",
            "Name": "Sherlock Doc",
            "URL": "https://sherlock-linux.org/en/documentation/"
        },

        {
            "Category": "Search Engine",
            "Name": "BuiltWith",
            "URL": "https://builtwith.com/"
        },
        {
            "Category": "Search Engine",
            "Name": "Public WWW",
            "URL": "https://publicwww.com/"
        },
        {
            "Category": "Threat Intelligence",
            "Name": "Pulsedive",
            "URL": "https://pulsedive.com/"
        },
        {
            "Category": "Threat Intelligence",
            "Name": "Urlscan",
            "URL": "https://urlscan.io/"
        },
        {
            "Category": "Vulnerabilities",
            "Name": "Vulners",
            "URL": "https://vulners.com/"
        },
        {
            "Category": "Virus Scan",
            "Name": "VirusTotal",
            "URL": "https://www.virustotal.com"
        },
        {
            "Category": "Virus Scan",
            "Name": "Jotti's Virus Scan",
            "URL": "https://virusscan.jotti.org/it"
        },
        {
            "Category": "IP Lookup",
            "Name": "What is My IP",
            "URL": "https://whatismyip.com/"
        },
        {
            "Category": "IP Lookup",
            "Name": "What's Their IP",
            "URL": "https://whatstheirip.com/"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Intelligence X",
            "URL": "https://intelx.io"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Leakcheck",
            "URL": "https://leakcheck.io"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "We Leak Info",
            "URL": "https://weleakinfo.to"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Leak Peek",
            "URL": "https://leakpeek.com"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Snusbase",
            "URL": "https://snusbase.com"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Leakedsource",
            "URL": "https://wikileaks.org"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "GlobelLeaks",
            "URL": "https://globaleaks.org"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Firefox Monitor",
            "URL": "https://monitor.firefox.com"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Breach Alarm",
            "URL": "https://breachalarm.com"
        }
    ]
    
    
    
    print("\n")
    for service in services:
        print(f"{service['Category']:20} | {service['Name']:20} | {service['URL']}")
        

    def browse_service():
        print("\n")
        response = input("Emily:Do you want to browse? (yes/no): ").strip().lower()
        if response == "yes":
            service_name = input("Emily:Type the website name: ").strip()
            for service in services:
                if service['Name'].lower() == service_name.lower():
                    print(f"Opening {service['Name']} at {service['URL']}")
                    webbrowser.open(service['URL'])
                    return
            print("Emily:Sorry, the service you entered is not in the list.")
        else:
            print("Emily:Okay, have a nice day!")


    browse_service()
    
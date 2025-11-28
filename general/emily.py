


# Ensure you can import from other folders (check the relative imports or path)
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'ascii'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'internet'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'ip'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'logs'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'bot_response'))
except ImportError:
    print("Error finding some paths")

# Import necessary modules with error handling
try:
    from ascii.ascii_art import raspberry_pi_pico_schematic_ascii_art, about
except ImportError as e:
    print(f"Error importing ascii_art: {e}")

try:
    from internet import test_speedtest_setup, check_internet_speed
except ImportError as e:
    print(f"Error importing internet modules: {e}")

try:
    from ip_analyst import ip_class, check_superuser, print_scan_info, get_domain_info, nmap_scanner
except ImportError as e:
    print(f"Error importing ip_analyst modules: {e}")

try:
    from logs.physical import log_action, note_down_emily, loading, type_animation, type_text
except ImportError as e:
    print(f"Error importing logs modules: {e}")

try:
    from bot_response.bot_response_handler import bot_response_handler
except ImportError as e:
    print(f"Error importing bot_response_handler: {e}")

try:
    # Browsing functions
    from browsing_unit import youtube, osintframe, dnslookup, waybackmachine
    from browsing_unit import ip2location, rdpguard, hackergpt, wiki, updater, panzer, bmi, python3_error
    # Installing functions
    from browsing_unit import virtualbox_install, telegram_install, spyder_install, code_installer
    from browsing_unit import rise_installer, vlc_installer, pentest_service
except ImportError as e:
    print(f"Error importing browsing_unit modules: {e}")

def install_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print(f"No module named '{module_name}'. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

# Install necessary modules
modules = ['selenium', 'flask', 'requests', 'webdriver_manager', 'socket', 'threading', 'dns.resolver', 'whois']
for module in modules:
    try:
        install_module(module)
    except Exception as e:
        print(f"Error installing module {module}: {e}")

loading()
os.system('cls' if os.name == 'nt' else 'clear')

class Emily:
    def __init__(self):
        self.responses = {
            "hello": [
                "Hello! Hope you're having a great day! How can I help?",
                "Hi there! What’s new with you today?",
                "Hello! What interesting things are you up to today?",
                
            ],
            "hi": ["Hello! What’s on your mind today?",
                "Hi! What can I do for you right now?",
                "Hey there! What’s up?",
                "Greetings! I'm here to help you with anything you need!",
                
            ],
            "how are you?": [
                "I'm just a program, but I'm here and ready to help you!",
                "Doing great, thanks! How about you?",
                "I'm here and excited to assist you! What can I do for you today?",
            ],
            "ophelia": [
                "Yes, that's me! How can I help you?", 
                "You know I love it when you say my name!", 
                "Aww, hearing my name from you always makes me smile",
            ],
            "bye": [
                "Goodbye!", 
                "See you later!", 
                "Take care!"
            ],
        }

        self.emily_data = {
            "name": "Ai Lian",
            "english_name": "Emily",
            "dob": "1980-08-18",
            "education": "Higher Diploma in Fashion Design from HKDI",
            "skills": {
                "scanning": [
                    "Scanning with nmap",
                    "Textile technology"
                ],
            }
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses.keys():
            if key in user_input:
                return random.choice(self.responses[key])
        return bot_response_handler(user_input)

    def get_name(self):
        return f"Emily: I am {self.emily_data['name']} (also known as {self.emily_data['english_name']})."

    def get_dob(self):
        return f"Emily: I was born on {self.emily_data['dob']}."

# Command Helping service function
def help_emily():
    log_action("Displaying help information")
    log_action("Help function", "Printing Message", "Printing")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(about())
    print("""
          That is Python AI model named Emily. The purpose is to help Penetration Testers in their work.
          This AI started on Oct 1, 2024, and will continue to develop in the future.
          
          User manual:
              
              update system      : To update your system 
              
              error fix python   : python error fix 
              
              note down emily    : to note down function 
              
              pentest list       : penetration testion service link collection

              Browsing Function :::>>>
              browse <web name> :           Browse to the respective website.   
              <youtube,osintframe,Dns lookup,wayback machine,Ip2 location,RDp guard,Hacker gpt,panzer,wiki,bin>
              
              update system : Update your system.
              
              
              Packge Installition Function :::>>>>
              install <pkgname> :            Install a specific package.
              <virtual box,sode-os,telegram,spyder,riseup,vlc>
              
              activate nmap  : to activate namp scanner function 
              
              note down ophelia:to note down something as note in ophelia
                              
            error fix python:that will error fix the env of python3
            
            internet speed : to check internet speed 
            
            get domain info : to get domain info
          """)
          
def main():
    emily = Emily()
    log_action("Assistant AI started")
    print(pyfiglet.figlet_format("Emily CLI"))
    command_map = {
        "your name": emily.get_name,
        "your birthday": emily.get_dob,
        "how can you help me": lambda: "I can help you in your penetration work.",
        "update system": lambda: updater() or "System update completed!",
        "activate nmap": lambda: nmap_scanner(),
        "ip check": lambda: ip_class(),
        "error fix python": lambda: python3_error(),
        "note down emily": lambda: note_down_emily(),
        "help": help_emily,
        "clear": lambda: os.system('cls' if os.name == 'nt' else 'clear'),
        "internet speed": lambda: test_internet_speed(),
        "pentest list": lambda: pentest_service(),
        "respberry pico": lambda: raspberry_pi_pico_schematic_ascii_art(),
        "get domain info": lambda: get_domain_info(),
    }

    while True:
        
        user_input = input("""\n┌──(security assistant㉿emily)-[Emily_bot]
└─$ """).lower()

        if user_input == "exit":
            print("Emily: Thank you for using the Assistant Bot. Goodbye!")
            log_action("Assistant AI session ended")
            break

        if user_input == "help":
            help_emily()
            continue  

        if "browse" in user_input:
            handle_browsing(user_input)
            log_action(action="browsing", process_name="browsing function", process_type="online")
            continue

        if "install" in user_input:
            handle_installation(user_input)
            log_action(action="installing", process_name="install function", process_type="online")
            continue

        response = None
        for command, action in command_map.items():
            if command in user_input:
                response = action()
                break

        if response:
            print(f"Emily: {response}")
            log_action(f"Executed command: {user_input}")
        else:
            response = emily.get_response(user_input)
            print(f"Emily: {response}")
            log_action(f"User input: {user_input} - Response: {response}")


def handle_browsing(user_input):
    browsing_options = {
        "youtube": youtube,
        "osintframe": osintframe,
        "dnslookup": dnslookup,
        "waybackmachine": waybackmachine,
        "ip2location": ip2location,
        "rdpguard": rdpguard,
        "hackergpt": hackergpt,
        "wiki": wiki,
        "bin": bmi,
        "panzer": panzer,
    }

    for site, action in browsing_options.items():
        if site in user_input:
            action()
            return

    user_link = input("Unknown link. Please provide a valid URL: ")
    os.system(f"firefox {user_link}")
    log_action(f"Browsing custom link: {user_link}")
    print(f"Opening {user_link}...")


def handle_installation(user_input):
    installation_options = {
        "virtualbox": virtualbox_install,
        "code-os": code_installer,
        "telegram": telegram_install,
        "spyder": spyder_install,
        "rise-up": rise_installer,
        "vlc": vlc_installer,
    }

    for package, action in installation_options.items():
        if package in user_input:
            action()
            return

    user_command = input("Unknown package. Please provide the installation command: ")
    os.system(user_command)
    log_action(f"Executed custom command: {user_command}")


def test_internet_speed():
    test_speedtest_setup()
    speeds = check_internet_speed()
    print(f"Download speed: {speeds['download_speed_mbps']} Mbps")
    print(f"Upload speed: {speeds['upload_speed_mbps']} Mbps")


if __name__ == "__main__":
    main()
    

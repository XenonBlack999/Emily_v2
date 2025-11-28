#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Emily Assistant (CLI + Voice)
Created on Oct 1 14:46:30 2024
Author: bytechef
"""

import os
import sys
import time
import platform
import datetime
import smtplib
import importlib
import importlib.util
from typing import Dict, List, Tuple





# ===================== STRICT MODE CONFIG =====================
STRICT_LOCAL_MODULES = True            # require local packages/symbols below
STRICT_VOICE_IF_CHOSEN = True          # if Voice Mode, require SpeechRecognition + mic
LOCAL_PKGS = ["ascii", "internet", "ip", "logs", "bot_response", "browsing"]





# Required symbols that MUST exist in your local modules (no stubs allowed)
REQUIRED_SYMBOLS: Dict[str, List[str]] = {
    "ascii.ascii_art": ["raspberry_pi_pico_schematic_ascii_art", "about"],
    "internet": ["test_speedtest_setup", "check_internet_speed"],
    "ip_analyst": ["ip_class", "check_superuser", "print_scan_info", "get_domain_info", "nmap_scanner"],
    "logs.physical": ["note_down_emily", "loading", "type_animation", "type_text"],
    "bot_response.bot_response_handler": ["bot_response_handler"],

    "browsing.browsing_unit": [
        # Browsing
        "youtube", "osintframe", "dnslookup", "waybackmachine", "ip2location",
        "rdpguard", "hackergpt", "wiki", "panzer", "bmi",
        # Maintenance
        "updater", "python3_error",
        # Installers
        "virtualbox_install", "telegram_install", "spyder_install", "code_installer",
        "rise_installer", "vlc_installer",
        # Lists
        "pentest_list"
    ],
}


def _project_root() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def _ensure_local_paths():
    base = _project_root()
    for p in LOCAL_PKGS:
        path = os.path.join(base, p)
        if path not in sys.path:
            sys.path.append(path)

def _find_spec_or_reason(modname: str) -> Tuple[bool, str]:
    spec = importlib.util.find_spec(modname)
    if spec is not None:
        return True, ""
    parts = modname.split(".")
    base_path = _project_root()
    guess = os.path.join(base_path, *parts[:-1])
    return False, (f"Module '{modname}' not found. Ensure it's on sys.path and directory exists: "
                   f"{guess}/ (with __init__.py if a package).")

def _preflight_import(modname: str):
    ok, reason = _find_spec_or_reason(modname)
    if not ok:
        raise ImportError(reason)
    try:
        return importlib.import_module(modname)
    except Exception as e:
        raise ImportError(f"Failed importing '{modname}': {e}") from e

def _check_symbols(modname: str, symbols: List[str]):
    mod = _preflight_import(modname)
    missing = [s for s in symbols if not hasattr(mod, s)]
    if missing:
        raise ImportError(f"Module '{modname}' missing symbols: {', '.join(missing)}")
    return mod

def preflight_or_die(require_voice: bool = False):
    _ensure_local_paths()

    problems: List[str] = []
    for modname, symbols in REQUIRED_SYMBOLS.items():
        try:
            _check_symbols(modname, symbols)
        except Exception as e:
            problems.append(str(e))

    if require_voice:
        try:
            import speech_recognition as _sr
        except Exception as e:
            problems.append(f"Voice mode requires SpeechRecognition: {e}")
        else:
            try:
                r = _sr.Recognizer()
                with _sr.Microphone() as _:
                    pass
            except Exception as e:
                problems.append(f"Microphone not accessible: {e}")

    if problems:
        print("\n[PRE-FLIGHT CHECK FAILED]")
        for i, p in enumerate(problems, 1):
            print(f"{i}. {p}")
        print("\nFix the above issues and run again. Strict mode is on.")
        sys.exit(2)







# ---------- Optional external libs (not enforced unless Voice Mode is chosen) ----------
def _safe_import(name):
    try:
        return importlib.import_module(name)
    except Exception:
        return None

pyttsx3 = _safe_import("pyttsx3")
wikipedia = _safe_import("wikipedia")
sr = _safe_import("speech_recognition")
pyfiglet = _safe_import("pyfiglet")




# ---------- Voice/Audio configuration ----------
LANG = "en-US"
PAUSE = 0.7
PHRASE_LIMIT = 30
TIMEOUT = 15





# ---------- Text-to-Speech ----------
_engine = None
def _init_tts():
    global _engine
    if _engine is None and pyttsx3:
        try:
            _engine = pyttsx3.init()
        except Exception as e:
            print(f"[warn] TTS init failed: {e}")
    return _engine

def speak(text: str):
    if not text:
        return
    eng = _init_tts()
    if eng:
        try:
            eng.setProperty("rate", 160)
            voices = eng.getProperty("voices")
            for v in voices:
                name = (getattr(v, "name", "") or "").lower()
                if "female" in name or "zira" in name:
                    eng.setProperty("voice", v.id)
                    break
            eng.say(text)
            eng.runAndWait()
        except Exception as e:
            print(f"[warn] TTS speak failed: {e}")
            print(f"[speak] {text}")
    else:
        print(f"[speak] {text}")

def tell():
    try:
        user_text = input("Input your string: ").strip()
    except Exception:
        user_text = ""
    if user_text:
        speak(user_text)





# ---------- Voice I/O ----------
def takeCommand() -> str:
    if not sr:
        print("[error] SpeechRecognition module not found.")
        return "none"

    r = sr.Recognizer()
    r.pause_threshold = PAUSE
    r.dynamic_energy_threshold = True

    try:
        with sr.Microphone() as source:
            print("[info] Calibrating mic for ambient noise...")
            try:
                r.adjust_for_ambient_noise(source, duration=0.8)
            except Exception as e:
                print(f"[warn] Ambient noise calibration failed: {e}")

            print("[info] Listening...")
            try:
                audio = r.listen(source, timeout=TIMEOUT, phrase_time_limit=PHRASE_LIMIT)
            except sr.WaitTimeoutError:
                print("[error] Timeout: No speech detected within limit.")
                return "none"
            except Exception as e:
                print(f"[error] Listening failed: {e}")
                return "none"

        print("[info] Recognizing speech...")
        try:
            query = r.recognize_google(audio, language=LANG)
            print(f"[success] User said: {query}")
            return query.lower().strip()
        except sr.UnknownValueError:
            print("[error] Could not understand the audio (speech unclear).")
            return "none"
        except sr.RequestError as e:
            print(f"[error] Could not connect to Google API: {e}")
            return "none"
        except Exception as e:
            print(f"[error] Recognition failed: {e}")
            return "none"

    except OSError as e:
        print(f"[error] Microphone not found or not accessible: {e}")
        return "none"
    except Exception as e:
        print(f"[fatal] Unexpected error in takeCommand(): {e}")
        return "none"






# ---------- System helpers ----------
def time_date():
    now = datetime.datetime.now()
    tstr = now.strftime("%I:%M:%S %p")
    speak(f"The current time is {tstr}")
    speak(f"Today's date is {now.day}, month is {now.month}, year is {now.year}")

def shutdown():
    os.system("shutdown /s /t 0" if platform.system() == "Windows" else "shutdown -h now")

def restart():
    os.system("shutdown /r /t 0" if platform.system() == "Windows" else "reboot")

def logout():
    if platform.system() == "Windows":
        os.system("shutdown /l")
    else:
        if os.system("gnome-session-quit --logout --no-prompt") != 0:
            if os.system("pkill -KILL -u \"$USER\"") != 0:
                speak("Logout not supported or failed on this system.")





# ---------- Email (uses env vars) ----------
def sendEmail(to, content):
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    if not EMAIL_USER or not EMAIL_PASS:
        speak("Email credentials not set. Please set EMAIL_USER and EMAIL_PASS environment variables.")
        return
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to, content)
        server.quit()
    except Exception as e:
        speak(f"Email send failed: {e}")





# ---------- Placeholders for local symbols (bound after preflight/imports) ----------
about = None
raspberry_pi_pico_schematic_ascii_art = None
test_speedtest_setup = None
check_internet_speed = None
ip_class = None
check_superuser = None
print_scan_info = None
get_domain_info = None
nmap_scanner = None
note_down_emily = None
loading = None
type_animation = None
type_text = None
bot_response_handler = None

# Optional: browsing_unit symbols (bound after import)
youtube = osintframe = dnslookup = waybackmachine = None
ip2location = rdpguard = hackergpt = wiki = updater = panzer = bmi = python3_error = None
virtualbox_install = telegram_install = spyder_install = code_installer = rise_installer = vlc_installer = pentest_list = None
_BROWSING_ENABLED = False





# ---------- Query processor ----------
def process_query(query: str):
    if not query or query == "none":
        return

    if "time" in query or "date" in query:
        time_date()

    elif ("research" in query) or ("wikipedia" in query):
        if not wikipedia:
            speak("Wikipedia module is not available.")
            return
        speak("Searching Wikipedia...")
        cleaned = query.replace("wikipedia", "").replace("research", "").strip() or "Wikipedia"
        try:
            result = wikipedia.summary(cleaned, sentences=2, auto_suggest=False, redirect=True)
            print(result)
            speak(result)
        except Exception as e:
            emsg = getattr(e, "msg", str(e))
            if "disambiguation" in emsg.lower():
                speak("There are multiple results. Please be more specific.")
            elif "page" in emsg.lower() and "not found" in emsg.lower():
                speak("Sorry, no results found.")
            else:
                speak(f"Something went wrong during the search. {emsg}")

    elif "shutdown" in query and "system" in query:
        shutdown()

    elif "restart" in query and "system" in query:
        restart()

    elif "logout" in query and "system" in query:
        logout()

    elif "send email" in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "xyz@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent.")
        except Exception as e:
            speak("Sorry, I was unable to send the email. " + str(e))

    elif ("offline" in query) or (query in {"quit", "exit"}):
        speak("I am going offline. Good luck!")
        sys.exit(0)

    else:
        resp = bot_response_handler(query)
        speak(resp)




# ---------- Emily smalltalk + data ----------
import random
class Emily:
    def __init__(self):
        self.responses = {
            "hello": [
                "Hello! Hope you're having a great day! How can I help?",
                "Hi there! What’s new with you today?",
                "Hello! What interesting things are you up to today?",
            ],
            "hi": [
                "Hello! What’s on your mind today?",
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
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "clear": ["Clearing the screen!"],
        }

        self.emily_data = {
            "name": "Ai Lian",
            "english_name": "Emily",
            "dob": "1980-08-18",
            "education": "Higher Diploma in Fashion Design from HKDI",
            "skills": {"scanning": ["Scanning with nmap", "Textile technology"]},
        }

    def get_response(self, user_input):
        u = (user_input or "").lower()
        for k in self.responses.keys():
            if k in u:
                response = random.choice(self.responses[k])
                speak(response)
                return response
        response = bot_response_handler(u)
        speak(response)
        return response

    def get_name(self):
        msg = f"I am {self.emily_data['name']} (also known as {self.emily_data['english_name']})."
        speak(msg); return msg

    def get_dob(self):
        msg = f"I was born on {self.emily_data['dob']}."
        speak(msg); return msg






# ---------- CLI helper screens ----------
def help_emily():
    print(r"""
That is Python Bot
Usage: python3 emily.py [command]

User command:

  update system        : To update your system
  error fix python     : Python3 env error fix
  note down emily      : Simple notes
  pentest list         : Penetration testing links


Browsing Function:
  browse <web name>    : youtube, osintframe, dnslookup, waybackmachine,
                         ip2location, rdpguard, hackergpt, wiki, bin, panzer


Package Installation:
  install <pkgname>    : virtualbox, code-os, telegram, spyder, rise-up, vlc


Other:
  activate nmap        : run nmap helper
  internet speed       : run internet speed test
  get domain info      : whois / dns info
""")






# ---------- Handlers ----------
def handle_browsing(user_input):
    if not _BROWSING_ENABLED:
        print("[info] Browsing features are disabled (browsing_unit not available).")
        return
    options = {
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
    for site, action in options.items():
        if site in user_input:
            action()
            return
    user_link = input("Unknown link. Please provide a valid URL: ").strip()
    if user_link:
        os.system(f"firefox '{user_link}' &")
        print(f"Opening {user_link}...")

def handle_installation(user_input):
    if not _BROWSING_ENABLED:
        print("[info] Installer features are disabled (browsing_unit not available).")
        return
    install_map = {
        "virtualbox": virtualbox_install,
        "code-os": code_installer,
        "telegram": telegram_install,
        "spyder": spyder_install,
        "rise-up": rise_installer,
        "vlc": vlc_installer,
    }
    for pkg, action in install_map.items():
        if pkg in user_input:
            action()
            return
    user_cmd = input("Unknown package. Please provide the installation command: ").strip()
    if user_cmd:
        os.system(user_cmd)

def test_internet_speed_cli():
    test_speedtest_setup()
    speeds = check_internet_speed() or {}
    print(f"Download speed: {speeds.get('download_speed_mbps', 0)} Mbps")
    print(f"Upload speed:   {speeds.get('upload_speed_mbps', 0)} Mbps")




# ========================== MAIN ==========================
def _timestamp_prompt() -> str:
    return f"[{datetime.datetime.now().strftime('%H:%M')}][Emily]: "

def main():
    # Choose mode so we know whether to enforce voice deps
    print("Choose mode:")
    print("1. Command Mode")
    print("2. Voice Mode")
    try:
        response = int(input("Please input your command (1/2): ").strip())
    except Exception:
        response = 1

    mode = "voice" if response == 2 else "command"

    if STRICT_LOCAL_MODULES:
        preflight_or_die(require_voice=(STRICT_VOICE_IF_CHOSEN and mode == "voice"))

    # After preflight passes, import/bind required local symbols.
    _ensure_local_paths()

    # ascii
    from ascii.ascii_art import raspberry_pi_pico_schematic_ascii_art as _pico, about as _about
    globals()["raspberry_pi_pico_schematic_ascii_art"] = _pico
    globals()["about"] = _about

    # internet
    from internet import test_speedtest_setup as _tss, check_internet_speed as _cis
    globals()["test_speedtest_setup"] = _tss
    globals()["check_internet_speed"] = _cis

    # ip_analyst
    from ip_analyst import ip_class as _ip_class, check_superuser as _check_superuser, \
        print_scan_info as _print_scan_info, get_domain_info as _get_domain_info, nmap_scanner as _nmap
    globals()["ip_class"] = _ip_class
    globals()["check_superuser"] = _check_superuser
    globals()["print_scan_info"] = _print_scan_info
    globals()["get_domain_info"] = _get_domain_info
    globals()["nmap_scanner"] = _nmap

    # logs.physical (without log_action)
    from logs.physical import note_down_emily as _note, loading as _loading, \
        type_animation as _type_anim, type_text as _type_text
    globals()["note_down_emily"] = _note
    globals()["loading"] = _loading
    globals()["type_animation"] = _type_anim
    globals()["type_text"] = _type_text

    # bot response
    from bot_response.bot_response_handler import bot_response_handler as _brh
    globals()["bot_response_handler"] = _brh

    # Browsing + installers (strict now, but will still try/except for clean error)
    global _BROWSING_ENABLED
    try:
        from browsing.browsing_unit import (
            youtube as _youtube, osintframe as _osintframe, dnslookup as _dnslookup, waybackmachine as _waybackmachine,
            ip2location as _ip2location, rdpguard as _rdpguard, hackergpt as _hackergpt, wiki as _wiki,
            updater as _updater, panzer as _panzer, bmi as _bmi, python3_error as _py3err,
            virtualbox_install as _vbox, telegram_install as _tg, spyder_install as _spyder, code_installer as _code,
            rise_installer as _rise, vlc_installer as _vlc, pentest_list as _pentest_list
        )

        globals()["youtube"] = _youtube
        globals()["osintframe"] = _osintframe
        globals()["dnslookup"] = _dnslookup
        globals()["waybackmachine"] = _waybackmachine
        globals()["ip2location"] = _ip2location
        globals()["rdpguard"] = _rdpguard
        globals()["hackergpt"] = _hackergpt
        globals()["wiki"] = _wiki
        globals()["updater"] = _updater
        globals()["panzer"] = _panzer
        globals()["bmi"] = _bmi
        globals()["python3_error"] = _py3err
        globals()["virtualbox_install"] = _vbox
        globals()["telegram_install"] = _tg
        globals()["spyder_install"] = _spyder
        globals()["code_installer"] = _code
        globals()["rise_installer"] = _rise
        globals()["vlc_installer"] = _vlc
        globals()["pentest_list"] = _pentest_list

        _BROWSING_ENABLED = True
    except Exception as e:
        _BROWSING_ENABLED = False
        print(f"[info] browsing_unit disabled: {e}")

    # Now it's safe to call loading() and render banner
    try:
        loading()
    except Exception:
        print("Loading...")
        time.sleep(0.3)

    os.system('cls' if os.name == 'nt' else 'clear')

    if pyfiglet:
        try:
            print(pyfiglet.figlet_format("Emily AI"))
        except Exception:
            print("=== Emily AI ===")
    else:
        print("=== Emily AI ===")

    emily = Emily()




    # Command map (exact triggers)
    command_map = {
        "your name": emily.get_name,
        "your birthday": emily.get_dob,
        "how can you help me": lambda: "I can help you in your penetration work.",
        "update system": lambda: (
            (updater() or "System update completed!") if _BROWSING_ENABLED else "Updater unavailable."
        ),
        "activate nmap": lambda: (nmap_scanner() or "Nmap helper executed."),
        "ip check": lambda: (ip_class() or "IP check executed."),
        "error fix python": lambda: (
            (python3_error() or "Python error fixer executed.") if _BROWSING_ENABLED else "Python error fixer unavailable."
        ),
        "note down emily": lambda: (note_down_emily() or "Note recorded."),
        "help": lambda: (help_emily() or "Help shown."),
        "clear": lambda: (os.system('cls' if os.name == 'nt' else 'clear') or "Screen cleared."),
        "internet speed": lambda: (test_internet_speed_cli() or "Speed test completed."),
        "pentest list": lambda: (
            (pentest_list() or "Opened pentest list.") if _BROWSING_ENABLED else "Pentest list unavailable."
        ),
        "raspberry pico": lambda: (raspberry_pi_pico_schematic_ascii_art() or "Raspberry Pi Pico schematic shown."),
        "raspberry pi pico": lambda: (raspberry_pi_pico_schematic_ascii_art() or "Raspberry Pi Pico schematic shown."),
        "get domain info": lambda: (get_domain_info() or "Domain info shown."),
    }


    

    print(f"Dear sir, You are now using {mode.capitalize()} Mode")
    speak(f"You are now using {mode} mode")

    while True:
        if mode == "voice":
            query = takeCommand()
            if query == "none":
                continue

            if "command system" in query or "command mode" in query:
                speak("Switching to command mode.")
                mode = "command"
                continue

            handled = False
            for command, action in command_map.items():
                if command in query:
                    handled = True
                    try:
                        res = action()
                    except Exception as e:
                        res = f"Error running '{command}': {e}"
                    if isinstance(res, str) and res.strip():
                        speak(res)
                    break
            if handled:
                continue

            em_resp = emily.get_response(query)
            speak(em_resp)

        else:  # command mode
            try:
                user_input = input(_timestamp_prompt()).strip().lower()
            except EOFError:
                print("\nSession ended.")
                break

            if user_input == "exit":
                print("Emily: Thank you for using the Assistant Bot. Goodbye!")
                break

            if user_input == "help":
                help_emily()
                continue

            if "browse" in user_input:
                handle_browsing(user_input)
                continue

            if "install" in user_input:
                handle_installation(user_input)
                continue

            if "voice system" in user_input or "voice mode" in user_input:
                if STRICT_VOICE_IF_CHOSEN:
                    preflight_or_die(require_voice=True)
                speak("Switching to voice command mode.")
                mode = "voice"
                continue

            # track whether we matched a command, even if it returns None
            handled = False
            response_text = None
            for command, action in command_map.items():
                if command in user_input:
                    handled = True
                    try:
                        out = action()
                    except Exception as e:
                        out = f"Error running '{command}': {e}"
                    if isinstance(out, str) and out.strip():
                        response_text = out
                    break

            if handled:
                if response_text:
                    print(f"Emily: {response_text}")
                continue  # don't fall back to smalltalk

            # Not handled by command_map -> process built-ins or fallback
            if any(k in user_input for k in [
                "time", "date", "wikipedia", "research",
                "shutdown system", "restart system", "logout system",
                "send email", "offline", "quit", "exit"
            ]):
                process_query(user_input)
            else:
                resp = emily.get_response(user_input)
                print(f"Emily: {resp}")



if __name__ == "__main__":
    main()
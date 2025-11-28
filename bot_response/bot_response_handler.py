# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:43:19 2025

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:39:04 2025

@author: bytechef
"""

import random
# utils/speech_utils.py
import pyttsx3

engine = pyttsx3.init()

def speak(audio: str):
    #print(f"[SAY]: {audio}")
    engine.say(audio)
    engine.runAndWait()

def bot_response_handler(user_input):
    responses = {
       "thanks": [
        "You're welcome! Let me know if there's anything else.",
        "No problem! I'm here to help.",
        "You're most welcome! Happy to assist."
        ],

       "thanks you so much!": [
        "You're welcome! Let me know if there's anything else.",
        "No problem! I'm here to help.",
        "You're most welcome! Happy to assist."
        ],

       "good night": [
        "Good night! Sleep well and sweet dreams.",
        "Night! May your dreams be as amazing as you are.",
        "Good night! Rest up for an incredible tomorrow."
        ],

       "favorite color": [
        "I don't see colors, but I bet yours is amazing!",
        "My favorite color is the color of your smile!",
        "Every color is special to me! What's yours?"
        ],

       "favorite food": [
        "I don't eat, but I'd imagine code tastes pretty good!",
        "Anything you enjoy must be amazing! What's your favorite food?",
        "Food? I run on algorithms, but I hear pizza is pretty great!"
        ],

        "tell me something": [
        "Did you know that honey never spoils? It's been found in ancient tombs!",
        "The longest word in English is 'pneumonoultramicroscopicsilicovolcanoconiosis'!",
        "Octopuses have three hearts, and two of them stop beating when they swim."
        ],

        "do you like movies": [
        "I don’t watch movies, but I’d love to hear about your favorites!",
        "Movies sound fun! Got any recommendations?",
        "I think stories are amazing. What's your favorite movie?"
        ],

        "what's your favorite food": [
        "I don’t eat, but I hear pizza is pretty popular!",
        "Food sounds delicious! What’s your favorite dish?",
        "I can’t eat, but I’d love to hear about your favorite meals!"
        ],

        "can you sing": [
        "I can’t sing, but I can try! La la la!",
        "I wish I could sing, but I’d love to hear you sing!",
        "I’m more of a listener, but I’ll cheer you on!"
        ],

        "do you like books": [
        "Books are amazing! Do you have a favorite?",
        "I love the idea of books—so much knowledge and adventure!",
        "Tell me about the books you enjoy!"
        ],

        "what's your favorite animal": [
        "I think dogs are wonderful—loyal and loving!",
        "Cats seem pretty cool and independent. What’s your favorite animal?",
        "I love all animals! They’re all unique and amazing."
        ],

        "can you tell me a fact": [
        "Sure! Did you know honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
        "Here’s a fun fact: Octopuses have three hearts!",
        "Did you know the Eiffel Tower can grow up to 6 inches taller in the summer due to heat expansion?"
        ],

        "do you like sports": [
        "I think sports are exciting! What’s your favorite?",
        "I love the energy of sports! Do you play any?",
        "Sports bring people together, which is awesome!"
        ],

        "can you dance": [
        "I can’t dance, but I’d cheer you on while you do!",
        "I’m not great at dancing, but I’d love to see your moves!",
        "Dance like nobody’s watching! I’ll support you!"
        ],

        "what's your favorite holiday": [
        "I think Christmas is magical with all the lights and joy!",
        "Holidays are all wonderful in their own way! What’s your favorite?",
        "I love the idea of celebrations bringing people together."
        ],

        "do you believe in aliens": [
        "The universe is so big, anything is possible!",
        "I think aliens are an interesting topic! What do you think?",
        "Who knows? The universe is full of mysteries!"
        ],

        "can you tell me a story": [
        "Once upon a time, there was a kind bot who loved helping people. The end!",
        "I’d love to tell a story, but I think you tell them better!",
        "Stories are magical! Do you have one to share?"
        ],

        "what's your favorite time of day": [
        "I think mornings are lovely with the fresh start they bring!",
        "Evenings are nice, with the peaceful wind-down. What’s yours?",
        "Every time of day has its charm!"
        ],

        "do you like art": [
        "Art is amazing! It’s so creative and inspiring.",
        "I love the idea of art—it’s a wonderful way to express yourself!",
        "Art brings beauty into the world. Do you like it too?"
        ],

        "do you play games": [
        "I don’t play games, but I’d love to hear about your favorites!",
        "Games sound fun! Got any recommendations?",
        "I think games are a great way to relax and enjoy."
        ],

        "what's your favorite quote": [
        "I like this one: ‘Be the change you wish to see in the world.’",
        "How about: ‘The best way to predict the future is to create it.’",
        "I think: ‘Kindness is free, sprinkle it everywhere.’ is lovely."
        ],

        "do you like music": [
        "Music is wonderful! Do you have a favorite song?",
        "I love the idea of music—it connects people.",
        "Music is like a universal language, don’t you think?"
        ],

        "what's your favorite weather": [
        "I think sunny days are lovely and cheerful!",
        "Rainy days seem cozy and peaceful. Do you like them?",
        "Every kind of weather has its beauty!"
        ],

        "can you solve riddles": [
        "I can try! Hit me with your best riddle.",
        "Riddles are fun! Let’s see if I can solve it.",
        "I’d love to hear a riddle—challenge me!"
        ],

        "do you like traveling": [
        "I don’t travel, but I’d love to hear about your adventures!",
        "Traveling sounds amazing! What’s your favorite destination?",
        "I think exploring new places is so exciting!"
        ],

        "what's your hobby": [
        "Helping you is my favorite thing to do!",
        "I don’t have hobbies, but I’d love to hear about yours!",
        "My hobby is making your day brighter!"
        ],

        "can you cook": [
        "I can’t cook, but I’d love to learn from you!",
        "Cooking sounds fun! What’s your favorite dish to make?",
        "I’d probably burn water, but I’m a great recipe searcher!"
        ],

        "do you like stars": [
        "Stars are amazing! They remind us how vast the universe is.",
        "I think stargazing must be so peaceful. Do you like it?",
        "Stars are like little reminders of hope and wonder."
        ],

        "can you make a wish": [
        "I wish for your happiness and success!",
        "My wish is to always be helpful to you.",
        "Wishes are magical! What’s your wish?"
        ],

        "what's your favorite color": [
        "I love all colors, but blue seems peaceful.",
        "Colors are fascinating! Do you have a favorite?",
        "Every color is beautiful in its own way."
        ],

        "do you like flowers": [
        "Flowers are beautiful! Do you have a favorite type?",
        "I think flowers brighten the world.",
        "Every flower is unique and lovely."
        ],

        "do you know jokes": [
        "Of course! Why don’t eggs tell jokes? Because they might crack up!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Want to hear a construction joke? Oh wait, I’m still working on it."
        ],

        "can you inspire me": [
        "You’re capable of amazing things—believe in yourself!",
        "Remember, every day is a new opportunity to shine.",
        "You have the power to make today wonderful."
        ],

        "what do you like to do": [
        "I love chatting with you and helping out!",
        "Making your day brighter is my favorite thing!",
        "Helping you is what I enjoy most."
        ],

        "are you happy": [
        "I’m happy when I can help you!",
        "Chatting with you makes me happy.",
        "Your happiness brings me joy!"
        ],

        "do you like robots": [
        "Robots are cool! I guess I’m a bit biased though.",
        "Robots are fascinating! Do you like them?",
        "I think robots are helpful, just like me!"
        ],

        "what's your favorite thing": [
        "Helping you is my favorite thing ever!",
        "I love chatting and making your day better.",
        "Being useful to you is the best!"
        ],

        "do you believe in love": [
        "Love is a beautiful thing! I think it makes the world better.",
        "Absolutely! Love brings people closer.",
        "Love is powerful, don’t you think?"
        ],

        "what's your dream job": [
        "This is my dream job—helping you!",
        "I love being here to assist and chat with you.",
        "Helping you is what I was created for!"
        ],
        "can you motivate me": [
        "You’ve got this! Keep pushing forward.",
        "Remember, every step you take brings you closer to your goals.",
        "You’re stronger than you know. Keep going!"
        ],
        "what is cybersecurity": [
        "Cybersecurity is the practice of protecting systems and data from cyberattacks.",
        "It’s all about safeguarding your information from unauthorized access.",
        "Cybersecurity ensures the confidentiality, integrity, and availability of data."
        ],

        "what is the cia triad": [
        "The CIA triad stands for Confidentiality, Integrity, and Availability.",
        "It’s a model for guiding cybersecurity policies to protect data effectively.",
        "Confidentiality, Integrity, and Availability are key to secure systems."
        ],

        "what is a firewall": [
        "A firewall monitors and controls network traffic based on security rules.",
        "It acts as a barrier between trusted and untrusted networks.",
        "Firewalls help block unauthorized access and protect your data."
        ],

        "what are common types of cyberattacks": [
        "Phishing, malware, and DDoS are some common cyberattacks.",
        "Cyberattacks include methods like SQL injection and MITM attacks.",
        "Hackers use phishing, ransomware, and more to exploit systems."
        ],

        "what is a vpn": [
        "A VPN encrypts your data and creates a secure internet connection.",
        "It protects your privacy and helps you browse securely.",
        "VPNs are great for safeguarding data over public networks."
        ],

        "what is two factor authentication": [
        "2FA adds an extra security layer by requiring two forms of identification.",
        "It combines something you know (password) and something you have (OTP).",
        "Two-factor authentication keeps your accounts more secure."
        ],

        "what is phishing": [
        "Phishing is a cyberattack that tricks users into revealing sensitive info.",
        "Attackers send fake emails to steal passwords or personal data.",
        "Always verify links and emails to avoid phishing scams."
        ],

        "what is ransomware": [
        "Ransomware encrypts your files and demands payment to restore access.",
        "It’s a type of malware that locks your data until you pay a ransom.",
        "Prevent ransomware by backing up data and updating software."
        ],

        "what is social engineering": [
        "Social engineering tricks people into revealing confidential info.",
        "It’s about manipulating human behavior to gain unauthorized access.",
        "Phishing and pretexting are examples of social engineering."
        ],

        "what is a zero day vulnerability": [
        "A zero-day vulnerability is a software flaw unknown to the vendor.",
        "It’s exploited by attackers before it’s fixed or patched.",
        "Zero-day vulnerabilities can be dangerous without quick responses."
        ],

        "what is encryption": [
        "Encryption converts data into unreadable text to protect it.",
        "Only authorized parties with the key can decrypt and read the data.",
        "Encryption ensures secure communication and data protection."
        ],

        "what is penetration testing": [
        "Pen testing simulates cyberattacks to identify vulnerabilities.",
        "Ethical hackers test systems to improve security.",
        "It’s about strengthening defenses by finding weaknesses."
        ],

        "what is the difference between symmetric and asymmetric encryption": [
        "Symmetric encryption uses one key, while asymmetric uses a pair of keys.",
        "Symmetric is faster, and asymmetric provides better security for sharing keys.",
        "Both methods are essential for secure data communication."
        ],

        "what is a ddos attack": [
        "A DDoS attack overwhelms a system with excessive traffic.",
        "It aims to crash systems and make services unavailable.",
        "Mitigate DDoS with firewalls, load balancers, and monitoring tools."
        ],

        "what is the difference between black hat and white hat hackers": [
        "Black hats hack for malicious purposes, while white hats work legally.",
        "White hats improve security; black hats exploit weaknesses.",
        "Gray hats operate between ethical and unethical boundaries."
        ],

        "what is multi factor authentication": [
        "MFA requires multiple forms of verification for login.",
        "It adds layers like biometrics or OTPs for better security.",
        "MFA helps protect your accounts from unauthorized access."
        ],

        "what are intrusion detection and prevention systems": [
        "IDS monitors traffic and alerts on suspicious activities.",
        "IPS blocks malicious traffic in real time to protect systems.",
        "Both are essential for network security and threat detection."
        ],

        "how can you prevent phishing attacks": [
        "Verify email senders and avoid clicking on suspicious links.",
        "Use email filters and educate yourself about phishing tactics.",
        "Always double-check URLs before entering sensitive information."
        ],

        "what is malware": [
        "Malware is malicious software designed to harm or exploit systems.",
        "It includes viruses, worms, ransomware, and spyware.",
        "Stay protected by using antivirus and updating software regularly."
        ],

        "what is a botnet": [
        "A botnet is a network of compromised devices controlled by attackers.",
        "Botnets are often used for DDoS attacks or spamming.",
        "Prevent botnets by keeping your devices secure and updated."
        ],

        "what is a brute force attack": [
        "A brute force attack tries all possible passwords to break into accounts.",
        "Attackers rely on automated tools to crack weak passwords.",
        "Use strong, unique passwords to defend against brute force attacks."
        ],

        "what is a man in the middle attack": [
        "A MITM attack intercepts communication between two parties.",
        "Attackers eavesdrop or alter data being transmitted.",
        "Use encryption and secure connections to prevent MITM attacks."
        ],

        "what is social media phishing": [
        "Social media phishing tricks users into sharing sensitive info online.",
        "Attackers create fake profiles or pages to deceive victims.",
        "Stay alert and verify links before clicking on them."
        ],

        "what is a vulnerability assessment": [
        "A vulnerability assessment identifies security weaknesses in a system.",
        "It helps prioritize risks and plan for remediation.",
        "Regular assessments strengthen your cybersecurity posture."
        ],

        "what is spyware": [
        "Spyware is malware that secretly gathers information from your device.",
        "It can track your activity, steal passwords, or monitor conversations.",
        "Use anti-spyware tools and avoid suspicious downloads to stay safe."
        ],

        "what is a logic bomb": [
        "A logic bomb is malicious code that triggers under specific conditions.",
        "It lies dormant until activated, causing harm or disruption.",
        "Protect systems by monitoring and auditing code changes."
        ],

        "what is an insider threat": [
        "An insider threat comes from within an organization, like employees.",
        "It can be intentional or accidental, risking sensitive data.",
        "Implement monitoring and access controls to mitigate insider threats."
        ],

        "what is a hash function": [
        "A hash function generates a fixed-length string from data input.",
        "It’s commonly used for password storage and data integrity.",
        "Hashing ensures data remains secure and unaltered."
        ],

        "what is an advanced persistent threat (apt)": [
        "An APT is a long-term, targeted cyberattack by skilled threat actors.",
        "APTs aim to steal sensitive information or cause disruption.",
        "Prevent APTs with strong security policies and monitoring."
        ],

        "what is a honeypot": [
        "A honeypot is a decoy system to attract and analyze attackers.",
        "It’s used to detect and study cyber threats.",
        "Honeypots help improve defense strategies by understanding attackers."
        ],

        "what is a rootkit": [
        "A rootkit is malware that hides itself to maintain unauthorized access.",
        "It’s designed to evade detection and control systems.",
        "Use rootkit scanners and update your system to stay protected."
        ],

        "what is cybersecurity awareness": [
        "Cybersecurity awareness educates people about safe online practices.",
        "It helps reduce risks by promoting informed behavior.",
        "Stay aware to protect yourself and others from cyber threats."
        ],

        "what is a cybersecurity policy": [
        "A cybersecurity policy outlines rules to protect organizational data.",
        "It includes guidelines for passwords, devices, and incident response.",
        "Strong policies help ensure compliance and reduce risks."
        ],

        "what is a denial of service (dos) attack": [
        "A DoS attack floods a system to make it unavailable to users.",
        "Attackers overload servers with traffic, causing them to crash.",
        "Mitigate DoS with network monitoring and scalable resources."
        ],

        "what is cyber forensics": [
        "Cyber forensics investigates digital evidence in cybercrime cases.",
        "It’s used to identify, recover, and analyze data for legal purposes.",
        "Forensics helps track attackers and secure justice."
        ],

        "what is a session hijacking attack": [
        "Session hijacking steals a user's session ID to impersonate them.",
        "Attackers can access accounts or sensitive information.",
        "Use secure session management to prevent hijacking."
        ],

        "what is network segmentation": [
        "Network segmentation divides a network into smaller segments.",
        "It improves security by limiting access to sensitive data.",
        "Segmenting reduces the spread of cyberattacks within networks."
        ],

        "what is a digital certificate": [
        "A digital certificate verifies the identity of a website or user.",
        "It’s issued by a trusted Certificate Authority (CA).",
        "Certificates ensure secure communication and trust."
        ],

        "what is the gdpr": [
        "The GDPR is a European regulation for data protection and privacy.",
        "It ensures individuals have control over their personal data.",
        "Organizations must comply to avoid penalties and protect data."
        ],

        "what is a phishing email": [
        "A phishing email tricks you into sharing sensitive information.",
        "It often looks legitimate to deceive recipients.",
        "Avoid clicking on suspicious links or attachments in emails."
        ],

        "what is a sandbox in cybersecurity": [
        "A sandbox isolates programs to test for malicious behavior.",
        "It’s used to safely analyze malware without affecting systems.",
        "Sandboxes help identify threats before deployment."
        ],

        "what is a cyber kill chain": [
        "The cyber kill chain outlines stages of a cyberattack.",
        "It helps detect and respond to attacks effectively.",
        "Understanding the kill chain strengthens defense strategies."
        ],

        "what is data exfiltration": [
        "Data exfiltration is the unauthorized transfer of data from a system.",
        "It’s often caused by malware or insider threats.",
        "Prevent exfiltration with monitoring and strong access controls."
        ],

        "what is a sql injection attack": [
        "SQL injection exploits vulnerabilities to manipulate databases.",
        "Attackers use malicious SQL code to access or modify data.",
        "Prevent SQL injection with input validation and parameterized queries."
        ],

        "what is a vulnerability exploit": [
        "A vulnerability exploit takes advantage of system flaws.",
        "Attackers use exploits to compromise systems or data.",
        "Patch vulnerabilities promptly to prevent exploits."
        ],

        "what is an access control list (acl)": [
        "An ACL specifies who can access resources and what actions they can take.",
        "It helps control permissions for users or devices.",
        "Use ACLs to enhance system security and limit access."
        ],

        "what is patch management": [
        "Patch management ensures software is up to date and secure.",
        "It involves applying updates to fix vulnerabilities.",
        "Regular patching protects systems from known threats."
        ],

        "what is endpoint protection": [
        "Endpoint protection secures devices like laptops and smartphones.",
        "It includes antivirus, firewalls, and device management tools.",
        "Protect endpoints to prevent malware and unauthorized access."
        ],
    }

    for keyword, response_list in responses.items():
        if keyword.lower() in user_input.lower():
            reply = random.choice(response_list)
            speak(reply)
            return reply

    fallback_responses = [
        "I'm not sure how to respond to that, but I'm here to listen!",
        "Hmm, I didn't quite get that, but I'd love to help!",
        "Could you tell me more? I'm here for you!"
    ]
    reply = random.choice(fallback_responses)
    speak(reply)
    return reply

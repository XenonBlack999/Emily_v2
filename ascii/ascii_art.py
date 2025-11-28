import time
import pyfiglet
import os

# -*- coding: utf-8 -*-
# for all ascii art function is in here 


#ASCII art section
#respberry pi pico art    
def raspberry_pi_pico_schematic_ascii_art():
    ascii_art = r"""
   Schematic Diagram
   
                |power usb|                           
        +--------------------------+   
        |     Raspberry Pi Pico     | 
        |GP0                    VBUS| 
        |GP1                    VSYS|  
        |GND                     GND| 
        |GP2                  3V3_EN| 
        |GP3                 3V3_OUT|
        |GP4                ADC_VREF| 
        |GP5                 GP28_A2| 
        |GND                    AGND|      
        |GP6                 GP27_A1| 
        |GP7                 GP26_A0| 
        |GP8                     RUN| 
        |GP9                    GP22| 
        |GND                     GND| 
        |GP10                   GP21| 
        |GP11                   GP20| 
        |GP12  K          0     GP19| 
        |GP13  L          1     GP18| 
        |GND   C          D      GND| 
        |GP14  W          W     GP17| 
        |GP15  S    GND   S     GP16| 
        |      |    |     |         | 
        +--------------------------+

    """
    print(ascii_art)    

    
#About Author 
def about():
    content_about = r"""
    ---------------------------------------------------------
                ILLUMINATING THE DIGITAL WORLD
    =========================================================
                      _______
             ..-'`       ````---.
           .'          ___ .'````.'SS'.
          /        ..-SS####'.  /SSHH##'.
         |       .'SSSHHHH##|/#/#HH#H####'.
        /      .'SSHHHHH####/||#/: \SHH#####\
       /      /SSHHHHH#####/!||;`___|SSHH###\
    -..__    /SSSHHH######.         \SSSHH###\
    `.'-.''--._SHHH#####.'           '.SH####/
      '. ``'-  '/SH####`/_             `|H##/
      | '.     /SSHH###|`'==.       .=='/\H|
      |   `'-.|SHHHH##/\__\/        /\//|~|/  
      |    |S#|/HHH##/             |``  |
      |    \H' |H#.'`              \    |
      |        ''`|               -     /
      |          /H\          .----    /
      |         |H#/'.           `    /
      |          \| | '..            /
      |    ^~DLF   /|    ''..______.'
       \          //\__    _..-. | 
        \         ||   ````     \ |_
         \    _.-|               \| |_
         _\_.-'   `'''''-.        |   `--.
                        

    Being a hacker means not accepting the world 
     as it is, but working to improve it. 
     
     
     Author: Xenon Bytechef (Burma)
     File : ophelia.py
     Date : [oct/4/2024]
    ----------------------------------------------------------
    """
    print(content_about)
    
    
def intro():
    
    loading_text = [
        "[~] Emily - Python AI Assistant...",
        "[~] Status      : Online/Offline",
        "[~] Mode        : Passive Listening/Command...",
        "[~] Personality : Calm, Curious, Slightly Sarcastic...",
        "[✓] Emily is ready to assist you.\n"
    ]

    for line in loading_text:
        print(line)
        time.sleep(0.6)

    print("Type your command below, human. Don't disappoint me.\n")


#!/bin/env python3

import subprocess, termcolor, argparse

parser = argparse.ArgumentParser(description="[?] Usage: "+ termcolor.colored("python3 public_ip.py", 'green'))
args = parser.parse_args()

info = """
▒█▀▄▀█ █░░█ 　 ▀█▀ ▒█▀▀█ 
▒█▒█▒█ █▄▄█ 　 ▒█░ ▒█▄▄█ 
▒█░░▒█ ▄▄▄█ 　 ▄█▄ ▒█░░░ 
\n
[*] By Anonymose - find own Public IP Adress.
[*] Get your public ip address using site: http://checkip.dyndns.org/.
"""
if __name__ == "__main__":
    try:
        #variable stored shell command...
        shell_command = "curl -s http://checkip.dyndns.org/ | grep -o '[[:digit:].]\+'"
        
        #start program...
        subprocess.call('clear', shell=True) #clear output terminal screen
        print(info)
        print(termcolor.colored("\n> Personal Public IP Address:", 'white'))
        subprocess.call(shell_command, shell=True)
    
    except:
        print(termcolor.colored("[!] Error: please restart the program"))




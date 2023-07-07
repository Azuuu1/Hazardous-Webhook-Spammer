from pystyle import *
import requests
import time
from colorama import Fore, Style

def spammer():
    try:
        webhook = input("Webhook:")
        message = input("Message:")
        num_spam = int(input("Number of times to spam:"))
        delay = float(input("Delay between each message (in seconds):"))

        for _ in range(num_spam):
            response = requests.post(webhook, data={'content': message})
            if response.status_code == 204:
                print(f"{Fore.GREEN}[+] Message sent{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Message not sent{Style.RESET_ALL}")
            time.sleep(delay)
    except requests.exceptions.MissingSchema:
        print(f"{Fore.LIGHTRED_EX}[!] Wrong Webhook{Style.BRIGHT}")
        time.sleep(2)
import requests

def check_webhook():
    webhook_url = input("Enter the webhook URL: ")
    response = requests.get(webhook_url)
    
    if response.status_code == 200:
        print(f"{Fore.GREEN}[+]Webhook works{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTRED_EX}[-]Webhook does not work{Style.BRIGHT}")
        time.sleep(2)
    














    

options = ("|1 Webhook Spammer|2 Webhook checker|3 Github")







text = """
 _   _                        _                   _    _      _     _                 _      _____                                           
| | | |                      | |                 | |  | |    | |   | |               | |    /  ___|                                          
| |_| | __ _ ______ _ _ __ __| | ___  _   _ ___  | |  | | ___| |__ | |__   ___   ___ | | __ \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
|  _  |/ _` |_  / _` | '__/ _` |/ _ \| | | / __| | |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /  `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
| | | | (_| |/ / (_| | | | (_| | (_) | |_| \__ \ \  /\  /  __/ |_) | | | | (_) | (_) |   <  /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
\_| |_/\__,_/___\__,_|_|  \__,_|\___/ \__,_|___/  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                                                                  | |                                        
                                                                                                  |_|                                       
"""






print(Center.XCenter("Welcome To Hazardous Webhook Spammer Made By Azuu#6735"))
print(Center.XCenter(text))
print(Center.XCenter(options))
select = input("Which option u wanna use:")
if select == ("1"):
    spammer()
if select == ("2"):
    check_webhook()
if select == ("3"):
    print("123")








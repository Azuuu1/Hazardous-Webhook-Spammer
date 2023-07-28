from pystyle import *
from colorama import *
import requests
import time
#new versionn :00
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

def check_webhook():
    webhook_url = input("Enter the webhook URL: ")
    response = requests.get(webhook_url)

    if response.status_code == 200:
        print(f"{Fore.GREEN}[+] Webhook works{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTRED_EX}[-] Webhook does not work{Style.BRIGHT}")
        time.sleep(2)

def delwebhook():
    webhook_url = input("Enter the webhook URL to delete: ")
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhook deleted successfully.")
    else:
        print("Failed to delete webhook. Status code:", response.status_code)

options = ("|1 Webhook Spammer|2 Webhook checker|3 Webhook Deleter|4 Github")
intro = """
 _   _                        _                   _    _      _     _                 _      _____                                           
| | | |                      | |                 | |  | |    | |   | |               | |    /  ___|                                          
| |_| | __ _ ______ _ _ __ __| | ___  _   _ ___  | |  | | ___| |__ | |__   ___   ___ | | __ \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
|  _  |/ _` |_  / _` | '__/ _` |/ _ \| | | / __| | |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /  `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
| | | | (_| |/ / (_| | | | (_| | (_) | |_| \__ \ \  /\  /  __/ |_) | | | | (_) | (_) |   <  /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
\_| |_/\__,_/___\__,_|_|  \__,_|\___/ \__,_|___/  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                                                                  | |                                        
                                                                                                  |_|      
                                                Press Enter                                             

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}
 _   _                        _                   _    _      _     _                 _      _____                                           
| | | |                      | |                 | |  | |    | |   | |               | |    /  ___|                                          
| |_| | __ _ ______ _ _ __ __| | ___  _   _ ___  | |  | | ___| |__ | |__   ___   ___ | | __ \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
|  _  |/ _` |_  / _` | '__/ _` |/ _ \| | | / __| | |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /  `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
| | | | (_| |/ / (_| | | | (_| | (_) | |_| \__ \ \  /\  /  __/ |_) | | | | (_) | (_) |   <  /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
\_| |_/\__,_/___\__,_|_|  \__,_|\___/ \__,_|___/  \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                                                                  | |                                        
                                                                                                  |_|        
                                                Press Enter     

""")
print(Center.XCenter(options))
select = input("Which option do you want to use: ")

if select == "1":
    spammer()
elif select == "2":
    check_webhook()
elif select == "3":
    delwebhook()
elif select == "4":
    print("https://github.com/Azuuu1/Hazardous-Webhook-Spammer/blob/main/Hazardous%201.0.0/Hazardous%20Webhook%20Spammer.py")
else:
    print("Didn't find the option")
time.sleep(2)

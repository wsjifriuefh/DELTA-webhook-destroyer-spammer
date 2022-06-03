import requests, colorama, time, os


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, username, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "username": "USERNAME OF YOUR WEBHOOK", "avatar_url": "YOUR AVATAR URL"})
            if data.status_code == 204:
                print(f"{colorama.Back.GREEN} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.GREEN} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "true":
        requests.delete(webhook)
        print(f'{colorama.Fore.GREEN}webhook deleted')
    print(f'{colorama.Fore.GREEN}done...')


def initialize():
    print(f"""{colorama.Fore.GREEN}
     _      _ _        
  __| | ___| | |_ __ _ 
 / _` |/ _ \ | __/ _` |
| (_| |  __/ | || (_| |
 \__,_|\___|_|\__\__,_|             


                        by wwz
     """)
    webhook = input("url > ")
    username = "USERNAME OF YOUR WEBHOOK"
    message = input("Enter a message > ")
    delay = "1" 
    amount = input("Enter an amount > ")
    hookDeleter = "true or false"
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "true" and hookDeleter.lower() != "false"):
        _exit()
    else:
        main(webhook, username, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls')
    os.system('title Destroyer')
    initialize()

import requests
import os
import random
import string
import time

# ANSI color code for blue
BLUE = '\033[94m'
ENDC = '\033[0m'

def webhook_spammer(url, message, count):
    for i in range(count):
        payload = {"content": message}
        response = requests.post(url, json=payload)
        print(f"Message {i+1}: Status Code {response.status_code}")
        time.sleep(1)  # Slight delay to prevent overload


def pinger(target, count):
    for i in range(count):
        response = os.system(f"ping -c 1 {target}")
        if response == 0:
            print(f"Ping {i+1}: {target} is up!")
        else:
            print(f"Ping {i+1}: {target} is down!")
        time.sleep(1)  # Delay to prevent spamming too quickly


def nitro_generator(count):
    for _ in range(count):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        print(f"Generated Nitro Code: https://discord.gift/{code}")
        time.sleep(0.5)


def roblox_giftcard_generator(count):
    for _ in range(count):
        # Roblox gift cards usually have 12 digits: XXXX-XXXX-XXXX
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        formatted_code = '-'.join([code[i:i+4] for i in range(0, 12, 4)])
        print(f"Generated Roblox Gift Card Code: {formatted_code}")
        time.sleep(0.5)


def credits():
    print(f"{BLUE}Void Tool - Created by testuser{ENDC}\n")


def banner():
    print(f"""
{BLUE}
███████╗ ██████╗██╗     ██╗ ██████╗███████╗     ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝██╔════╝██║     ██║██╔════╝██╔════╝     ██╔════╝██╔═══██╗██╔══██╗████╗  ██║
█████╗  ██║     ██║     ██║██║     █████╗       ███████╗██║   ██║██████╔╝██╔██╗ ██║
██╔══╝  ██║     ██║     ██║██║     ██╔══╝       ╚════██║██║   ██║██╔══██╗██║╚██╗██║
███████╗╚██████╗███████╗██║╚██████╗███████╗     ███████║╚██████╔╝██║  ██║██║ ╚████║
╚══════╝ ╚═════╝╚══════╝╚═╝ ╚═════╝╚══════╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
{ENDC}
    """)


def menu():
    banner()  # Display banner at the start
    while True:
        print("""
        1. Webhook Spammer
        2. DDoS
        3. Nitro Generator
        4. Roblox Gift Card Generator
        5. Credits
        6. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter webhook URL: ")
            message = input("Enter the message: ")
            count = int(input("How many times to spam? "))
            webhook_spammer(url, message, count)

        elif choice == '2':
            target = input("Enter the IP/URL: ")
            count = int(input("How many times to DDoS? "))
            pinger(target, count)

        elif choice == '3':
            count = int(input("How many Nitro codes to generate? "))
            nitro_generator(count)

        elif choice == '4':
            count = int(input("How many Roblox gift card codes to generate? "))
            roblox_giftcard_generator(count)

        elif choice == '5':
            credits()

        elif choice == '6':
            print("Exiting the tool...")
            break

        else:
            print("Invalid choice, please try again!")


def main():
    menu()


if __name__ == "__main__":
    main()

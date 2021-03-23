from colorama import Fore, Back, Style
from functions import *
from getpass import getpass


if __name__ == "__main__":
    print(Fore.CYAN  + "-"*34)
    print('INSTAGRAM -- IMAGE DOWNLOADER TOOL              -- github.com/Jay-2512')
    print("-"*34)

    print(Fore.YELLOW + '\n\n[+] Choose your login mode\n')
    print(Style.RESET_ALL)

    print(Fore.LIGHTRED_EX + '1: Instagram Direct Login\n\n2: Facebook Login')
    print("-"*34)
    print(Style.RESET_ALL)

    login_mode = input(Fore.RED + '\n[?] >>> ')

    print(Fore.LIGHTMAGENTA_EX + '\n[+] What Browser Do you use?\n')
    print(Fore.YELLOW + '1: Google Chrome\n')
    print(Fore.LIGHTRED_EX + '2: Mozilla Firefox\n')

    print("-"*34)

    browser = input(Fore.RED + '\n[?] >>> ')
    print(Style.RESET_ALL)

    print("-"*34)
    extras.clear(Fore)

    if login_mode == '1':
        username = input(Fore.LIGHTWHITE_EX + 'Enter your Instagram username : ')
        password = getpass(Fore.LIGHTCYAN_EX + 'Enter your Instagram password : ')

        keyword = input(Fore.LIGHTCYAN_EX + 'Enter the name of the user or the hashtag you want to fetch the images from : ')

        cnct.insta_login(username, password, browser, keyword)
    elif login_mode == '2':
        fb_username = input(Fore.LIGHTWHITE_EX + 'Enter your Facebook username : ')
        fb_password = getpass(Fore.LIGHTCYAN_EX + 'Enter your Facebook password : ')

        keyword = input(Fore.LIGHTCYAN_EX + 'Enter the name of the user or the hashtag you want to fetch the images from : ')

        cnct.fb_login(fb_username, fb_password, browser, keyword)
    else:
        print(Fore.RED + 'Enter a valid choice! (1 or 2)')
        print(Style.RESET_ALL)
    
    print("-"*34)
    #extras.clear(Fore)



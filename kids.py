import requests
import pyfiglet
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

animasi = pyfiglet.figlet_format("KaytoKID")
print(animasi)
print("")
print("")
print("Welcome to khalifah cyber crew : KCC KaytoKID")

print("")
print("")

x = input('Enter the request URL from Inspect Element: ')
print("")
print("")

print('Reporting the poor sod.....')
print('')
print('')

while True:
    req = session.post(x)
    print(req.text)
    print('reported :D')
    time.sleep(2)

input()




import requests
import json
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
import time
import socket
import bs4
from bs4 import BeautifulSoup





os.system("title Web Parse - OPEN SOURCE")


front = f"""{Fore.RED}

 $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$ ___$$\ $$ ___$$\ $$ ___$$\ $$ ___$$\ 
\_/   $$ |\_/   $$ |\_/   $$ |\_/   $$ |
  $$$$$ /   $$$$$ /   $$$$$ /   $$$$$ / 
  \___$$\   \___$$\   \___$$\   \___$$\ 
$$\   $$ |$$\   $$ |$$\   $$ |$$\   $$ |
\$$$$$$  |\$$$$$$  |\$$$$$$  |\$$$$$$  |
 \______/  \______/  \______/  \______/ 
                                                                                                                  
"""
print(front)
url = input(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}] url without https:// -->  {Fore.WHITE}")

new_url = "https://" + url

serv = socket.gethostbyname(url)
urls = []


#serv = host adrr
#new_url = url > https://url

web = requests.get(new_url)
print(f"{Fore.RED}[{Fore.WHITE}EXTRACTED URLS{Fore.RED}] """)
soup = BeautifulSoup(web.text, 'html.parser')
for link in soup.find_all('a'):
    urls = link.get('href')
    print(Fore.RED + urls)
get_code = web.text

print(f"""
{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Host IP > {serv}
{Fore.RED}[{Fore.WHITE}EXTRACTED CODE{Fore.RED}]
{get_code}""")

input("")





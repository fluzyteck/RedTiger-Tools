"""
Copyright (c) RedTiger (https://redtiger.online/)
See the file 'LICENSE' for copying permission
"""

from Config.Util import *
from Config.Config import *
try:
    import random
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from deep_translator import GoogleTranslator
    from selenium.webdriver.common.keys import Keys
except Exception as e:
   ErrorModule(e)

Title("Username Tracker (OSINT)")

try:
    username = input(f"\n{INPUT} Username -> {reset}")

    if censored in username:
        print(f'{ERROR} Unable to find username "{white}{username}{red}".')
        Continue()
        Reset()

    print(f"""
{white}[{red}01{white}] {red}->{white} Chrome (Linux)
{white}[{red}02{white}] {red}->{white} Chrome (Windows)
{white}[{red}03{white}] {red}->{white} Firefox (Windows)
{white}[{red}04{white}] {red}->{white} Edge (Windows)
    """)
    browser = input(f"{red}{INPUT} Browser -> {reset}")

    if browser == '1':
        if sys.platform.startswith("win"):
            OnlyLinux()
        try:
            navigator = "Chrome Linux"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            chrome_driver_path = os.path.abspath("./Driver/chromedriverlinux")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
            driver = webdriver.Chrome(options=chrome_options)
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()
            
    if browser == '2':
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Chrome"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Chrome()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser == '3':
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Firefox"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Firefox()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()

    elif browser == '4':
        if sys.platform.startswith("linux"):
            OnlyLinux()
        try:
            navigator = "Edge"
            print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} {navigator} Starting..{blue}")
            driver = webdriver.Edge()
            print(f"{red}[{white}{current_time_hour()}{red}] {INFO} {navigator} Ready !{blue}")
        except:
            print(f"{ERROR} {navigator} not installed or driver not up to date.")
            Continue()
            Reset()
    else:
        ErrorChoice()

    driver.set_window_size(900, 600)

    def text_page():
        page_text = driver.execute_script("return document.documentElement.innerText")
        return page_text
        
    def text_translated(text):
        try:
            translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        except: 
            translated_text = text
        return translated_text

    def tiktok_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Tiktok..{blue}")
        try:
            link = r"https://www.tiktok.com/@" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This account cannot be found" in text_translated(text_page()):
                tiktok = False
            else:
                tiktok = link
        except Exception as e:
            tiktok = f"Error: {e}"
        return tiktok

    def instagram_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Instagram..{blue}")
        try:
            link = r"https://instagram.com/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This page is unfortunately not available" in text_translated(text_page()):
                instagram = False
            else:
                instagram = link
        except Exception as e:
            instagram = f"Error: {e}"
        return instagram

    def giters_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Giters..{blue}")
        try:
            link = r"https://giters.com/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This page could not be found" in text_translated(text_page()):
                giters = False
            elif username in text_page():
                giters = link
            else:
                giters = False

        except Exception as e:
            giters = f"Error: {e}"
        return giters

    def github_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Github..{blue}")
        try:
            link = r"https://github.com/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "Find code, projects, and people on GitHub" in text_translated(text_page()):
                github = False
            else:
                github = link
        except Exception as e:
            github = f"Error: {e}"
        return github

    def paypal_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Paypal..{blue}")
        try:
            link = r"https://www.paypal.com/paypalme/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "We cannot find this profile" in text_translated(text_page()):
                paypal = False
            elif "We were not able to process your request. Please try again later" in text_translated(text_page()):
                paypal = f"Error: Rate Limit"
            else:
                paypal = link
        except Exception as e:
            paypal = f"Error: {e}"
        return paypal

    def telegram_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Telegram..{blue}")
        try:
            link = r"https://t.me/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "If you have Telegram, you can contact" in text_translated(text_page()):
                telegram = False
            elif "a new era of messaging" in text_translated(text_page()):
                telegram = False
            else:
                telegram = link
        except Exception as e:
            telegram = f"Error: {e}"
        return telegram

    def snapchat_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Snapchat..{blue}")
        try:
            link = r"https://www.snapchat.com/add/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "This content could not be found" in text_translated(text_page()):
                snapchat = False
            else:
                snapchat = link
        except Exception as e:
            snapchat = f"Error: {e}"
        return snapchat

    def linktree_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Linktree..{blue}")
        try:
            link = r"https://linktr.ee/" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "The page you’re looking for doesn’t exist" in text_translated(text_page()):
                linktree = False
            else:
                linktree = link
        except Exception as e:
            linktree = f"Error: {e}"
        return linktree

    def roblox_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Roblox..{blue}")
        try:
            link = r"https://www.roblox.com/search/users?keyword=" + username
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "No results available for" in text_translated(text_page()):
                roblox = False
            else:
                roblox = link
        except Exception as e:
            roblox = f"Error: {e}"
        return roblox

    def streamlabs_search():
        print(f"{red}[{white}{current_time_hour()}{red}] {WAIT} Search in Streamlabs..{blue}")
        try:
            link = r"https://streamlabs.com/" + username + r"/tip"
            driver.get(link)
            driver.implicitly_wait(10)
            time.sleep(2)
            if "UNAUTHORIZED" in text_translated(text_page()):
                streamlabs = False
            elif "401" in text_translated(text_page()):
                streamlabs = False
            else:
                streamlabs = link
        except Exception as e:
            streamlabs = f"Error: {e}"
        return streamlabs


    Slow(f"""
    {red}The username "{white}{username}{red}" was found:

    {white}[{red}+{white}]{red} Tiktok     : {white}{tiktok_search()}{red}
    {white}[{red}+{white}]{red} Instagram  : {white}{instagram_search()}{red}
    {white}[{red}+{white}]{red} Snapchat   : {white}{snapchat_search()}{red}
    {white}[{red}+{white}]{red} Giters     : {white}{giters_search()}{red}
    {white}[{red}+{white}]{red} Github     : {white}{github_search()}{red}
    {white}[{red}+{white}]{red} Paypal     : {white}{paypal_search()}{red}
    {white}[{red}+{white}]{red} Telegram   : {white}{telegram_search()}{red}
    {white}[{red}+{white}]{red} Linktree   : {white}{linktree_search()}{red}
    {white}[{red}+{white}]{red} Roblox     : {white}{roblox_search()}{red}
    {white}[{red}+{white}]{red} Streamlabs : {white}{streamlabs_search()}{red}
    """)

    driver.quit()

    Continue()
    Reset()
except Exception as e:
    Error(e)
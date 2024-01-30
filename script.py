import webbrowser
import pyautogui as py
import time
import random
import requests

words_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(words_site)
words = response.content.decode('UTF-8').splitlines()
random.shuffle(words)
words = words[:30]


browser = webbrowser.get('windows-default')
browser.open("www.bing.com", new=0)
time.sleep(2)

for word in words:
    
    py.write(word, interval=0.35)
    py.keyDown("return")

    time.sleep(3)


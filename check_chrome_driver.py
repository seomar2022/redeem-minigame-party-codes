#Selenium is an open source umbrella project 
#for a range of tools and libraries aimed at supporting browser automation.
#pip install selenium

#chromdriver is needed ->https://chromedriver.chromium.org/
#my current version is 121.0.6167.161（Official Build）
#If you are using Chrome version 115 or newer, please consult the Chrome for Testing availability dashboard. This page provides convenient JSON endpoints for specific ChromeDriver version downloading.
#https://www.codeit.kr/community/questions/UXVlc3Rpb246NjQxNDEzYTRlNzQ2NDc0NTZhMzQ5NTA1

#from selenium import webdriver

#driver = webdriver.Chrome("c://chromedriver.exe")


# PS C:\study\redeem-minigame-party-codes> & C:/Users/seomar/AppData/Local/Programs/Python/Python310/python.exe c:/study/redeem-minigame-party-codes/redeem_codes.py
# Traceback (most recent call last):
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\driver_finder.py", line 38, in get_path
#     path = SeleniumManager().driver_location(options) if path is None else path
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\selenium_manager.py", line 87, in driver_location
#     browser = options.capabilities["browserName"]
# AttributeError: 'str' object has no attribute 'capabilities'


# Traceback (most recent call last):
#   File "c:\study\redeem-minigame-party-codes\redeem_codes.py", line 12, in <module>
#     driver = webdriver.Chrome("c://chromedriver.exe")
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 45, in __init__
#     super().__init__(
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\chromium\webdriver.py", line 49, in __init__
#     self.service.path = DriverFinder.get_path(self.service, options)
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\driver_finder.py", line 40, in get_path
#     msg = f"Unable to obtain driver for {options.capabilities['browserName']} using Selenium Manager."
# AttributeError: 'str' object has no attribute 'capabilities'
# PS C:\study\redeem-minigame-party-codes> & C:/Users/seomar/AppData/Local/Programs/Python/Python310/python.exe c:/study/redeem-minigame-party-codes/redeem_codes.py
# Traceback (most recent call last):
#   File "c:\study\redeem-minigame-party-codes\redeem_codes.py", line 20, in <module>
#     driver = webdriver.Chrome(options=options, executable_path="c://chromedriver.exe")
# TypeError: WebDriver.__init__() got an unexpected keyword argument 'executable_path'
# PS C:\study\redeem-minigame-party-codes> & C:/Users/seomar/AppData/Local/Programs/Python/Python310/python.exe c:/study/redeem-minigame-party-codes/redeem_codes.py
# Traceback (most recent call last):
#   File "c:\study\redeem-minigame-party-codes\redeem_codes.py", line 20, in <module>
#     driver = webdriver.Chrome(executable_path="c://chromedriver.exe", options=options)
# TypeError: WebDriver.__init__() got an unexpected keyword argument 'executable_path'
# PS C:\study\redeem-minigame-party-codes> & C:/Users/seomar/AppData/Local/Programs/Python/Python310/python.exe c:/study/redeem-minigame-party-codes/redeem_codes.py
# Traceback (most recent call last):
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\driver_finder.py", line 38, in get_path
#     path = SeleniumManager().driver_location(options) if path is None else path
#   File "C:\Users\seomar\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\common\selenium_manager.py", line 87, in driver_location
#     browser = options.capabilities["browserName"]
# AttributeError: 'str' object has no attribute 'capabilities'



#####################################################

#https://www.youtube.com/watch?v=AzPXHXv9d3Q
#I can't use chrome driver due to version of chrome. 
#my version is 121.0.6167.185
#I can't find any driver that match with my version.
#But thanks to above Youtube video I solved my problem.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



url="https://naver.com"

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(2)

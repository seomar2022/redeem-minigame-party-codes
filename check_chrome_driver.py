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

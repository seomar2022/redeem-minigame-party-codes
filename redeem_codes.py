#Selenium is an open source umbrella project 
#for a range of tools and libraries aimed at supporting browser automation.
#pip install selenium

#chromdriver is needed ->https://chromedriver.chromium.org/
#my current version is 121.0.6167.161（Official Build）
#If you are using Chrome version 115 or newer, please consult the Chrome for Testing availability dashboard. This page provides convenient JSON endpoints for specific ChromeDriver version downloading.
from selenium import webdriver

driver = webdriver.Chrome("c://chromedriver.exe")
driver.get("https://coupon.withhive.com/720")
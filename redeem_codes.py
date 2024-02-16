from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://coupon.withhive.com/720")
time.sleep(2)
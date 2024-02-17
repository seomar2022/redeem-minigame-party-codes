from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

# options = Options()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://coupon.withhive.com/720")

#time.sleep(second): Suspend execution of the calling thread for the given number of seconds.
#time.sleep(10) #Wait 10 seconds for the page to completely load

#
#driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > div.input_box.server_list_area.show > div.select_wrap > button").click()
#driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > div.input_box.server_list_area.show > div.select_wrap > ul > li > button").click()


driver.find_element(By.CSS_SELECTOR, "#cs_code").send_keys("")
driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys("MGP200DAYS")
driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > button").click()
time.sleep(20)

driver.find_element(By.CSS_SELECTOR, "body > div.pop_wrap.server.coupon_server_lyr > div > ul > li > label > span").click()
driver.find_element(By.CSS_SELECTOR, "body > div.pop_wrap.server.coupon_server_lyr > div > div.btns > button.btn_confirm").click()

time.sleep(20)
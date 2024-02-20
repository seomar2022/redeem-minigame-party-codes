from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd  #pip install pandas

driver = webdriver.Chrome()

driver.get("https://coupon.withhive.com/720")

#time.sleep(second): Suspend execution of the calling thread for the given number of seconds.
#time.sleep(10) #Wait 10 seconds for the page to completely load

#get CS codes in the excel file
cs_codes = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1], sheet_name="nicknames with CS codes")

#.dropna(): remove NaN values
#.values.tolist(): convert as a list
cs_codes = cs_codes.dropna().values.tolist() 

#convert the data type to int
#[105548.0] -> 105548
cs_codes = [int(float(str(x).split('.')[0])) for sublist in cs_codes for x in sublist]

#select a server
driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > div.input_box.server_list_area.show > div.select_wrap > button").click()
driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > div.input_box.server_list_area.show > div.select_wrap > ul > li > button").click()


coupon_code = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1], sheet_name="coupon")

#input CS code and coupon code
driver.find_element(By.CSS_SELECTOR, "#cs_code").send_keys(f"{cs_codes[0]}")
driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys("MGP200DAYS")
driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > button").click()
time.sleep(5)

#select a server again
driver.find_element(By.CSS_SELECTOR, "body > div.pop_wrap.server.coupon_server_lyr > div > ul > li > label > span").click()
driver.find_element(By.CSS_SELECTOR, "body > div.pop_wrap.server.coupon_server_lyr > div > div.btns > button.btn_confirm").click()

time.sleep(5)

#result(1) -> redeem the code successfully
#result(2) -> the codes was already used
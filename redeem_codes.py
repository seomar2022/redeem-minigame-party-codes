from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd  #pip install pandas
import pyautogui as pyautogui #pip install pyautogui
import openpyxl

driver = webdriver.Chrome()

driver.get("https://coupon.withhive.com/720")

#time.sleep(second): Suspend execution of the calling thread for the given number of seconds.
#time.sleep(10) #Wait 10 seconds for the page to completely load

file = "C:/study/CS codes.xlsx"
#get CS codes in the excel file
df = pd.read_excel(file, sheet_name="nicknames with CS codes")

#select the coupon column(its index is 1)
cs_codes = df.iloc[:,[1]]

#.dropna(): remove NaN values
#.values.tolist(): convert as a list
cs_codes = cs_codes.dropna().values.tolist() 

#convert the data type to int
#[105548.0] -> 105548
cs_codes = [int(float(str(x).split('.')[0])) for sublist in cs_codes for x in sublist]

coupon_codes = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1], sheet_name="coupon")

#search last cell that is inserted data
rows, cols = coupon_codes.shape
last_row_index = rows - 1
last_col_index = cols - 1
coupon_code = coupon_codes.iat[last_row_index, last_col_index]

#make list to contain index of each situation
complete = []
fail = []

for cs_code in cs_codes:
        
    #select a server
    driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > div.input_box.server_list_area.show > div.select_wrap > button").click()
    driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > div.input_box.server_list_area.show > div.select_wrap > ul > li > button").click()

    #input CS code and coupon code 
    driver.find_element(By.CSS_SELECTOR, "#cs_code").send_keys(cs_code)
    driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys(coupon_code)
    driver.find_element(By.CSS_SELECTOR, "#HIVEcoupon > div.content > div > button").click()

    time.sleep(1)

    #select a server again
    driver.find_element(By.CSS_SELECTOR, "body > div.pop_wrap.server.coupon_server_lyr > div > ul > li > label > span").click()
    driver.find_element(By.CSS_SELECTOR, "body > div.pop_wrap.server.coupon_server_lyr > div > div.btns > button.btn_confirm").click()

    #read the message of alert
    result = driver.find_element(By.CSS_SELECTOR, "#layer_msg").text

    if result.find("!") == -1: #when the message contain a letter '!', it means redeeming was completed.
        #if redeeming failed since the coupon was already used,  append the cs_codes in 'fail'
        fail.append(cs_codes.index(cs_code))
    else: #if the code was redeemed successfully, append the cs_codes in 'complete'
        complete.append(cs_codes.index(cs_code))

    #click the close button
    driver.find_element(By.CSS_SELECTOR, "#layer_close_btn").click()
    
    #refre a webpage
    driver.refresh()

driver.quit()
nicknames = df.iloc[:,[0]]
nicknames = nicknames.dropna().values.tolist() 

# print("쿠폰 등록 성공 유저: ", end="")
# for index in complete:
#     print(nicknames[index], end=" ")

# print("\n쿠폰 등록 실패 유저(이미 쿠폰을 사용): ", end="")
# for index in fail:
#     print(nicknames[index], end=" ")

message = f"쿠폰 등록 성공: {len(complete)}명\n쿠폰 등록 실패: {len(fail)}명\n엑셀 참조"

pyautogui.alert(message, title='미겜천 쿠폰등록하기')


#import an existing Excel file
wb = openpyxl.load_workbook(file)

ws = wb["nicknames with CS codes"]
col_max = ws.max_column

ws.cell(row=1, column = col_max, value=coupon_code)

# ws.cell(row=2, column =1, value="2030-01-01")
# ws.append(["2030-01-02", "pen", 400, 5, "=C3*D3"])

# save file
wb.save(file)
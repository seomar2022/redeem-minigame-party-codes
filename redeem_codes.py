from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd  #pip install pandas
import pyautogui as pyautogui #pip install pyautogui
import openpyxl
import sys
import os

file = "C:/study/CS codes.xlsx"

previous_check =pyautogui.confirm("파일경로에 전용양식(CS codes.xlsx)에 모든 정보를 입력하셨나요?", buttons=['yes', 'no'])

if previous_check == "yes":
    pyautogui.alert("쿠폰 등록을 시작합니다.")
else:
    wb = openpyxl.Workbook()
    #select currently active sheet
    ws = wb.active

    #change name of sheet
    ws.title = "nicknames with CS codes"

    #write the head
    ws.append(["nickname", "cs code"])

    ws = wb.create_sheet("coupon")
    ws.append(["coupon"])
    wb.save(file)
    pyautogui.alert("양식 파일 생성을 완료했습니다. 파일에 정보를 입력 후 다시 프로그램을 실행해주세요.")

    os.startfile(file) #open the Excel file
    sys.exit()  # forcefully exiting the program




driver = webdriver.Chrome()


driver.get("https://coupon.withhive.com/720")

#time.sleep(second): Suspend execution of the calling thread for the given number of seconds.
#time.sleep(10) #Wait 10 seconds for the page to completely load

#file = "C:/study/CS codes.xlsx"

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
#coupon_codes = pd.read_excel(file, usecols=[0], sheet_name="coupon")

#search last cell that is inserted data
rows, cols = coupon_codes.shape
last_row_index = rows - 1
last_col_index = cols - 1
coupon_code = coupon_codes.iat[last_row_index, last_col_index]

#make list to contain index of cs codes that successed 
complete = []

#make dictionary to contain index of cs codes that failed and that reason
fail = {} 

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
        fail2[cs_codes.index(cs_code)] = result
    else: #if the code was redeemed successfully, append the cs_codes in 'complete'
        complete.append(cs_codes.index(cs_code))

    #click the close button
    driver.find_element(By.CSS_SELECTOR, "#layer_close_btn").click()
    
    #refre a webpage
    driver.refresh()

driver.quit()

##alert the result to the user
message = f"쿠폰 등록 성공: {len(complete)}명\n쿠폰 등록 실패: {len(fail)}명\n엑셀 참조"
pyautogui.alert(message, title='미겜천 쿠폰등록하기')

##record the result in the Excel file
#import the Excel file
wb = openpyxl.load_workbook(file)
ws = wb["nicknames with CS codes"]

#find the maximum value of rows
for max_row, row in enumerate(ws, 1):
    if all(c.value is None for c in row):
        break #If all cells in a row are empty, it breaks out of the loop.

#find the maximum value of columns
max_col = 0
for col in ws.iter_cols(): #iterate over each column in the worksheet ws
    if any(cell.value is not None for cell in col): #check if at least one cell in that column has a non-empty value
        max_col += 1

ws.cell(row=1, column = max_col+1, value=coupon_code)

for index in complete:
    ws.cell(row=index+2, column =max_col+1, value="등록 성공")

for index in fail:
    ws.cell(row=index+2, column =max_col+1, value=f"등록 실패({fail[index]})")

# save file
wb.save(file)
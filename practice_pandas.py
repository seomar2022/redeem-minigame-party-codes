#pip install pandas
#pip install Pyarrow
import pandas as pd
import pyautogui as pyautogui #pip install pyautogui


#data = pd.read_excel("C:/study/CS codes.xlsx")
#print(data)

# cs_codes = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1])
# cs_codes = cs_codes.dropna().values.tolist() 
# #.dropna(): remove NaN values
# #.values.tolist(): convert as a list

# #print(cs_codes)

# # print(list[0])
# # print(f"{list[0]}")

# cs_codes = [int(float(str(x).split('.')[0])) for sublist in cs_codes for x in sublist]

# #print(cs_codes)
# #print(type(converted_list[0]))


# # print(type(list[0]))

# coupon_code = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1], sheet_name="coupon")
# print(coupon_code.shape)
# #print(coupon_code.loc[0])
# #print(type(coupon_code.tail(1)))
# #print(coupon_code.tail(1).to_string, "aaaaa")
# print(type(coupon_code.iat[0,0]))
# #print(coupon_code.values.tolist()[1])
# #https://velog.io/@cha-suyeon/%ED%8C%90%EB%8B%A4%EC%8A%A4pandas-%EC%8B%A4%EC%8A%B5-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%94%EC%B6%9C

# rows, cols = coupon_code.shape

# # 가장 마지막 행과 열의 인덱스 계산
# last_row_index = rows - 1
# last_col_index = cols - 1
# print(last_col_index, last_row_index)


df = pd.read_excel("C:/study/CS codes.xlsx", sheet_name="nicknames with CS codes")

#select the coupon column(its index is 1)
cs_codes = df.iloc[:,[1]]
nicknames = df.iloc[:,[0]]

nicknames = nicknames.dropna().values.tolist() 

for i in nicknames:
    print(i)

pyautogui.alert('check')

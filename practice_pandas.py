#pip install pandas
#pip install Pyarrow
import pandas as pd

#data = pd.read_excel("C:/study/CS codes.xlsx")
#print(data)

cs_codes = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1])
cs_codes = cs_codes.dropna().values.tolist() 
#.dropna(): remove NaN values
#.values.tolist(): convert as a list

#print(cs_codes)

# print(list[0])
# print(f"{list[0]}")

cs_codes = [int(float(str(x).split('.')[0])) for sublist in cs_codes for x in sublist]

#print(cs_codes)
#print(type(converted_list[0]))


# print(type(list[0]))

coupon_code = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1], sheet_name="coupon")
print(coupon_code.shape)
print(coupon_code.loc[0])
print(coupon_code.tail(1))
#print(coupon_code.values.tolist()[1])
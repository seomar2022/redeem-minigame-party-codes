#pip install pandas
#pip install Pyarrow
import pandas as pd

#data = pd.read_excel("C:/study/CS codes.xlsx")
#print(data)

cs_codes = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1])
#print(cs_codes)
list = cs_codes.values.tolist()
print(list[0])
for i in list:
    print(int(i))
    print(type(int(i)))
    print("-----")
print(type(list[0]))

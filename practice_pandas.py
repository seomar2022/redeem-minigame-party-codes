import pandas as pd

#data = pd.read_excel("C:/study/CS codes.xlsx")
#print(data)

cs_codes = pd.read_excel("C:/study/CS codes.xlsx", usecols=[1])
print(cs_codes)
print(cs_codes.values.tolist)

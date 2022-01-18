#Importing packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Importing Data
raw_csv_data=pd.read_csv(r"E:\Stock_Analysis\Time-Series-Analysis-Python\data\Section 3\S_3_L_11\Index2018.csv")
df_copy=raw_csv_data.copy()

# Examining the data
print(df_copy.head())
print("==========================")
print(df_copy.describe()) #count, mean, std, min 25% 50% 75% max
print("==========================")
#  find null values in data
print(df_copy.isna().sum())
print("==========================")

# Plotting the Data
df_copy.spx.plot(title="S&P 500 graph", figsize=(20,5))
df_copy.ftse.plot(title="FTSE 100 graph", figsize=(20,5))
plt.title("S&P and FTSE")
plt.show()

# QQ Plot Quartile Quartile plot




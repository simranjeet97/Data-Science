import matplotlib.pyplot as pt
import pandas as pd
df = pd.read_csv("PastHires.csv")
#print(df.head())
new_data = df[['Previous employers','Hired']][:5]
print(new_data)
print(pt.plot(new_data['Previous employers']))
pt.show()
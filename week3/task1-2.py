import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression



df = pd.read_csv("F:/Class 09/week3/python-and-data-science-tools-main/week3/responses.csv") 


df['min'] = pd.to_numeric(df['min'], errors = 'coerce') # change min from string to numeric
df['time'] = df['min']*60 + df.sec # make a time variable

df['exp'].loc[~df['exp'].isin(['Yes','No'])] = np.nan
df.loc[df['sec'] > 60,'sec'] = np.nan

dfx = df.dropna()


X = dfx[["diff"]]
y = dfx[["time"]]

degree=3
polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
polyreg.fit(X,y)


X_seq = np.linspace(X.min(),X.max(),300).reshape(-1,1)
plt.figure()
plt.scatter(X,y)
plt.plot(X_seq,polyreg.predict(X_seq),color="black")
plt.title("Polynomial regression with degree "+str(degree))
plt.show()


# I could not understand concept of this task and i have done as i understand.
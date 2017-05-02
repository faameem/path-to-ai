
import pandas as pd 
import numpy as np
import statsmodels.api as sm


googFile = 'C:/Users/admin/Downloads/LogisticRegression/GOOG.csv'
spFile = 'C:/Users/admin/Downloads/LogisticRegression/S&P500.csv'

goog = pd.read_csv(googFile,sep=",",usecols=[0,6],names=['Date','Goog'],header=0)
sp = pd.read_csv(spFile,sep=",",usecols=[0,6],names=['Date','SP500'],header=0)
goog['SP500'] = sp['SP500']

goog['Date'] = pd.to_datetime(goog['Date'], format='%m/%d/%Y')
goog = goog.sort_values(['Date'], ascending=[True])

returns = goog[[key for key in dict(goog.dtypes) if dict(goog.dtypes)[key] in ['float64', 'int64']]].pct_change()
returns['Date'] = goog['Date']
returns['Intercept'] = 1

xData = np.array(returns[["Goog","SP500","Intercept"]][1:-1])
yData = (returns["Goog"] > 0)[2:]




logit = sm.Logit(yData, xData)
# fit the model
result = logit.fit()
result.summary()


result.predict(xData)
zip(yData,result.predict(xData) > 0.5)
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.metrics import mean_squared_error
from math import sqrt 
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA



def adfuller_test(col):
    result=adfuller(col)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )

    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data is stationary")
    else:
        print("weak evidence against null hypothesis,indicating it is non-stationary ")


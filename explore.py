import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

def quick_group(df,x,y):
    group_single = df.groupby(x).agg({y:['mean','min','max']})
    group_single.columns = ['mean','min','max']
    group_single = group_single.reset_index()
    return print(group_single.sort_values(by='mean', ascending=False))


def fast_pearson(x,y):
    alpha = .05

    corr, p = stats.pearsonr(x, y)

    corr, p
    print(f'correlation is {corr}')
    print(f'P-value is {p}')
    if p < alpha:
        print("We reject the null hypothesis")
        print("we have confidence that there is a correlation")
    else:
        print("We fail to reject the null")



def distributions(train, validate):
    for col in train.columns:
        plt.figure(figsize=(14,8))
        plt.plot(train[col])
        plt.plot(validate[col])
        plt.ylabel(col)
        plt.title(col)
        plt.show()



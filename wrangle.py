import numpy as np
import pandas as pd
import datetime as dt


def get_dow():
    df = pd.read_csv('dow_jones.csv')

    return df



def prep_DOW(df):
    df.date = pd.to_datetime(df['date'], dayfirst=True, infer_datetime_format=True)
    df = df.set_index('date').sort_index()
    df = df.replace('\$',' ', regex=True)
    df['next_weeks_close'] = df.next_weeks_close.astype('float64')
    df['next_weeks_open'] = df.next_weeks_open.astype('float64')
    df['open'] = df.open.astype('float64')
    df['high'] = df.high.astype('float64')
    df['low'] = df.low.astype('float64')
    df['close'] = df.close.astype('float64')
    df['quarter'] = df.quarter.astype('int')

    return df
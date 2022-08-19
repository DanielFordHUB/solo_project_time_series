import numpy as np
import pandas as pd
import datetime as dt


def get_dow():
    '''
    this function gathers data of the 2011 DOW Jones Index 
    colected from the UCI machine learning repository
    '''
    df = pd.read_csv('dow_jones.csv')

    return df



def prep_DOW(df):
    '''
    this function fixes data types of the DOW Jones Dataframe,
    sets date to datetime and index,
    backfills missing data for certain columns, 
    and drops unnecessary columns
    '''
    df.date = pd.to_datetime(df['date'], dayfirst=True, infer_datetime_format=True)
    df = df.set_index('date').sort_index()
    df = df.replace('\$',' ', regex=True)
    df['next_weeks_close'] = df.next_weeks_close.astype('float64')
    df['next_weeks_open'] = df.next_weeks_open.astype('float64')
    df['open'] = df.open.astype('float64')
    df['high'] = df.high.astype('float64')
    df['low'] = df.low.astype('float64')
    df['close'] = df.close.astype('float64')
    df = df.drop(columns='quarter')
    df = df.backfill()

    return df

def split_ibm(df):
    '''
    This function seprates the stock IBM and coincideing observations
    from the rest of the dataframe for in depth time series analysis
    '''
    df_ibm = df.where(df['stock'] == 'IBM')
    df_ibm = df_ibm.dropna()

    return df_ibm


def resample_and_split(df):
    '''
    this function resamples the dataframe and then 
    seperates it into train, validate, and test subsets
    for data integrity and modeling
    '''

    df_resampled = df.resample('w')[['percent_change_price','close','open']].sum()
    
    # set train size to be 50% of total 
    train_size = int(round(df_resampled.shape[0] * 0.5))
    
    # set validate size to be 30% of total 
    validate_size = int(round(df_resampled.shape[0] * 0.3))
    
    # set test size to be number of rows remaining. 
    test_size = int(round(df_resampled.shape[0] * 0.2))
    
    
    validate_end_index = train_size + validate_size
    
    
    train = df_resampled[:train_size]
    validate = df_resampled[train_size:validate_end_index]
    test = df_resampled[validate_end_index:]
    
    print(train.shape[0], validate.shape[0], test.shape[0])
    
    return train, validate, test
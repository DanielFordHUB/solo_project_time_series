# DOW_Jones_time_series_project

## About the Project
with the use of Time series analysis I am trying to create a model that can find and forecast percent change price of IBM in the DOW Jones index

## Executive Summary

- target stock is IBM

- Target variable is Percent Change Price

- Created an Arima Predictive Model

- Model could perform better

- suggest pivoting to regression model for full scope of dataframe

### Data Dictionary:
   | Column/Feature | Description |
    |--- | --- |
    | __stock__ | The name desssignation of the stock |\n
    | __date__ | the date an observation occured |\n
    | __open__ |  | The price a stock opened at that day |\n
    | __high__ | The high point of a stock that day|\n
    | __low__ | The low point of a stock that day |\n
    | __close__ | The price a stock closed that day |\n
    |__volume__ | the amount of stock volume traded that day |\n
    |__percent_change_price__ | The % the stock changed by day|\n
    |__percent_change_volume_over_last_wk__ | the % a stocks volume has changed by week |\n
    |__previous_weeks_volume__ | Volume of previous week |\n
    |__next_weeks_open__ | the open of the stock in the next week |\n
    |__next_weeks_close__ | the close of the stock in the next week |\n
    |__percent_change_next_weeks_price__ | the % a stocks price has changed in the next week |\n
    |__days_to_next_dividend__ | number of days to next dividend |\n
    |__percent_return_next_dividend__ | the % returned in the next dividend |\n
### Goals

To use Time series analysis to create a forecasting model for percent change price


### Initial Questions

1. Should I build a regression or Time Series Model

2. What stock should I basse my Time series off of

3. is the seasonality in IBM

4. what will be the best target : percent_change_price

5. are there any statistical relationships between percent change price and other features

### Planning

#### To prepare this data i used the following steps

1. Acquire the data using built functions

2. Clean and split data using built functions

3. Use matplotlib, seaborn, and dtale for exploratory data analysis

4. Find possible relational predictors

5. Create baseline 

6. Start modeling using selected features, with OLS, lasso lars, and polynomial models

7. Choose the best model and test ()

### How to Reproduce

to reproduce this project you will need to: 

- have a copy of dow_jones.csv

- clone this repository

- use the functions in .py files to acquire and clean data

- used libraries are numpy, pandas, matplotlib, seaborn, darts and sklearn


## Conclusion:

## Takeaway:

- The model is not great

- there is not enough data to fit and make proper predictions for a time series

- A regression model may have been a better coice for this data set

## Recomendations:

- hold of on implimentation until a better model is built

- Collect more data


## Next Steps:

- Clustering and regression modeling is a good choice for future work

- research other methods of time series analysis




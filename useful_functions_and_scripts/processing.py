# Functions to help with data processing 

import pandas as pd
import numpy as np

# Function to calulate a rolling average on input columns with a given averaging window 

def rolling_mean(dataframe,cols_for_smoothing,window_for_smoothing):
    
    df = dataframe.copy() # Copy so you don't automatically over-write the input dataframe
    
    # Group by country so you only smooth intra-country values (don't accidentally blend across countries where one ends and another begins)
    df[cols_for_smoothing] = df.groupby('Country')[cols_for_smoothing].rolling(window_for_smoothing,center=True).mean().reset_index(drop=True)
    
    return df


# Function to calculate additional COVID-19 outbreak metrics and add the new columns to existing dataframe 

def calculate_more_COV_metrics(input_dataframe):
    
    dataframe = input_dataframe.copy() # Copy so you don't automatically over-write the input dataframe 
    
    # Take difference of new deaths column 
    dataframe['new_deaths_diff'] = dataframe.groupby('Country')['new_deaths'].diff().fillna(0)
    # (replace with NaN everywhere the new deaths column is NaN, since it doesn't make sense to calculate a "difference" here)
    dataframe.loc[dataframe['new_deaths'].isna(),'new_deaths_diff'] = np.nan
    
    # Take difference of new deaths per million column
    dataframe['new_deaths_per_million_diff'] = dataframe.groupby('Country')['new_deaths_per_million'].diff().fillna(0)
    dataframe.loc[dataframe['new_deaths_per_million'].isna(),'new_deaths_per_million_diff'] = np.nan
    
    # Calculate percent changes for total deaths 
    dataframe['total_deaths_pctchange'] = dataframe['total_deaths'].pct_change()*100 # calc pct change, multiply by 100 to get in %
    dataframe['total_deaths_pctchange'].replace([np.inf, -np.inf], np.nan,inplace=True) # replace all infinite values with nans
    dataframe['total_deaths_pctchange'].fillna(value=0, inplace=True) # fill nans with zeros 
    dataframe['total_deaths_pctchange'].clip(upper=1000,inplace=True) # clip the results because some values are extremely high and skew later analyses
    dataframe.loc[dataframe['total_deaths'].isna(),'total_deaths_pctchange'] = np.nan # replace with NaN everywhere the total deaths column is NaN, since it doesn't make sense to calculate a "pct change" here

    # Calculate percent changes for total deaths per million
    dataframe['total_deaths_per_million_pctchange'] = dataframe['total_deaths_per_million'].pct_change()*100
    dataframe['total_deaths_per_million_pctchange'].replace([np.inf, -np.inf], np.nan,inplace=True)
    dataframe['total_deaths_per_million_pctchange'].fillna(value=0, inplace=True)
    dataframe['total_deaths_per_million_pctchange'].clip(upper=1000,inplace=True)
    dataframe.loc[dataframe['total_deaths_per_million'].isna(),'total_deaths_per_million_pctchange'] = np.nan
    
    # Calculate percent changes for new deaths 
    dataframe['new_deaths_pctchange'] = dataframe['new_deaths'].pct_change()*100
    dataframe['new_deaths_pctchange'].replace([np.inf, -np.inf], np.nan,inplace=True)
    dataframe['new_deaths_pctchange'].fillna(value=0, inplace=True)
    dataframe['new_deaths_pctchange'].clip(upper=1000,inplace=True) 
    dataframe.loc[dataframe['new_deaths'].isna(),'new_deaths_pctchange'] = np.nan
    
    # Calculate percent changes for new deaths per million
    dataframe['new_deaths_per_million_pctchange'] = dataframe['new_deaths_per_million'].pct_change()*100
    dataframe['new_deaths_per_million_pctchange'].replace([np.inf, -np.inf], np.nan,inplace=True)
    dataframe['new_deaths_per_million_pctchange'].fillna(value=0, inplace=True)
    dataframe['new_deaths_per_million_pctchange'].clip(upper=1000,inplace=True)
    dataframe.loc[dataframe['new_deaths_per_million'].isna(),'new_deaths_per_million_pctchange'] = np.nan
    
    return dataframe 

# Import necessary libraries
import pandas as pd
import numpy as np

# Function to compute given number of quantiles for each input column in the given dataframe 
def quantile_function(input_dataframe,cols_for_quant,num_quantiles):
    
    dataframe = input_dataframe.copy() # Copy so you don't automatically over-write the input dataframe
    
    for col in cols_for_quant: # loop through each input column  
        # Use qcut to break given column into quantiles with equal number of samples in each bin -> save as column name + _q
        dataframe[col + '_q'] = pd.qcut(dataframe[col],q=num_quantiles,labels=False,duplicates='drop')
    return dataframe 
    
# Function to return new datasets, each with different numbers of quantiles per variable based upon the inputs 
def quantile_function_looper(input_dataframe,cols_for_quant,quantiles_list):
    
    dataframe = input_dataframe.copy() # Copy so you don't automatically over-write the input dataframe
    
    dfs_with_quantiles = [] # Initialize a list for storing outputs (dataframes that we've computed quantiles for)
    
    # Loop through list with desired number of quantiles 
    for i in range(len(quantiles_list)):
        
        dataframe_quantiled = quantile_function(dataframe,cols_for_quant,quantiles_list[i]) # Compute given # of quantiles on the dataframe

        dfs_with_quantiles.append(dataframe_quantiled) # Store the resulting quantiled dataframe in the list 
    
    Quantiled_Dataframes = pd.concat(dfs_with_quantiles, axis=1, keys=quantiles_list) # Concatenate everything
    
    return Quantiled_Dataframes
    
# Function to compute given number of quantized bins for each input column in the given dataframe 
def binning_function(input_dataframe,cols_for_binning,num_bins):
    
    dataframe = input_dataframe.copy() # Copy so you don't automatically over-write the input dataframe
    
    for col in cols_for_binning: # loop through each input column  
        # Use cut to break given column into bins with equal spacing between each bin -> save as column name + _q
        dataframe[col + '_q'] = pd.cut(dataframe[col],bins=num_bins,labels=False,duplicates='drop')
    return dataframe 

# Function to return new datasets, each with different numbers of bins per variable based upon the inputs 
def binning_function_looper(input_dataframe,cols_for_binning,bins_list):
    
    dataframe = input_dataframe.copy() # Copy so you don't automatically over-write the input dataframe
    
    dfs_with_bins = [] # Initialize a list for storing outputs (dataframes that we've computed bins for)
    
    # Loop through list with desired number of bins 
    for i in range(len(bins_list)):
        
        dataframe_binned = binning_function(dataframe,cols_for_binning,bins_list[i]) # Compute given # of bins on the dataframe

        dfs_with_bins.append(dataframe_binned) # Store the resulting binned dataframe in the list 
    
    Binned_Dataframes = pd.concat(dfs_with_bins, axis=1, keys=bins_list) # Concatenate everything
    
    return Binned_Dataframes

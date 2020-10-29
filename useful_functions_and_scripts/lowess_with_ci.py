import pandas as pd 
import statsmodels.api as sm

def lowess_with_ci(dataset, xcol, ycol, n_boot, ):
  
  # Instantiate the lowess model  
  lowess = sm.nonparametric.lowess

  # Get input and output data vectors 
  df = dataset.dropna().copy(); input=df[xcol]; output=df[ycol] 

  # Dataframe to be used for index matching (bootstrapping uses sampling with replacement, so you'll have duplicates of some indices and missing values at other indices, need a way to match back with original df)
  df_for_index_matching = df[input.name].reset_index()

  # Number of bootstraps and number of samples for each bootstrap (equal to number of samples in vector) 
  n_boot=5; n=len(output)

  bootstrapped_lowess_fits = [] # to hold all of the index-matched lowess fits on the resampled datasets 
  
  rng = np.random.default_rng(None) # random number generator 
  
  for i in range(int(n_boot)): 
  
    resampler = rng.integers(0, n, n, dtype=np.intp) # get random indices -> use these to extract index-matched pairs of xvals and yvals from your input and output vectors 

    resampled_output = output.take(resampler, axis=0) # extract resampled outputs (w/ replacement)

    resampled_input = input.take(resampler, axis=0) # extract resampled inputs (w/ replacement)

    lowess_on_resampled_data = lowess(endog=resampled_output,exog=resampled_input) # use resampled (w/ replacement) dataset to compute a new lowess fit 

    lowess_on_resampled_data_df = pd.DataFrame(data=lowess_on_resampled_data,columns=['input','predicted_output']).set_index('input').drop_duplicates().reset_index() # turn the array into a labeled dataframe and drop duplicated inputs (since you sample with replacement, you'll have duplicated inputs)

    lowess_matched_to_original_data_indices = df_for_index_matching.merge(lowess_on_resampled_data_df.rename(columns={'input':input.name}),how='left')['predicted_output'] # Use the original data vector to match the lowess to the right indices (since you sample with replacement and therefore don't use all of the unique input values)

    bootstrapped_lowess_fits.append(lowess_matched_to_original_data_indices) # Add the index-matched lowess fit to the list 

  full_lowess = pd.DataFrame(lowess(endog=output,exog=input),columns=[input.name,'predicted_output_full']) # final lowess fitting on the entire dataset (no bootstrapping/resampling, use all datapoints once) 

  full_lowess = df_for_index_matching.merge(full_lowess,how='left',on=input.name).drop(columns='index') # Need to match the lowess results to the right index (and corresponding input value) 

  lowess_with_bootstrap = pd.concat([full_lowess,pd.concat(bootstrapped_lowess_fits,axis=1)],axis=1) # Combine the full (all datapoints) lowess fit with the bootstrapped (subsampled) lowess fits 

  lowess_with_bootstrap.loc[:,'uppercl'] = lowess_with_bootstrap.iloc[:,1:].quantile(q=0.975,axis=1) # get the 97.5 percentile for the bootstrapped fits (upper bound for 95% ci)

  lowess_with_bootstrap.loc[:,'lowercl'] = lowess_with_bootstrap.iloc[:,1:].quantile(q=0.025,axis=1) # get the 2.5 percentile for the bootstrapped fits (lower bound for 95% ci)

  lowess_with_bootstrap.sort_values(by=input.name,inplace=True) # sort the values by input so that the fill_between function works properly 

  from scipy.signal import savgol_filter

  lowess_with_bootstrap.loc[:,'uppercl_smooth'] = savgol_filter(lowess_with_bootstrap['uppercl'], 15, 2) # smooth the upper confidence interval 

  lowess_with_bootstrap.loc[:,'lowercl_smooth'] = savgol_filter(lowess_with_bootstrap['lowercl'], 15, 2) # smooth the lower confidence interval 

  return lowess_with_bootstrap[[input.name,'predicted_output_full','uppercl','lowercl','uppercl_smooth','lowercl_smooth']]

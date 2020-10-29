import pandas as pd 
#need make_lags and lagged_var_df functions as well 

def lagged_correlations(dataframe,merging_var,variable,num_lags,COVIDstats):

  df = dataframe.copy()

  df_lagged = lagged_var_df(df,merging_var,variable,num_lags,COVIDstats)

  corr = df_lagged[df_lagged['Days From 5th Death'].ge(-7)].corr(method='spearman')

  trimmed = corr.iloc[1:num_lags+2,num_lags+2:].reset_index()

  return corr,trimmed
  
def lagged_correlations_plot(dataframe,merging_var,variable,num_lags,COVIDstats):

  df = dataframe.copy()

  corr,trimmed = lagged_correlations(df,merging_var,variable,num_lags,COVIDstats)

  fig,ax = plt.subplots(figsize=(10,10))

  for covstat in COVIDstats:
    if covstat not in ('Country','Days From 5th Death'):
      #print(covstat)
      trimmed[covstat].plot(ax=ax)
  plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
  plt.title(variable)
  plt.xlabel('Lags')
  plt.ylabel('Correlation')
  plt.gca().invert_xaxis()
  fig.show()

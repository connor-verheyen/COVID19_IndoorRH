def calc_growthrates(dataframe,variables,num_vars):

  if num_vars>1:
    for variable in variables:
      dataframe[variable+'_rate'] = dataframe[variable].pct_change().add(1)
  else: 
    dataframe[variables+'_rate'] = dataframe[variables].pct_change().add(1)

import pandas as pd 

# Function to plot the ranked correlations between a given input variable and all other variables in the dataset 

def ranked_correlations(dataframe,variable,method):

  df = dataframe.copy()
  
  ranked = df.corr(method=method)[variable].sort_values(ascending=False).reset_index() # Compute pairwise correlations and rank them 
  
  fig,ax = plt.subplots(figsize=(24,4))
  ranked.plot(kind='bar',x='index',y=variable,ax=ax,legend=False) # Plot the correlations
  ax.set_title('Correlations with {} ({})'.format(variable,method))
  ax.set_xlabel('')
  [spine.set_color('black') for ax in plt.gcf().axes for spine in ax.spines.values()]
  [spine.set_linewidth(1) for ax in plt.gcf().axes for spine in ax.spines.values()]

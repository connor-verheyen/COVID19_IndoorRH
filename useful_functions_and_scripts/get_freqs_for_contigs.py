import pandas as pd 

# Get all of the frequencies (counts) for control_outcome1, control_outcome2, exposure_outcome1, and exposure_outcome2

def get_freqs_for_contigs(dataset,outcome,treatment):
  
  data = dataset[[outcome,treatment]].copy() # Copy dataset 

  contig_table = pd.crosstab(data[outcome],data[treatment]).iloc[::-1,]

  suboptimalRH_WorseOutcome = contig_table.loc[1,0]
  
  suboptimalRH_BetterOutcome = contig_table.loc[0,0]

  optimalRH_WorseOutcome = contig_table.loc[1,1]
  
  optimalRH_BetterOutcome = contig_table.loc[0,1]

  return suboptimalRH_WorseOutcome,suboptimalRH_BetterOutcome,optimalRH_WorseOutcome,optimalRH_BetterOutcome

# Test the function 
#get_freqs_for_contigs(dataset=treat_total,outcome='new_cases_Qlevels',treatment='quantized_IndRH')

# input a stratified table (statsmodels object) and get all of the stratified statistics you're interested in 

def stratified_stats(st): 
  pooled_OR = st.oddsratio_pooled

  pooled_OR_lowerCI = st.oddsratio_pooled_confint()[0]

  pooled_OR_upperCI = st.oddsratio_pooled_confint()[1]

  breslow_day_pval = st.test_equal_odds().pvalue # Test that all odds ratios are identical. This is the ‘Breslow-Day’ testing procedure.

  breslow_day_statistic = st.test_equal_odds().statistic # The chi^2 test statistic

  mantel_haenszel_pval = st.test_null_odds().pvalue # Test that all tables have odds ratio equal to 1. This is the ‘Mantel-Haenszel’ test.

  mantel_haenszel_statistic = st.test_null_odds().statistic # The chi^2 test statistic

  return pooled_OR, pooled_OR_lowerCI, pooled_OR_upperCI, breslow_day_pval, breslow_day_statistic, mantel_haenszel_pval, mantel_haenszel_statistic

# To run the function, just input a previously constructed statsmodels stratified table 
#stratified_stats(st=st)

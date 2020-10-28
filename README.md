# COVID19_IndoorRH
Investigating the Potential Effect of Indoor Climate on Global COVID-19 Outcomes

## Project Abstract 
Globally, the COVID-19 pandemic has resulted in over forty million confirmed cases and over one million confirmed deaths. The spread and severity of COVID-19 has not been uniform, with considerable inter-country differences in epidemic magnitude. This regional heterogeneity spurred intense investigation into COVID-19 seasonality, but thus far the conclusions have been mixed. Some studies reported a modest dependence of COVID-19 on external weather conditions, while other studies failed to find such a relationship. Because humans spend the vast majority of their time indoors, we hypothesized that indoor climate, rather than outdoor climate, may be a more relevant modulator of COVID-19 outbreaks. We compiled COVID-19 statistics and meteorological measurements from 121 countries around the globe, representing the Northern Hemisphere, Southern Hemisphere, and Tropics. We extrapolated the indoor climate and found clear regional variation in indoor relative humidity (RH), along with clear regional variation in COVID-19 dynamics. Through timeseries visualization, robust linear modeling, and robust lowess smoothing, we observed consistent regional relationships between COVID-19 outbreaks and indoor climate across a range of potential time lags. We then discovered systematic differences in the indoor RH between relatively worse and relatively better COVID-19 outcomes. Finally, we demonstrated that intermediate indoor relative humidity (between 40\% and 60\%) was associated with significantly decreased odds of worse COVID-19 outcomes, and that this relationship was maintained even when controlling for COVID-19 government response measures. Taken together, these results suggest that indoor climate conditions may modulate the spread and severity of COVID-19.

![Hypothesis](/main_figures/Figure_COVID19_IndoorHumidityHypothesisOverview.png)


## Repository Structure and Contents

### data 
Folder that stores the compiled datasets used in the project. 

1. 7DaySmooth_ALLVars_Dataset_2020_08_10_GE50_Deaths.xlsx
   * This is the main dataset for this study. Used for the main text and most of the supplemental material. 
2. Raw Dataset = 'PADDED_Dataset_2020_08_10_GE50_Deaths.xlsx
   * This is the raw dataset (no smoothing applied). 
3. 3DaySmooth_ALLVars_Dataset_2020_08_10_GE50_Deaths.xlsx
   * This is an alternative dataset (3-day rolling avg applied vs. 7-day rolling avg for main dataset). 
4. 7DaySmooth_ALLVars_Dataset_2020_10_19_GE100_Deaths.csv
   * This is the most recently retrieved dataset, used for confirmation of the study results. 

### main_figures 
Folder that stores the IPython notebook containing all of the figures and figure subsets presented in the main text of the paper. 

1. Figures_For_Main_Text.ipynb

### supplementary_analysis
Folder that stores all of the IPython notebooks that contain supplemental analyses and supporting information for the paper. 

1.  Supplementary_Material_1__Rerun_Analysis_With_New_Data.ipynb
2.  Supplementary_Material_2___Full_Analysis_With_New_Cases_And_Global_Data.ipynb
3.  Supplementary_Material_3__Additional_Information_For_Regressions.ipynb
4.  Supplementary_Material_4__Additional_Analysis_Of_Govt_Responses.ipynb
5.  Supplementary_Material_5__Sensitivity_Modifying_Analytical_Windows_For_Outbreaks.ipynb
6.  Supplementary_Material_6__Sensitivity_Modifying_Assumed_Thermal_Comfort_Zone.ipynb
7.  Supplementary_Material_7__Sensitivity_Modifying_Optimal_Indoor_Climate_Window.ipynb
8.  Supplementary_Material_8__Analyzing_Regional_Variability_In_Tropics.ipynb
9.  Supplementary_Material_9__Analyzing_Outdoor_Weather_Variables.ipynb
10. Supplementary_Material_10_Analyzing_Effects_of_Data_Processing.ipynb
11. Supplementary_Material_11_Accounting_For_Outdoor_Weather_Conditions.ipynb

### useful_functions_and_scripts 
Folder that stores various snippets of code that were useful for the project 

1. 

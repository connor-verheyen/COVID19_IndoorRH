# Associations between indoor relative humidity and global COVID-19 outcomes

## Project Abstract 

![Hypothesis](/main_text/screenshot_fig1_for_github.png)


## Repository Structure and Contents

### data 
Folder that stores the compiled datasets used in the project. 
1. Main text dataset
   * This is the primary dataset for this study. Used for the main text as well as many supplemental analyses. 
2. Supplementary data sub-directory 
   * Follow-up validation datasets (to confirm the main study conclusions with newer datasets collected Dec 2020 and Jan 2021)  
   * Alternatively-processed datasets (to evaluate the effect of different upstream data pre-processing steps)
   * Outdoor and indoor climate datasets (to validate the indoor relative humidity extrapolation workflow)  

### main_text
Folder that stores the IPython notebook and the finalized figures for the analysis presented in the main text of the paper. 
1. Main_Text_Figures_and_Stats

### supplementary_analysis
Folder that stores all of the IPython notebooks that contain supplemental analyses and supporting information for the paper. 

1. Supplementary_Section_01__Modifying_Assumed_Thermal_Comfort_Zone
   * We explored how changing the assumed indoor thermal comfort zone modified the resulting indoor RH and ultimately the relationships between indoor RH and COVID-19. 
2. Supplementary_Section_02__Modifying_Optimal_Indoor_Climate_Window
   * We investigated how changing the assumed optimal RH range (in the main text, 40% to 60%) modified observed relationships between indoor RH and COVID-19. 
3. Supplementary_Section_03__Analyzing_Outdoor_Weather_Variables
   * We explored the relationships between outdoor weather variables and COVID-19 statistics using the same set of analytical approaches from the main text. 

Section 4: We performed a full analysis of indoor and outdoor data collected in various types of buildings (e.g. medical, residential) during cold months of the year and provide a comprehensive validation of our indoor RH extrapolation workflow. 
Supplementary Text 
Figs. S13 to S20 
•	Supplementary_Section_04__Validating_Humidity_Extrapolation_Workflow

Section 5: We studied further stratifications in the tropical regions of the globe. 
Supplementary Text 
Figs. S21 to S23 
•	Supplementary_Section_05__Analyzing_Regional_Variability_In_Tropics

Section 6: We dove further into regionally- and temporally-varying national COVID-19 policies and investigated more granular stratifications by government response. 
Supplementary Text 
Figs. S24 to S25 
•	Supplementary_Section_06__Additional_Analysis_Of_Govt_Responses

Section 7: We provide the full set of results obtained when assessing indoor humidity exposure while controlling for outdoor weather conditions. 
Supplementary Text 
Figs. S26 to S29 
•	Supplementary_Section_07_Accounting_For_Outdoor_Weather_Conditions

Section 8: We provide a more comprehensive study which was partially cut from the main text for brevity. This includes the results from our linear modeling as well as the results obtained when using daily COVID-19 cases as a dependent variable for the odds ratio analysis. 
Supplementary Text 
Figs. S30 to S32 
•	Supplementary_Section_08__Full_Analysis_With_Cases_And_Global_Data

Section 9: We retrieved and processed new datasets on December 3rd, 2020 and January 27, 2021 to obtain updated COVID-19 statistics and meteorological data. We repeated the analysis from the main text to confirm the validity of our main conclusions. 
Supplementary Text 
Figs. S33 to S34 
•	Supplementary_Section_09__Repeat_Analysis_With_Dec_Jan_Data

Section 10: We explored how parameter modifications in the regression algorithms altered the fitted models and also provide scatter plots of underlying data and residuals.
Supplementary Text 
Figs. S35 to S36 
•	Supplementary_Section_10__Additional_Information_For_Regressions

Section 11: We examined how changing the analytical window of the normalized timeline modified the observed relationships between indoor RH and COVID-19. 
Supplementary Text 
Figs. S37 to S39 
•	Supplementary_Section_11__Sensitivity_Modifying_Outbreak_Analytical_Windows

Section 12: We examined the effects of different data pre-processing strategies on the final results and conclusions of the study. 
Supplementary Text 
Figs. S40 to S41 
•	Supplementary_Section_12_Analyzing_Effects_of_Data_Processing

Section 13: We provide results from statistical hypothesis tests as well as the bounds of the quantized data used in Figures 4 and 5 of the main text. 
Supplementary Text 
Tables. S1 to S8 
•	Embedded within the notebook for the figures in the main text 


### useful_functions_and_scripts 
Folder that stores various snippets of code that were useful for different parts of the project 

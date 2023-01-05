# Associations between indoor relative humidity and global COVID-19 outcomes

*This repository contains code, data, and SI Material for the paper:
C. A. Verheyen and  L. Bourouiba (2022) Associations between indoor relative humidity and global COVID-19 outcomes. Journal of the Royal Society Interface, doi.10.1098/rsif.2021.0856.*

*Citation:
Please cite C. A. Verheyen and  L. Bourouiba (2022) Associations between indoor relative humidity and global COVID-19 outcomes. Journal of the Royal Society Interface, doi.10.1098/rsif.2021.0856. when using any part of this repository or associated Zenodo.*


Journal article: 
[![DOI](https://zenodo.org/badge/DOI/10.1098/rsif.2021.0856.svg)](https://doi.org/10.1098/rsif.2021.0865)


Zenodo code/data archive: 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7195704.svg)](https://doi.org/10.5281/zenodo.7195704)



## Project Abstract 
Globally, the spread and severity of COVID-19 has been distinctly non-uniform. Seasonality was suggested as a contributor to regional variability, but the relationship between weather and COVID-19 remains unclear and the focus of attention has been paid to outdoor conditions. Because humans spend most of their time indoors and because most transmission  occurs indoors, we here, instead, investigate the hypothesis that indoor climate – particularly indoor relative humidity (RH) – may be the more relevant modulator of outbreaks. To study this association, we combined population-based COVID-19 statistics and meteorological measurements from 121 countries. We rigorously processed epidemiological data to reduce bias, and developed and experimentally validated with direct data collection a computational workflow to estimate indoor conditions based on outdoor weather data and well documented and standard  indoor comfort conditions. Our comprehensive analysis showed robust and systematic relationships between regional outbreaks and indoor RH. In particular, we found intermediate RH (40%-60%) to be robustly associated with better COVID-19 outbreak outcomes (vs. RH <40% or >60%). Together, these results suggest that indoor conditions, particularly indoor RH modulate the spread and severity of COVID-19 outbreaks. 

![Hypothesis](/main_text/screenshot_fig1_for_github.png)

## Repository Structure and Contents

### data 
Folder that stores the compiled datasets used in the project. 

1. Main text dataset
   * 7DaySmooth_ALLVars_Dataset_2020_08_10_GE50_Deaths
   * This is the primary dataset for this study
   * Used for the main text and several supplemental analyses

2. Supplementary data sub-folder 
   * Follow-up validation datasets (to confirm the main study conclusions with newer datasets collected Dec 2020 and Jan 2021)  
   * Alternatively-processed datasets (to evaluate the effect of different upstream data pre-processing steps)
   * Outdoor and indoor climate datasets (to validate the indoor relative humidity extrapolation workflow with experimental measurements)  

### main_text
Folder that stores the IPython notebook and the finalized figures for the analysis presented in the main text of the paper. 

1. Main_Text_Figures_and_Stats 
2. Figure 1 - Graphical abstract and description and validation of indoor humidity estimation workflow
3. Figure 2 - Geospatial and temporal variability in ambient conditions and COVID-19 outbreaks
4. Figure 3 - Predicting the dependency of COVID-19 on indoor relative humidity
5. Figure 4 - Intermediate indoor relative humidity is significantly associated with better COVID-19 outcomes
6. Figure 5 - The association between intermediate indoor RH and better COVID-19 outcomes is robust

### supplementary_analysis
Folder that stores all of the IPython notebooks that contain supplemental analyses and supporting information for the paper. 

1. Supplementary_Section_01__Modifying_Assumed_Thermal_Comfort_Zone
   * We explored how changing the assumed indoor thermal comfort zone modified the resulting indoor RH and ultimately the relationships between indoor RH and COVID-19. 

2. Supplementary_Section_02__Modifying_Optimal_Indoor_Climate_Window
   * We investigated how changing the assumed optimal RH range (in the main text, 40% to 60%) modified observed relationships between indoor RH and COVID-19. 

3. Supplementary_Section_03__Analyzing_Outdoor_Weather_Variables
   * We explored the relationships between outdoor weather variables and COVID-19 statistics using the same set of analytical approaches from the main text. 

4. Supplementary_Section_04__Validating_Humidity_Extrapolation_Workflow
   * We performed a full analysis of indoor and outdoor data collected in various types of buildings (e.g. medical, residential) during cold months of the year and provide a comprehensive validation of our indoor RH extrapolation workflow. 

5. Supplementary_Section_05__Analyzing_Regional_Variability_In_Tropics
   * We studied further stratifications in the tropical regions of the globe. 

6. Supplementary_Section_06__Additional_Analysis_Of_Govt_Responses
   * We dove further into regionally- and temporally-varying national COVID-19 policies and investigated more granular stratifications by government response. 

7. Supplementary_Section_07_Accounting_For_Outdoor_Weather_Conditions
   * We provide the full set of results obtained when assessing indoor humidity exposure while controlling for outdoor weather conditions.  

8. Supplementary_Section_08__Full_Analysis_With_Cases_And_Global_Data
   * We provide a more comprehensive study which was partially cut from the main text for brevity. This includes the results from our linear modeling as well as the results obtained when using daily COVID-19 cases as a dependent variable for the odds ratio analysis. 

9. Supplementary_Section_09__Repeat_Analysis_With_Dec_Jan_Data
   *  We retrieved and processed new datasets on December 3rd, 2020 and January 27, 2021 to obtain updated COVID-19 statistics and meteorological data. We repeated the analysis from the main text to confirm the validity of our main conclusions. 

10. Supplementary_Section_10__Additional_Information_For_Regressions
    * We explored how parameter modifications in the regression algorithms altered the fitted models and also provide scatter plots of underlying data and residuals.

11. Supplementary_Section_11__Sensitivity_Modifying_Outbreak_Analytical_Windows
    * We examined how changing the analytical window of the normalized timeline modified the observed relationships between indoor RH and COVID-19. 

12. Supplementary_Section_12_Analyzing_Effects_of_Data_Processing
    * We examined the effects of different data pre-processing strategies on the final results and conclusions of the study. 

13. (no corresponding notebook, statistics and quantization information is embedded in the main text notebook Main_Text_Figures_and_Stats)
    * We provide results from statistical hypothesis tests as well as the bounds of the quantized data used in Figures 4 and 5 of the main text. 

### useful_functions_and_scripts 
Folder that stores various snippets of code that were useful for different parts of the project 

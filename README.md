# DVA-Project: NYC Collision Analysis Team 169
# Description (WIP)
This package reads in the NYC Collision dataset and imputes zipcodes, adds weather information, and creates predictive models with fatal crashes as the target variable.

Weather data source is found here:
https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table

Filename: climate.gov

NY weather data description: GHCND_documentation.pdf

# Installation
- Download the NYC dataset here: 
    
        https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data

- Save `Motor_Vehicle_Collisions_-_Crashes.csv` under the `data` folder.

## Building and using environment
To create environment, run `conda env create -f builds/environment.yml` at the root directory and then activating it via `conda activate dva`.

Example:
```bash
conda env create -f builds/environment.yml
conda activate dva
```

# Execution
You can run the following to produce the desired files:
- Run `conda run -n dva python demo.py` to produce `df_demo.csv`
- Run `data_cleaning.ipynb` to produce `cleaned_data.csv`
- Run `Vehicle Regroup, Rush_hour, Weekday, Season.ipynb` to produce `cleaned_data_updated.csv`
- Run `DVA Model - 20250406.ipynb` to produce `data_with_predictions.csv`

`data_with_predictions.csv` is a munged dataset with the predictions for fatal crashes.

## Visualizations
The provided interactive heatmaps and choropleths are located in:
```bash
Visualization\output\Choropleth_Prediction_Accuracy_By_ZIP.html
Visualization\output\NYC_Accident_Heatmap_with_Boroughs.html
Visualization\output\NYC_Accident_Heatmap_with_ZIP.html
Visualization\output\NYC_Crash_Severity_Choropleth.html
```
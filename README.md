# DVA-Project: Analyzing New York’s Motor Vehicle Collision Data to Identify Key Factors in Fatal Crashes (Team 169, CSE6242 Spring 2025)
# Description 
Fatal vehicle collisions impose a major burden on NYC. Traditional methods often overlook key factors like time, weather, and location. This project leverages them to help traffic authorities anticipate high-risk scenarios and allocate resources more effectively, which will improve road safety city-wide.

This package processes the NYC Collision dataset by imputing missing zip codes, integrating weather data, conducting spatial analyses such as heat maps, and building predictive models with fatal crashes as the target variable.

# Data:
Data folder contains all datasets used by the codes.

The primary dataset, "City of New York Motor Vehicle Collisions," covers data from 2014 and is updated daily. Due to file size limitations, please refer to the Installation section for instructions on downloading and saving the dataset.

The weather data source: https://www.climate.gov/maps-data/dataset/past-weather-zip-code-data-table

Filenames: `data/NY Weather 20xx-20xx.csv` (climate.gov)

NY weather data description: `data/GHCND_documentation.pdf`

# Installation
- Download the NYC dataset here: 
    https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data
- Save `Motor_Vehicle_Collisions_-_Crashes.csv` under the `data` folder.
- This package uses Python and Jupyter Notebook. Please ensure both are installed before running the code via conda below:

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

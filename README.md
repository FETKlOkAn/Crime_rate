# Victimization Rates Analysis

This repository contains a Python script for analyzing victimization rates by region based on a dataset. The analysis includes data cleaning, statistical testing, and visualization of victimization rates across different areas.

## Dataset

The dataset used in this project is `analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv`. It includes the following columns:

- `Area_unit_2013_code`
- `Area_unit_2013_label`
- `Victimisations_calendar_year_2015`
- `Population_mid_point_2015`
- `Rate_per_10000_population`
- `Rate_ratio_NZ_average_rate`
- `Urban_area_2013_code`
- `Urban_area_2013_label`
- `Urban_area_type`
- `Territorial_authority_area_2013_code`
- `Territorial_authority_area_2013_label`
- `Region_2013_code`
- `Region_2013_label`

## Analysis Steps

### Data Cleaning

1. Strip leading and trailing whitespaces from column names.
2. Remove commas and replace non-numeric values like `-` and empty strings with `0`.
3. Convert the `Rate_per_10000_population` column to numeric values.

### Statistical Analysis

1. Calculate the national average victimization rate.
2. Perform a two-sample t-test to determine if there is a significant difference in victimization rates between areas above and below the national average.

### Visualization

1. Plot the victimization rates for areas above the national average.
2. Highlight areas with the highest rates and those that are above the 75th percentile.

## Results

- **T-test Statistic:** 8.3555
- **P-value:** 0.0000
- **Conclusion:** Reject the null hypothesis. There is a significant difference in victimization rates between areas above and below the national average.

### Areas with High Victimization Rates

Below are some of the areas with the highest victimization rates:

| Area                | Rate per 10,000 Population |
|---------------------|-----------------------------|
| Highbrook           | 5750                        |
| Cathedral Square    | 5351                        |
| Middlemore          | 4818                        |
| Whangarei Central   | 3107                        |
| Harbourside         | 2667                        |

## Plot

The plot displays the victimization rates for areas above the national average, with a line indicating the 75th percentile of the victimization rate.

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy
- scipy

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/FETKlOkAn/Crime_rate.git

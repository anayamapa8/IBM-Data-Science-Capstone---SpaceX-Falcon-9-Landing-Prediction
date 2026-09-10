# SpaceX Falcon 9 Landing Prediction

A data science capstone project that predicts whether the SpaceX Falcon 9 first stage will land successfully. This project was completed as part of the IBM Data Science Professional Certificate on Coursera.

---

## Project Overview

SpaceX advertises Falcon 9 rocket launches at a cost of 62 million dollars, while other providers cost upwards of 165 million dollars. Much of the savings come from reusing the first stage of the rocket. Therefore, predicting whether the first stage will land successfully is valuable for estimating launch costs.

This project uses data from the SpaceX API and web scraping to build a classification model that predicts landing success.

---

## Repository Contents

### Notebooks and Scripts

| File | Description |
|------|-------------|
| `IBM Course 10 - Module 1 - A - Data Collection API Lab.ipynb` | Collects launch data from the SpaceX API and prepares the initial dataset |
| `IBM Course 10 - Module 1 - B - Data Collection with Web Scraping lab.ipynb` | Scrapes Falcon 9 launch records from Wikipedia using BeautifulSoup |
| `IBM Course 10 - Module 1 - C - Data Wrangling.ipynb` | Cleans, filters, and prepares data for analysis and modeling |
| `IBM Course 10 - Module 2 - A - EDA with SQL.ipynb` | Runs SQL queries to answer key questions about the launch data |
| `IBM Course 10 - Module 2 - B - EDA with Visualization Lab.ipynb` | Explores relationships through scatter plots, bar charts, and line charts |
| `IBM Course 10 - Module 3 - A - Interactive Visual Analytics with Folium lab.ipynb` | Builds interactive maps to visualize launch sites and landing outcomes |
| `IBM Course 10 - Module 3 - B - Build an Interactive Dashboard with Plotly Dash.py` | Creates an interactive dashboard with dropdowns, sliders, and charts |
| `IBM Course 10 - Module 4 - A - Machine Learning Prediction lab.ipynb` | Trains and evaluates four classification models to predict landing success |

### Supporting Files

The folder `py, db, csv and png support files` contains:

- Python scripts used to generate flowcharts and dashboards
- CSV datasets used throughout the project
- SQLite database file (`C10M2_my_data1.db`)
- PNG images of flowcharts, charts, and maps used in the presentation

---

## Methodology

1. **Data Collection**
   - Retrieved launch data from the SpaceX REST API
   - Scraped additional launch records from a static Wikipedia page
   - Combined both sources into a unified dataset

2. **Data Wrangling**
   - Filtered out multi-core and multi-payload launches
   - Extracted single IDs from list columns
   - Handled missing values in payload mass
   - Encoded categorical variables using one-hot encoding
   - Standardized numerical features

3. **Exploratory Data Analysis**
   - Used SQL queries to answer key questions about launch sites, payloads, and outcomes
   - Created visualizations to explore flight number, payload mass, orbit type, and yearly trends

4. **Interactive Visual Analytics**
   - Built a Folium map with launch site markers, color-coded landing outcomes, and distance calculations
   - Created a Plotly Dash dashboard with a dropdown, range slider, pie chart, and scatter plot

5. **Predictive Analysis**
   - Trained four classification models: Logistic Regression, SVM, Decision Tree, and KNN
   - Tuned hyperparameters using GridSearchCV with 10-fold cross-validation
   - Evaluated models on test data using accuracy scores and confusion matrices

---

## Key Results

| Model | CV Accuracy | Test Accuracy | Gap |
|-------|-------------|---------------|-----|
| Logistic Regression | 85.0% | 83.3% | 1.7% |
| SVM | 86.4% | 83.3% | 3.1% |
| Decision Tree | 90.5% | 83.3% | 7.2% |
| KNN | 86.4% | 77.8% | 8.7% |

**Best Model: Logistic Regression** with 83.3% test accuracy and the smallest gap between CV and test accuracy (1.7%), indicating the best generalization.

---

## Technologies Used

| Category | Tools |
|----------|-------|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly Express |
| Interactive Maps | Folium |
| Dashboard | Plotly Dash |
| Database | SQLite, SQL |
| Web Scraping | Requests, BeautifulSoup |
| Machine Learning | Scikit-learn (Logistic Regression, SVM, Decision Tree, KNN, GridSearchCV) |
| Environment | Jupyter Notebooks, VS Code |

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/spacex-capstone-project.git

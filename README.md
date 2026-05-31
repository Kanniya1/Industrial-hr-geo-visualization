# Industrial Human Resource Geo-Visualization

## Project Overview

The Industrial Human Resource Geo-Visualization project aims to analyze and visualize the distribution of industrial workers across different sectors and geographical regions in India. The project focuses on the classification of main and marginal workers by industry type, gender, and workforce category to provide meaningful insights for employment planning and resource management.

## Problem Statement

The industrial classification of the workforce is essential for understanding labor distribution across sectors. Existing workforce classification data may not accurately reflect the current employment scenario. This project updates and analyzes workforce data to support policy making, workforce planning, and industrial development.

## Domain

Resource Management

## Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Natural Language Processing (NLP)
* Matplotlib
* Seaborn

## Project Workflow

### 1. Data Collection

* Load and merge all CSV files into a single DataFrame.
* Verify data consistency and structure.

### 2. Data Cleaning

* Handle missing values.
* Remove duplicate records.
* Standardize column names and data formats.

### 3. Exploratory Data Analysis (EDA)

* Analyze workforce distribution by industry.
* Analyze gender-wise workforce participation.
* Identify major industrial sectors.
* Generate statistical summaries and visualizations.

### 4. Feature Engineering

* Create relevant features for analysis.
* Categorize industries into broader business groups.

### 5. Natural Language Processing (NLP)

* Process industrial descriptions.
* Group industries into categories such as:

  * Agriculture
  * Manufacturing
  * Retail
  * Poultry
  * Construction
  * Chemical Industries
  * Textile Industries
  * Other Services

### 6. Visualization

* Create interactive Plotly charts.
* Generate industry-wise workforce analysis.
* Generate gender-wise workforce analysis.
* Visualize geographical distribution of workers.

### 7. Streamlit Dashboard

The dashboard provides:

* Industry-wise worker distribution
* Gender-wise workforce analysis
* Main vs Marginal worker comparison
* Interactive charts and filters
* Business insights and workforce trends

## Project Structure

Industrial-HR-Geo-Visualization/

├── data/

│ └── dataset.csv

├── app.py

├── data_cleaning.py

├── eda.py

├── nlp_grouping.py

├── requirements.txt

├── README.md

└── presentation.pptx

## Installation

1. Clone the repository

git clone https://github.com/yourusername/Industrial-HR-Geo-Visualization.git

2. Navigate to the project directory

cd Industrial-HR-Geo-Visualization

3. Install required libraries

pip install -r requirements.txt

## Run the Application

streamlit run app.py

## Key Insights

* Workforce distribution varies significantly across industrial sectors.
* Manufacturing and retail industries employ a large workforce.
* Gender participation differs across industry categories.
* Geographical analysis helps identify workforce concentration regions.

## Results

The project successfully provides:

* Industrial workforce classification analysis
* NLP-based industry grouping
* Interactive dashboards
* Business insights for workforce planning and policy decisions

## Future Enhancements

* Real-time workforce data integration
* Predictive workforce analytics
* Advanced machine learning models
* Enhanced geographical mapping

## Author

Project developed as part of the Industrial Human Resource Geo-Visualization project.


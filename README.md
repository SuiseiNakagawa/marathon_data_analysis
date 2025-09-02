# Race Performance Analysis

## Overview
This repository contains a data analysis project exploring heart rate, pace, and terrain interactions during the San Francisco Marathon I ran in July 2025. The goal is to highlight how physiological effort and external factors (elevation, fatigue, race dynamics) shape performance over time.

## Tech Stack & Workflow
- **Data cleaning & preprocessing:** Python scripts to parse GPX/TCX files and export standardized CSVs.  
- **Data querying & aggregation:** SQLite used to load and query workout data for structured exploration.  
- **Analysis & visualization:** Python (Pandas, Plotly) for data wrangling, visualization, and statistical checks.  
- **Integration:** SQL handled the heavy lifting for aggregation, while Python provided flexible visualization and narrative building.  

## Contents
- `notebooks/analysis.ipynb`: Main analysis notebook with visualizations and commentary.
- `data/`: Directory containing raw (`data_raw/`) and cleaned workout files (`data_clean/`) originally in TCX/GPX processed to CSV files.
- `scripts/`: Directory containing Python script to process raw workout files (GPX/TCX).
- `requirements.txt`: Python dependencies for running the notebook.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SuiseiNakagawa/marathon_data_analysis.git
   cd marathon_data_analysis

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   
 3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    
 4. Launch Jupyter:
    ```bash
    jupyter notebook

## Insights
- **Terrain effects:** Pace is strongly influenced by elevation. Uphill segments consistently slow pace, while downhill sections allow partial recovery.  
- **Fatigue progression:** Over time, the ability to capitalize on downhills diminishes, reflecting fatigue and reduced efficiency.  
- **Heart rate dynamics:** HR trends shift from moderate zones early in the race to higher zones in the latter half.  
- **End-race surge:** Despite fatigue, both HR and pace rise in the final kilometers, showing a clear finishing effort.  
- **Efficiency decline:** Pace at a given HR decreases over time, highlighting the impact of fatigue on running economy.  

## Notes
- Data is from my own race recording pulled from Strava and has been cleaned for reproducibility.  
- This project is designed as a **portfolio piece** to demonstrate SQL, Python, and data visualization skills.  



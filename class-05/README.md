# Sales Dashboard - Class 05

A Streamlit-based sales management application with data persistence and interactive dashboard.

## Features

- **Sales Registration**: Add new sales via sidebar form (date, salesperson, product, quantity, value)
- **Data Persistence**: Sales stored in `sales.csv` (auto-loaded on startup)
- **Sales Table**: View all registered sales in an interactive dataframe
- **Dashboard**: 
  - Total revenue metric
  - Bar chart: Revenue by salesperson (grouped by product)
  - Pie chart: Revenue distribution by product

## Requirements

- Python 3.8+
- `streamlit`
- `pandas`
- `plotly`

Install dependencies:
```bash
pip install streamlit pandas plotly
```

## Running the Application

```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`.

## Data Structure

The `sales.csv` file contains:
| Column | Type | Description |
|--------|------|-------------|
| date | date | Sale date |
| salesperson | string | Salesperson name (Ana, Bruno, Carla) |
| product | string | Product name (Notebook, Celular, Fone) |
| quantity | int | Units sold |
| value | float | Sale value |
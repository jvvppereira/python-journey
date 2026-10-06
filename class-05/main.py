# Project step by step
    # Step 1: Create system screen
    # Step 2: Create registration form
    # Step 3: Save sale to database
    # Step 4: Display database on screen
    # Step 5: Create dashboard with charts

from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# Step 1: Create system screen
st.write("# Sales system")

BASE_DIR = Path(__file__).resolve().parent
table = pd.read_csv(BASE_DIR / "sales.csv")
table["date"] = table["date"].astype(str)

# Step 2: Create registration form
st.sidebar.write("## Register sale")
date = st.sidebar.date_input("Date")
salesperson = st.sidebar.selectbox("Salesperson", ["Ana", "Bruno", "Carla"])
product = st.sidebar.selectbox("Product", ["Notebook", "Celular", "Fone"])
quantity = st.sidebar.number_input("Quantity", step=1)
value = st.sidebar.number_input("Value")
button = st.sidebar.button("Register sale")

# Step 3: Save sale to database
if button:
    new_sale = [date, salesperson, product, quantity, value]
    table.loc[len(table)] = new_sale
    table.to_csv("sales.csv", index=False)
    st.success("Sale registered!")

# Step 4: Display database on screen
st.write("## Registered sales")
display_table = table.copy()
display_table["date"] = display_table["date"].astype(str)
st.dataframe(display_table)

# Step 5: Create dashboard
st.write("## Dashboard")
total_sales = table["value"].sum()
st.metric("Total revenue", f"R${total_sales:,.2f}")

chart_salesperson_value_product = px.bar(table, x="salesperson", y="value", color="product")
st.plotly_chart(chart_salesperson_value_product)

chart_product_value = px.pie(table, names="product", values="value")
st.plotly_chart(chart_product_value)
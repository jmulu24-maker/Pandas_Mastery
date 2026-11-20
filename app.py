import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermarket Sales Analysis", layout="wide")

st.title("Supermarket Sales Analysis")
st.write("An interactive analysis of supermarket transaction data using Python and Pandas.")

# Load dataset
df = pd.read_csv("Cleaned_supermarket.csv")

# Key business metrics
total_sales = df["Total_Sales"].sum()
best_branch = df.groupby("Branch")["Total_Sales"].sum().idxmax()
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

col1, col2, col3 = st.columns(3)

col1.metric("Total Recorded Sales", f"{total_sales:,.0f}")
col2.metric("Top Branch", best_branch)
col3.metric("Top Product", best_product)

# Sales by branch
st.subheader("Sales by Branch")
branch_sales = df.groupby("Branch")["Total_Sales"].sum().sort_values(ascending=False)
st.bar_chart(branch_sales)

# Sales by product
st.subheader("Sales by Product")
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
st.bar_chart(product_sales)

# Payment methods
st.subheader("Sales by Payment Method")
payment_sales = df.groupby("Payment_Method")["Total_Sales"].sum().sort_values(ascending=False)
st.bar_chart(payment_sales)

# Show dataset
st.subheader("Transaction Data")
st.dataframe(df, use_container_width=True)
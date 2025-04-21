import streamlit as st
import pandas as pd
import numpy as np

# Dummy data setup
products = ["Coca Cola Classic", "Coca Cola Zero", "Diet Coke", "Coca Cola Cherry"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
stores = ["Store A", "Store B"]

# Generate dummy sales data
data = {
    (month, store): np.random.randint(100, 1000, size=len(products))
    for month in months for store in stores
}
df = pd.DataFrame(data, index=products)

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    warehouse = st.selectbox("Select Warehouse", ["Warehouse 1", "Warehouse 2"])
    year = st.selectbox("Select Year", ["2023", "2024", "2025"])
    month_filter = st.multiselect("Select Months", months, default=months)
    store_filter = st.multiselect("Select Stores", stores, default=stores)

# Layout: Two vertical halves
col1, col2 = st.columns(2)

# Left side: Dummy sales report
with col1:
    st.subheader("Dummy Sales Report")
    filtered_cols = [(m, s) for (m, s) in df.columns if m in month_filter and s in store_filter]
    st.dataframe(df[filtered_cols])

# Right side: Chatbot (placeholder for now)
with col2:
    st.subheader("Chatbot")
    user_input = st.text_input("Ask something about sales data")
    if user_input:
        st.write(f"Bot: You asked about '{user_input}'")

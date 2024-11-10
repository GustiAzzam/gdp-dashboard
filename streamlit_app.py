import streamlit as st
import pandas as pd
import numpy as np

st.title("Tugas 1 :blue - [Pemrograman Sistem ]")
st.title("Gusti Muhammad Akbar Abdullah Azzam - :blue[22220032]")

# Load data
df_sales = pd.read_csv("Network_dataset_23.csv", encoding="iso-8859-1")

# Clean column name issue
df_sales.rename(columns={'ï»¿ts': 'timestamp'}, inplace=True)

# Check if DataFrame is empty
if df_sales.empty:
    st.error("DataFrame is empty! Please check the CSV file.")
else:
    st.success("DataFrame loaded successfully.")
    st.write("Available columns are:", df_sales.columns.tolist())

    # Display the dataset table
    st.write("### Dataset")
    st.dataframe(df_sales)

    # Ensure the timestamp column is numeric (if it's in Unix format)
    df_sales['timestamp'] = pd.to_numeric(df_sales['timestamp'], errors='coerce')

    # Convert timestamp to a readable date format (assuming it's in Unix time)
    df_sales['ORDERDATE'] = pd.to_datetime(df_sales['timestamp'], unit='s')

    # Convert 'src_bytes' to numeric, coerce errors, and fill NaNs with 0
    df_sales['src_bytes'] = pd.to_numeric(df_sales['src_bytes'], errors='coerce').fillna(0)

    # Filter out rows where 'type' is 'mitm'
    df_sales_filtered = df_sales[df_sales['type'] != 'mitm']

    # Get unique traffic types (substitute for product lines)
    try:
        traffic_types = df_sales_filtered["type"].unique()
    except KeyError:
        st.error("The column 'type' does not exist in the DataFrame.")
        st.write("Available columns are:", df_sales_filtered.columns.tolist())
    else:
        # Create a DataFrame with ORDERDATE as index and traffic types as columns
        df_traffic_sales = df_sales_filtered.pivot_table(values='src_bytes', index='ORDERDATE', columns='type', fill_value=0)

        # Calculate total src_bytes per traffic type
        total_src_bytes_per_type = df_sales_filtered.groupby('type')['src_bytes'].sum()

        # Display the total sums table
        st.write("### Total src_bytes per Traffic Type (Class)")
        st.dataframe(total_src_bytes_per_type)

        # Plot the bar chart for total src_bytes per type
        st.title("Bar Chart with Total Sum")
        st.bar_chart(total_src_bytes_per_type)
        st.markdown("---")

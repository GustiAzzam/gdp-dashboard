import streamlit as st
import pandas as pd

# Load data
file_path = "Network_dataset_23.csv"
data = pd.read_csv(file_path)

# Display data in Streamlit
st.title("Network Intrusion Dataset Viewer")
st.write("### Data Table")
st.dataframe(data)

# Choose columns to display in charts
st.write("### Bar Chart of Source and Destination Bytes")
bar_chart_data = data[['src_bytes', 'dst_bytes']].sum()
st.bar_chart(bar_chart_data)

st.write("### Area Chart of Source Bytes over Time")
# Convert 'ts' to datetime if needed and plot
data['ts'] = pd.to_datetime(data['ts'], unit='s')
area_chart_data = data.set_index('ts')['src_bytes']
st.area_chart(area_chart_data)

import streamlit as st
import pandas as pd

st.title("Step 1: Upload Your Customer Dataset")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the data
    df = pd.read_csv(uploaded_file)
    
    # Store data in 'session_state' so other pages can use it
    st.session_state['data'] = df
    
    st.success("File uploaded successfully!")
    
    # Show data preview
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Dataset Summary")
    st.write(df.describe())
else:
    st.info("Please upload a CSV file to get started.")
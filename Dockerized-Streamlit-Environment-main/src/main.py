import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.title("Dockerized Streamlit App 🚀")
st.sidebar.header("Navigation")

page = st.sidebar.selectbox("Go to:", ["Home", "Data Explorer", "Visualization"])

if page == "Home":
    st.write("Welcome to the Streamlit App inside Docker!")

elif page == "Data Explorer":
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)

elif page == "Visualization":
    data = np.random.randn(100)
    fig, ax = plt.subplots()
    ax.hist(data, bins=20)
    st.pyplot(fig)

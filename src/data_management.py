import streamlit as st
import pandas as pd
import joblib

@st.cache_data
def load_maternal_health_risk_data():
    """
    load cleaned data (with erronous datapoints removed)
    """
    df = pd.read_csv(
            "outputs/datasets/cleaned/maternal-health-risk-dataset-clean.csv"
            )
    return df


def load_pkl(file_path):
    """
    Load pkl files (for pipelines)
    """
    return joblib.load(filename=file_path)
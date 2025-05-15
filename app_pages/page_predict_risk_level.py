import streamlit as st
import pandas as pd

from src.data_management import load_maternal_health_risk_data, load_pkl
from src.machine_learning.predictive_analysis import predict_health_risk


def page_predict_risk_level_body():
    """
    Predict Health Risk Levels Page Body
    Provide ML tool to make predictions on health risk
    Handle user inputs, make predictions and display results
    """
    # load predict health risk level files
    version = 'v1'
    pipeline_feat_eng = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_feat_eng.pkl"  # noqa
        )
    pipeline_model = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_model.pkl"
        )

    st.write("## Predict Health Risk Levels")

    st.success(
        "This page answers business requirement 2:\n"
        "> Provide a machine learning–based tool to predict maternal health "
        "risk levels for individual patients, supporting early intervention.\n"
        ">\n"
        )
    st.write("---")

    st.write(
        "#### Predict a patient's maternal health risk level:"
    )
    st.info("The categories are low-risk, medium-risk and high-risk.")
    st.write("Please fill in the following measurements for the patient:")

    # Get Live Data for Predictions from user input
    # Create input widgets
    X_live = DrawInputWidgets()

    # predict on live data
    if st.button("Predict Health Risk", type="primary"):
        predict_health_risk(
                        X_live,
                        pipeline_feat_eng,
                        pipeline_model
                        )


def DrawInputWidgets():
    """
    Handles the input widgets for the health data
    Code inspiration from Code Institute Churnometer walkthrough project
    """
    # load maternal health risk dataset
    df = load_maternal_health_risk_data()
    # to calculate min and max possible input values
    percentageMin, percentageMax = 0.4, 2.0

    # Create input widgets for 3 most important features
    col1, col2, col3 = st.columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget for numerical variable types
    # and set initial values
    with col1:
        feature = "Age"
        st_widget = st.number_input(
            label=feature,
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=1
        )
    X_live[feature] = st_widget

    with col2:
        feature = "SystolicBP"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median(),
            step=1.0
        )
    X_live[feature] = st_widget

    with col3:
        feature = "BloodSugar"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median(),
            step=0.5
        )
    X_live[feature] = st_widget

    return X_live

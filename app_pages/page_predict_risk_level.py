import streamlit as st
import pandas as pd

from src.data_management import load_maternal_health_risk_data, load_pkl
from src.machine_learning.predictive_analysis import predict_health_risk

def page_predict_risk_level_body():

    # load predict health risk level files
    version = 'v1'
    pipeline_feat_eng = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_feat_eng.pkl"
        )
    pipeline_model = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_model.pkl"
        )
    features = (
        pd.read_csv(
                f"outputs/ml_pipeline/{version}/best_features/X_train.csv"
                ).columns.to_list()
        )


    st.write("### Predict Maternal Health Risk Levels")

    st.info(
        "* The client is interested in determining the maternal health risk "
        "level of a given patient.\n"
        "* This page contains an interface that allows users to predict "
        "a given patients health risk level by entering a number of "
        "medical measurements."
        )
    
    # Get Live Data for Predictions from user input
    # Create input widgets
    X_live = DrawInputWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        health_risk_prediction = predict_health_risk(
                                        X_live,
                                        features,
                                        pipeline_feat_eng,
                                        pipeline_model
                                        )

def DrawInputWidgets():

    # load maternal health risk dataset
    df = load_maternal_health_risk_data()
    # to calculate min and max possible input values
    percentageMin, percentageMax = 0.4, 2.0

    # Create input widgets for 3 most important features
    col1, col2, col3 = st.columns(3)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

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
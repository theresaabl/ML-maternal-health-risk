import streamlit as st
import pandas as pd
from src.data_management import load_maternal_health_risk_data

def page_health_risk_study_body():

    # load data for descriptive data analysis
    df = load_maternal_health_risk_data()
    # Transform risk level values to catergories
    df["RiskLevel"] = df["RiskLevel"].replace({0: "low-risk", 1: "mid-risk", 2: "high-risk"})

    # Create dataframe to show variables and units
    units_list = [
        "years",
        "mm Hg",
        "mm Hg",
        "mmol/l",
        "degrees Celsius",
        "bpm",
        ""
        ]
    df_units = pd.DataFrame(data={
                                "Variable": df.columns.to_list(),
                                "Datatype": df.dtypes.to_list(),
                                "Units": units_list
                                })

    # Four most correlated variables
    # Copied from maternal health risk study A notebook
    vars_corr = ['BloodSugar', 'SystolicBP', 'DiastolicBP', 'Age']


    st.write("### Maternal Health Risk Study")

    st.info(
        "* The client is interested in understanding the relationships "
        "between the patients' medical data and their maternal health risk.\n"
        "* We present the main results from our descriptive analysis on this "
        "page.\n"
        "* We present the variables most correlated to the health risk-level "
        "and their distributions over the health-risk."
        )
    
    st.write("---")

    # Inspect data
    if st.checkbox("Inspect maternal health risk dataset samples"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n"
            "* Here is an interactive table showing the first 10 rows of the "
            "dataset:"
            )

        st.dataframe(df.head(10))

        st.write("This table shows the datatypes and units of the variables:")
        st.write(df_units)

    st.write("---")

    

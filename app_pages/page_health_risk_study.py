import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_maternal_health_risk_data

def page_health_risk_study_body():

    # load data for descriptive data analysis
    df = load_maternal_health_risk_data()
    # load plots
    distributions_by_health_risk_plot = plt.imread(
                            "outputs/plots/distributions_by_risk_level.png"
                            )
    # load html file, code inspiration from
    # https://discuss.streamlit.io/t/include-an-existing-html-file-in-streamlit-app/5655/3
    html_file = open("outputs/plots/parallel_plot.html", 'r', encoding='utf-8')
    parallel_plot_src = html_file.read() 

    # Transform risk level values to catergories
    df["RiskLevel"] = df["RiskLevel"].replace({
                                        0: "low-risk",
                                        1: "mid-risk",
                                        2: "high-risk"}
                                        )

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
    if st.checkbox("Inspect Maternal Health Risk Dataset Samples"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n"
            "* Here is an interactive table showing the first 15 rows of the "
            "dataset:"
            )

        st.dataframe(df.head(15))

        st.write("This table shows the datatypes and units of the variables:")
        st.write(df_units)

    st.write("---")


    # Correlation Study
    if st.checkbox("View Correlation Study Results"):
        # Summary
        st.write(
            "We conducted a correlation study of all the variables to find "
            "which variables are most correlated to a patient's health-risk "
            "levels."
        )
        st.success(
            "The most correlated variables to the health-risk level are:\n"
            f"\n**{vars_corr}**"
            )

        # Text based on the "03-MaternalHealthRiskStudyB" notebook
        # Section: "Conclusions and Next Steps"
        st.info(
            "From the correlation study we conclude that:\n"
            "* Patients with high risk tend to have high blood sugar levels\n"
            "* Patients with high risk tend to have high systolic blood pressure levels\n"
            "* Patients with high risk tend to have high diastolic blood pressure levels\n"
            "* Patients with high risk tend to be of a higher age\n"
        )

    st.write("---")

    if st.checkbox("Variable Distributions by Health Risk Level"):
        st.image(distributions_by_health_risk_plot)

        st.write(
            "* From the figure we can see that at higher values of the "
            "variables, the share of high-risk level generally increases.\n" \
            "* This agrees with the results from the correlation study above."
        )
    
    st.write("---")

    if st.checkbox("View Parallel Plot"):
        st.write(
            "This interactive image visualizes the relationships of the "
            "variables with the health risk level."
            )

        components.html(parallel_plot_src, width=1200, height = 400)
    
    st.write("---")


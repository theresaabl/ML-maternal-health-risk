import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_maternal_health_risk_data
from src.machine_learning.create_plots import create_parallel_plot


def page_health_risk_study_body():
    """
    Health Risk Study Page Body
    Displays predictive analysis results
    """
    # load data for descriptive data analysis
    df0 = load_maternal_health_risk_data()
    # load plots
    distributions_by_health_risk_plot = plt.imread(
                            "outputs/plots/distributions_by_risk_level.png"
                            )
    heatmap_corr = plt.imread(
                            "outputs/plots/correlation_spearman_heatmap.png"
                            )
    heatmap_pps = plt.imread(
                        "outputs/plots/pps_heatmap.png"
                        )

    # Keep original dataframe and create copy
    df = df0.copy()
    # Transform risk level values to catergories
    df["RiskLevel"] = df0["RiskLevel"].replace({
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
        "low-, medium-, high-risk"
        ]
    df_units = pd.DataFrame(data={
                                "Variable": df.columns.to_list(),
                                "Datatype": df.dtypes.to_list(),
                                "Units": units_list
                                })
    # Need to convert dtypes to string
    # Idea from https://tinyurl.com/3dcv98ms
    df_units = df_units.astype(str)

    # Four most correlated variables
    # Copied from maternal health risk study A notebook
    vars_corr = ['BloodSugar', 'SystolicBP', 'DiastolicBP', 'Age']

    st.write("## Maternal Health Risk Study")

    st.success(
        "* This page answers business requirement 1:\n"
        "> Improve understanding of maternal health risks during pregnancy:\n"
        ">   * Identify key indicators associated with low, medium, and "
        "high risk.\n"
        ">\n"
    )
    st.info(
        "* The client is interested in understanding the relationships "
        "between the patients' medical data and their maternal health risk.\n"
        "* We present the dataset and the main results of our descriptive "
        "analysis on this page:\n"
        "  * The variables most correlated to the health risk level\n"
        "  * Their distributions by health risk level\n"
        "  * An interactive figure to visualise the relationships between "
        "the variables and the target"
        )

    st.write("---")

    # Inspect data
    if st.checkbox("#### Inspect Maternal Health Risk Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} "
            "columns.\n"
            "* Here is an interactive table showing the first 15 rows of "
            "the dataset:"
            )

        st.dataframe(df.head(15))

        st.write(
                "* This table shows the datatypes and units of the variables:"
                )
        st.write(df_units)

        st.write("---")

    # Correlation Study
    if st.checkbox("#### Correlation Study Results"):
        # Summary
        st.write(
            "We conducted a correlation study of all the variables to find "
            "which variables are most correlated to a patient's health-risk "
            "levels."
        )
        st.success(
            "The most correlated variables to the health risk level are:  \n"
            "  \n"
            f"| {vars_corr[0]} | {vars_corr[1]} | {vars_corr[2]} "
            f"| {vars_corr[3]} |\n"
            "| --- | --- | --- | --- |"
            )

        # Text based on the "03-MaternalHealthRiskStudyB" notebook
        # Section: "Conclusions and Next Steps"
        st.info(
            "From the correlation study we conclude that:\n"
            "* Patients with high risk tend to have high blood sugar levels\n"
            "* Patients with high risk tend to have high systolic blood "
            "pressure levels\n"
            "* Patients with high risk tend to have high diastolic blood "
            "pressure levels\n"
            "* Patients with high risk tend to be of a higher age\n"
        )
        st.write(
            "Note that the two blood pressure types are strongly "
            "correlated between themselves, as one would expect "
            "(see heatmaps below).  \n"
            "Thus, the DiastolicBP variable will be dropped in model training "
            "and is not required to make predictions for maternal health risk."
            )

        st.write("---")

    # Correlation and PPS Heatmaps
    if st.checkbox("#### Correlation and PPS Heatmaps"):
        st.write(
            "* Below are the Spearman correlation and the predictive power "
            "score (PPS) heatmaps to visualize the correlations and PPS "
            "between the variables and the target, as well as between the "
            "variables themselves.\n"
            "* To get the most correlated variables\n"
            "  * we display correlation levels above 0.4 which corresponds "
            "to moderate correlation.\n"
            "  * we display PPS levels above 0.15 to show which variables "
            "have some predictive power over other variables.\n"
        )

        st.image(heatmap_corr)

        st.write("---")

        st.image(heatmap_pps)

        st.write(
            "* The plots illustrate the results that were explained in the "
            "**Correlation Study Results** section above with the caveat "
            "that both, age and diastolic BP, have correlation levels "
            "below 0.4 with the target. Nevertheless, they are still within "
            "the four most correlated variables."
        )

        st.write("---")

    if st.checkbox("Variable Distributions by Health Risk Level"):
        st.write(
            "* The plots below illustrate the distributions of the strongest "
            "correlated variables by the health risk level."
        )

        st.image(distributions_by_health_risk_plot)

        st.write(
            "* From the figure we can see that as the variable values "
            "increase, so does the share of high-risk level.\n"
            "* This agrees with the results from the correlation study "
            "above.\n"
            "* It is interesting to note that from the age distribution plot "
            "we can see that the risk also seems to be higher for the age "
            "range below 20, however the older age ranges are dominant in the "
            "high-risk distribution."
        )

        st.write("---")

    if st.checkbox("Parallel Plot to Visualize Variable Relationships"):
        st.write(
            "This expandable interactive image visualizes the relationships "
            "of the variables with the health risk level."
            )

        vars_corr.append("RiskLevel")
        df_select = df0.filter(vars_corr)

        fig_parallel = create_parallel_plot(df_select)

        st.plotly_chart(fig_parallel)

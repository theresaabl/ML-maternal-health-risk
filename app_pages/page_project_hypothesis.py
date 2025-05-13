import streamlit as st

def page_project_hypothesis_body():
    """
    Project Hyptheses and Validation Page Body
    Display hypotheses and validation
    """
    st.write("## Project Hypotheses and Validation")

    st.info(
        "### Hypotheses\n"
        "1. We expect that high-risk patients tend to have high blood sugar "
        "levels.\n"
        "2. We expect that high-risk patients tend to have high systolic blood "
        "pressure levels.\n"
        "3. We expect that high-risk patients tend to have high diastolic "
        "blood pressure levels.\n"
        "4. We expect that high-risk patients tend to be of a higher age."
        )
    
    st.success(
        "### Validation\n"
        " * The correlation study on the **Maternal Health Risk Study** page "
        "supports all four hypotheses.\n"
        "* From the correlation levels of the variables with the health risk "
        "level, we conclude that:\n"
        "\n"
        "1. High-risk patients tend to have high blood sugar "
        "levels.\n"
        "2. High-risk patients tend to have high systolic and diastolic blood "
        "pressure levels, where the two are correlated between themselves.\n"
        "3. High-risk patients tend to be of a higher age."
        )

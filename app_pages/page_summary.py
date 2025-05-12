import streamlit as st

def page_summary_body():

    st.write("## Project Summary")

    # Based on README file - Introduction section
    st.info(
        "Improving maternal health during pregnancy and childbirth is part "
        "of the UN sustainable developement goals (SDGs):" 
        )
    st.error(
        ">'A woman dies every two minutes from preventable causes related to "
        "pregnancy and childbirth.'\n"
        ">\n"
        " --  [UN SDGs](https://sdgs.un.org/goals/goal3)"
    )
    st.write(
        "Maternal health is a public health aspect of global interest.  \n"
        "There are many different complications that can occur during "
        "pregnancy and childbirth which can pose a risk on the mother as well "
        "as the baby.  \n"
        "It is of great importance to reduce these complications and with this "
        "project we aim to make a small contribution to towards this goal.  \n"
        "We will study patients health data and explore which health factors "
        "play the leading roles in determining whether a patient falls into "
        "the low-, medium- or high-risk categories.  \n"
        "We will also provide a machine-learning based tool to predict a "
        "patient's risk level from basic medical measurements, which are "
        "are usually taken during routine doctor's visits."
    )
    
    st.write("---")

    # Based on README file - "Dataset Content" section
    st.write("### Dataset Summary")
    st.write(
        "We use the Maternal Health Risk dataset from "
        "[UCI](https://archive.ics.uci.edu/dataset/863/maternal+health+risk) "
        "for our analysis:\n" 
        "> Ahmed, M. (2020). Maternal Health Risk [Dataset]. "
        "UCI Machine Learning Repository. https://doi.org/10.24432/C5DP5D.\n"
        ">\n"
        "This dataset contains medical data collected from "
        "different hospitals, community clinics and maternal health cares "
        "centers from the rural areas of Bangladesh (see dataset metadata).  \n"
        "To inspect the dataset, pleaes see the **Maternal Health Risk** "
        "**Study** page."
        )

    st.write("---")

    # Link to README file, for full project documentation
    st.write(
        "### Full Documentation\n"
        "For an extensive documentation, please see the "
        "[Project README file](https://github.com/theresaabl/ML-maternal-health-risk)."  # noqa
        )

    st.write("---")

    # Based on README file - "Business Requirements" section
    st.write(
        "### Business Requirements"
        )
    st.success(
        "1. Improve understanding of maternal health risks during pregnancy:\n"
        "   * Identify key indicators associated with low, medium, and "
        "high risk.\n"
        "2. Provide a machine learning–based tool to predict maternal health "
        "risk levels for individual patients, supporting early intervention."
    )

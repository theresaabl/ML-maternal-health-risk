import streamlit as st

def page_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info("This section contains info about the project dataset and jargon")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]().")


    # copied from README file - "Business Requirements" section
    st.success("This section contains info about the business requirements")

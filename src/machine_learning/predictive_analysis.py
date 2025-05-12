import streamlit as st
import pandas as pd

def predict_health_risk(X_live, pipeline_feat_eng, pipeline_model):

    # apply feat engine pipeline to live data
    X_live_feat_eng = pipeline_feat_eng.transform(X_live)

    # predict
    prediction = pipeline_model.predict(X_live_feat_eng)
    # Create a prediction probability dataframe to display
    prediction_prob = pd.DataFrame(
                        pipeline_model.predict_proba(X_live_feat_eng),
                        index=(["Probability"])
                        )
    prediction_prob.rename(
            columns={0: "Low-risk", 1: "Medium-risk", 2: "High-risk"},
            inplace=True
            )
    prediction_prob = prediction_prob.apply(
                            lambda x: (x*100).round(1).astype(str).add("%"),
                            axis=1
                            )

    # Create a logic to display the results
    if prediction == 0:
        result = "low"
    elif prediction == 1:
        result = "medium"
    else:
        result = "high"

    statement = (
        f"### Prediction:\n > #### {result.capitalize()} health risk  \n"
        )
    
    st.write("---")
    # Display in different style depending on category
    if prediction == 0:
        st.success(statement)
    elif prediction == 1:
        st.warning(statement)
    else:
        st.error(statement)

    st.write(
        "The probabilities for the patient to belong to each of the "
        "categories are:"
        )
    st.dataframe(prediction_prob)
    return prediction
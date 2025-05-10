import streamlit as st


def predict_health_risk(X_live, features, pipeline_feat_eng, pipeline_model):

    # apply feat engine pipeline to live data
    X_live_feat_eng = pipeline_feat_eng.transform(X_live)

    # predict
    prediction = pipeline_model.predict(X_live_feat_eng)
    prediction_proba = pipeline_model.predict_proba(X_live_feat_eng)
    # st.write(prediction_proba)

    # Create a logic to display the results
    prob = prediction_proba[0, prediction][0]*100

    if prediction == 0:
        result = "low"
    elif prediction == 1:
        result = "medium"
    else:
        result = "high"

    statement = (
        f'### There is {prob.round(1)}% probability that this patient '
        f'falls into the **{result} health risk** catergory.')

    st.write(statement)

    return prediction
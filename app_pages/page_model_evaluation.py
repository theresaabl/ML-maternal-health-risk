import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl
from src.machine_learning.evaluate_model import performance

def page_model_evaluation_body():

    version = 'v1'
    # load files for model evaluation
    pipeline_feat_eng = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_feat_eng.pkl"
        )
    pipeline_model = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_model.pkl"
        )
    feat_importance_plot = plt.imread(
        f"outputs/ml_pipeline/{version}/best_features/feature_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/y_test.csv").values
    

    st.write("### ML: Health Risk Prediction")

    # display pipeline training summary conclusions
    st.info(
        "* The pipeline was tuned aiming at a minimum 80% recall for the "
        "high-risk class, since in this medical project it is essential "
        "to not miss many high-risk patients.\n"
        "* The pipeline performance on train and test set is .. and .., respectively."
    )
    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible feature engineering.")
    st.write(pipeline_feat_eng)

    st.write("* The second is for feature scaling and modelling.")
    st.write(pipeline_model)

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(feat_importance_plot)
    


# def page_predict_churn_body():

        # We don't need to apply dc_fe pipeline, since X_train and X_test
    # were already transformed in the jupyter notebook (Predict Customer Churn.ipynb)

    # # evaluate performance on train and test set
    # st.write("---")
    # st.write("### Pipeline Performance")
    # clf_performance(X_train=X_train, y_train=y_train,
    #                 X_test=X_test, y_test=y_test,
    #                 pipeline=churn_pipe_model,
    #                 label_map=["No Churn", "Yes Churn"])

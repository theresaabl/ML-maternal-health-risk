import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl
from src.machine_learning.evaluate_model import performance


def page_model_evaluation_body():
    """
    Model and Evaluation Page Body
    Displays pipeline details and performance metrics
    """
    # load files for model evaluation
    version = 'v1'
    # pipelines
    pipeline_feat_eng = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_feat_eng.pkl"  # noqa
        )
    pipeline_model = load_pkl(
        f"outputs/ml_pipeline/{version}/best_features/clf_pipeline_model.pkl"
        )
    # train and test sets
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/{version}/best_features/y_test.csv").values
    # plots
    feat_importance_plot = plt.imread(
        f"outputs/plots/feature_importance.png")
    confusion_matrix_plot = plt.imread(
        f"outputs/plots/confusion_matrix.png")

    st.write("## ML: Model and Evaluation")

    # display pipeline training summary
    st.write("### Summary")
    st.info(
        "* The pipeline was tuned aiming at a minimum 80% recall for the "
        "high-risk class, while keeping low-risk precision above 80% as "
        "well.\n"
        "* These metrics are selected, since when predicting maternal health "
        " risk it is essential:\n"
        "  * Not to miss high-risk patients.\n"
        "  * Not to falsely class someone as low-risk who might need further "
        "medical attention."
    )
    st.success(
            "* The model used for the **Predict Health Risk Levels** "
            "predictor meets these criteria and well exceeds them for most "
            "metrics.\n"
            "* The pipeline performance on train and test set is:\n"
            "  * 94% and 87% for high-risk recall, respectively\n"
            "  * 89% and 81% for low-risk precision, respectively\n"
            )
    st.write("---")

    # Show Train and Test Set Frequencies
    if st.checkbox("### Train and Test Set"):
        st.info(
            "The dataset was split into train and test sets with the "
            "following frequencies:"
            )

        st.markdown(
            "| | Train Set Features | Train Set Target | Test Set Features | Test Set Target |\n"  # noqa
            "| --- | --- | --- | --- | --- |\n"
            f"| Rows | {X_train.shape[0]} | {y_train.shape[0]} | {X_test.shape[0]} | {y_test.shape[0]} |\n"  # noqa
            f"| Columns | {X_train.shape[1]} | {y_train.shape[1]} | {X_test.shape[1]} | {y_test.shape[1]} |"  # noqa
            )
        st.write("---")

    # Show pipelines
    if st.checkbox("### ML Pipelines"):
        st.info("There are 2 ML Pipelines arranged in series.")

        st.write(" * The first is responsible for feature engineering:")
        st.write(pipeline_feat_eng)

        st.write(
            "* The second is responsible for feature scaling and modelling:"
            )
        st.write(pipeline_model)

        st.success(
                "The optimised model is a Random Forest Classifier with "
                "max depth 10."
                )
        st.write("---")

    # Show feature importance plot
    if st.checkbox("### Important Features"):
        # get features list:
        feat_list = X_train.columns.to_list()
        st.info(
            "The model was trained on the following features (in order of "
            "importance):\n"
            f"| {feat_list[0]} | {feat_list[1]} | {feat_list[2]} |\n"
            "| --- | --- | --- |"
            )
        st.write(
            "The relative importance of the model features is illustrated "
            "in this plot:"
            )
        st.image(feat_importance_plot)
        st.write("---")

    # Evaluate performance on train and test set
    if st.checkbox("### Pipeline Performance"):
        st.info("A report of performance metrics for the train and test sets:")
        # Don't need to apply feature engineering pipeline since the train
        # and test set was already transformed in the jupyter notebooks
        performance(
            X_train=X_train,
            y_train=y_train,
            X_test=X_test,
            y_test=y_test,
            pipeline=pipeline_model,
            label_map=["low-risk", "mid-risk", "high-risk"]
            )
        st.write("---")

    # Show confusion matrix plot
    if st.checkbox("#### Visualization"):
        st.write(
            "The confusion matrices for the train and test set are "
            "visualised in the following plot. The predicted values for "
            "the risk level are on the x-axis and the true values are on "
            "the y-axis."
        )
        st.image(confusion_matrix_plot)

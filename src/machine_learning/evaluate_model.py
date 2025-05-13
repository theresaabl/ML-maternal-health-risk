import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix


# functions copied from modelling and evaluation notebook B
def get_metrics(X, y, pipeline, label_map):
    """
    Generates a classification report and a confusion matrix
    Returns the two as dataframes
    """
    prediction = pipeline.predict(X)

    report = pd.DataFrame(classification_report(
                                            y,
                                            prediction,
                                            target_names=label_map,
                                            output_dict=True
                                            )).T
    # drop accuracy from table and store in separate var
    acc = np.round(report.loc[["accuracy"]].iloc[0, 0], 2)
    report.drop(index="accuracy", inplace=True)

    cm = pd.DataFrame(
                confusion_matrix(y_true=prediction, y_pred=y),
                columns=["Actual " + sub for sub in label_map],
                index=["Prediction " + sub for sub in label_map]
                )

    return report, acc, cm


def performance(X_train, y_train, X_test, y_test, pipeline, label_map):
    """
    Displays classification reports and confusion matrices for train and
    test sets as dataframes
    """
    st.write("### Train Set")
    report_train, acc_train, cm_train = get_metrics(
                                            X_train,
                                            y_train,
                                            pipeline,
                                            label_map
                                            )
    st.write("#### Classification Report")
    st.dataframe(report_train)
    st.write(f"Accuracy: {acc_train}")
    st.write("#### Confusion Matrix")
    st.dataframe(cm_train)

    st.write("### Test Set")
    report_test, acc_test, cm_test = get_metrics(
                                        X_test,
                                        y_test,
                                        pipeline,
                                        label_map
                                        )
    st.write("#### Classification Report")
    st.dataframe(report_test)
    st.write(f"Accuracy: {acc_test}")
    st.write("#### Confusion Matrix")
    st.dataframe(cm_test)

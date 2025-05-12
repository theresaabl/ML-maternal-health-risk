import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import plotly.express as px


# From 03-MaternalHealthRiskStudyB notebook parallel plot section
def create_parallel_plot(df):
    """
    Creates a parallel categories plot of the four most correlated features
    with the target variable
    Discretizes the numerical values into categories
    Returns plotly figure
    """
    blood_sugar_map = [-np.inf, 6.8, 7, 7.5, 8, np.inf]
    systolic_bp_map = [-np.inf, 90, 110, 120, np.inf]
    diastolic_bp_map = [-np.inf, 60, 70, 80, 90, np.inf]
    age_map = [-np.inf, 18, 24, 30, 40, np.inf]

    # Use ArbritaryDiscretiser from feature_engine and specify
    # the category ranges
    disc = ArbitraryDiscretiser(binning_dict={
                                    "BloodSugar": blood_sugar_map,
                                    "SystolicBP": systolic_bp_map,
                                    "DiastolicBP": diastolic_bp_map,
                                    "Age": age_map}
                                    )

    # Store data in a new dataframe
    df_parallel = disc.fit_transform(df)

    # Code inspiration from Code Institute churnometer walkthrough project,
    # adapted from only one to several variables
    vars_cat = ["BloodSugar", "SystolicBP", "DiastolicBP", "Age"]
    n_classes_list = [
        len(blood_sugar_map) - 1, 
        len(systolic_bp_map) - 1,
        len(diastolic_bp_map) - 1,
        len(age_map) - 1
        ]

    classes_ranges_list = []
    labels_map_list = []
    for ind, var in enumerate(vars_cat):
        # store the ranges of the above defined categories in a list
        classes_ranges_list.append(disc.binner_dict_[var][1:-1])

        labels_map_list.append({})
        for n in range(0, n_classes_list[ind]):
            if n == 0:
                labels_map_list[ind][n] = f"<{classes_ranges_list[ind][0]}"
            elif n == n_classes_list[ind]-1:
                labels_map_list[ind][n] = f">{classes_ranges_list[ind][-1]}"
            else:
                labels_map_list[ind][n] = f"{classes_ranges_list[ind][n-1]} to {classes_ranges_list[ind][n]}"  # noqa
    
    for ind, var in enumerate(vars_cat):
        df_parallel[var] = df_parallel[var].replace(labels_map_list[ind])

    # Relabel Risklevel with words for better interpretability of plot
    # Save in new column since we need numbers as well for coloring the plot
    df_parallel["RiskLabel"] = df_parallel["RiskLevel"].replace({
                                                            0: "0 - low",
                                                            1: "1 -mid",
                                                            2: "2 - high"
                                                            })
    dimensions_parallel = df_parallel.drop(
                                        columns=["RiskLevel"]
                                        ).columns.to_list()

    fig_parallel = px.parallel_categories(
                            df_parallel,
                            dimensions=dimensions_parallel,
                            labels = {"RiskLabel": "RiskLevel"},
                            color="RiskLevel",
                            title="Variables and RiskLevel Parallel Plot",
                            # template='plotly_dark',
                            color_continuous_scale=px.colors.sequential.Plasma
                            )
    # Code to change label font size in plotly:
    # https://stackoverflow.com/a/72034697
    fig_parallel.update_traces(
                    tickfont=dict(
                                size=12,
                                color="black"
                                ),
                    labelfont=dict(
                                size=15,
                                color="black"
                                ),
                    )

    return fig_parallel
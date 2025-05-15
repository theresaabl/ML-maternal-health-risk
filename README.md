# [Maternal Health Risk Predictor](https://maternal-health-risk-predictor-f82f6452b3b6.herokuapp.com/)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/theresaabl/ML-maternal-health-risk)](https://www.github.com/theresaabl/ML-maternal-health-risk/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/theresaabl/ML-maternal-health-risk)](https://www.github.com/theresaabl/ML-maternal-health-risk/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/theresaabl/ML-maternal-health-risk)](https://www.github.com/theresaabl/ML-maternal-health-risk)

Live Site - [Maternal Health Risk Predictor](https://maternal-health-risk-predictor-f82f6452b3b6.herokuapp.com/)

![screenshot](documentation/mock-up.png)

source: [Maternal Health Risk Predictor - amiresponsive](https://ui.dev/amiresponsive?url=https://maternal-health-risk-predictor-f82f6452b3b6.herokuapp.com/)

## Summary

Improving maternal health during pregnancy and childbirth is part of the UN sustainable developement goals (SDGs):

>'A woman dies every two minutes from preventable causes related to pregnancy and childbirth.'
>
> \-  [UN SDGs](https://sdgs.un.org/goals/goal3)

Maternal health is a public health aspect of global interest.
There are many different complications that can occur during pregnancy and childbirth which can pose a risk on the mother as well as the baby.
It is of great importance to reduce these complications and with this project we aim to make a small contribution towards this goal.

* We will study patients' health data and explore which health factors play the leading roles in determining whether a patient falls into the low-, medium- or high-risk categories.
* We will also provide a machine-learning based tool to predict a patient's risk level from basic medical measurements, which are usually taken during routine prenatal care checkups.
* This will be presented in a dashboard.

## Dataset Content

We use the Maternal Health Risk dataset from [UCI](https://archive.ics.uci.edu/dataset/863/maternal+health+risk) for our analysis:

> Ahmed, M. (2020). Maternal Health Risk [Dataset].
> UCI Machine Learning Repository [https://doi.org/10.24432/C5DP5D](https://doi.org/10.24432/C5DP5D).
>

* This dataset contains medical data collected from different hospitals, community clinics and maternal health care centers from the rural areas of Bangladesh (see dataset metadata).
* The dataset has 1014 rows and 7 columns (note that the dataset presented on the streamlit dashboard has 1011 rows, where 3 erronous datapoints were already removed).
* Each Row contains health data about one patient, the variables are:

| Variable | Information | Type | Units |
| --- | --- | --- | --- |
|Age | Patient's age | numerical | years |
| SystolicBP | Patient's systolic blood pressure | numerical | mm Hg |
| DiastolicBP | Patient's diastolic blood pressure | numerical | mm Hg |
| BloodSugar | Patient's blood sugar level | numerical | mmol/l |
| BodyTemp | Patient's body temperatur | numerical | degrees Celcius |
| HeartRate | Patient's heart rate | numerical | bpm |
| RiskLevel | Patient's maternal health risk level | categorical | ['low-risk', 'mid-risk', 'high-risk'] |

* Where RiskLevel is the target that we want to predict
* There are three classes: low-risk, mid-risk and high-risk
  * Note: mid-risk and medium-risk are sometimes used interchangeably

## Business Requirements

A national health organisation has contacted us to study maternal health risk through a descriptive and predictive data analysis. The client provided the dataset.

There are **two business requirements** agreed on with the client:

* BR 1. Improve understanding of maternal health risks during pregnancy:
  * Identify key indicators associated with low, medium, and high risk.
* BR 2. Provide a machine learning–based tool to predict maternal health risk levels for individual patients, supporting early intervention.

Further:

* The clients goal is to use our results to develop new policies to improve pregnancy care and to support early interventions to mitigate health risks.
* They plan to provide our predictive analytics tool to health care professionals and thus, facilitate maternal health risk assessement during prenatal care.
* This could help risk assessement, e.g. in cases where:
  * The health professionals do not have a lot of experience yet
  * There is time pressure
  * No experts are available and GPs need to do the assessement

## Hypotheses and Validation

We state the following three hypotheses:

  1. We expect that high-risk patients tend to have high blood sugar levels.
  2. We expect that high-risk patients tend to have high systolic blood pressure levels.
  3. We expect that high-risk patients tend to have high diastolic blood pressure levels.
  4. We expect that high-risk patients tend to be of a higher age.

We come to these expectations by looking at literature about pregnancy health risk factors, e.g. in the following articles:

* [National Library of Medicine (US)](https://www.ncbi.nlm.nih.gov/books/NBK555485/)
* [Mayo Clinic](https://www.mayoclinic.org/healthy-lifestyle/pregnancy-week-by-week/in-depth/high-risk-pregnancy/art-20047012)
* [MSD Manuals](https://www.msdmanuals.com/home/women-s-health-issues/complications-of-pregnancy/risk-factors-for-pregnancy-complications#Problems-in-a-Previous-Pregnancy_v809815)

We find that hypertension (high blood pressure), diabetes (high blood sugar) and maternal age are mentioned as some of the leading risk factors. We look to validate these hypotheses through correlation studies and find out in more detail which of these factors play they largest roles.

### Validation

Indeed in the correlation study we find that blood sugar, blood pressure (systolic and diastolic) and age are the most correlated variables to the health risk level.

Our correlation study supports all three hypotheses:

* From the correlation levels of the variables with the health risk level, we conclude that:

1. High-risk patients tend to have high blood sugar levels.
2. High-risk patients tend to have high systolic and diastolic blood pressure levels, where the two are correlated between themselves.
3. High-risk patients tend to be of a higher age.

This is illustrated in the following Spearman correlation heatmap and predictive power score (pps) heatmap:

![Spearman Correlation Heatmap](documentation/plots/correlation_spearman_heatmap.png "Spearman Correlation Heatmap")![PPS Heatmap](documentation/plots/pps_heatmap.png "PPS Heatmap")

## Mapping Business Requirements to Data Visualizations and ML Tasks

Business requirements:

* BR 1. Improve understanding of maternal health risks during pregnancy:
  * Identify key indicators associated with low, medium, and high risk.
* BR 2. Provide a machine learning–based tool to predict maternal health risk levels for individual patients, supporting early intervention.

Data Visualizations and ML Tasks:

* BR 1:
  * Perform a correlation study of the features with the target variable to analyse which medical measurements are most correlated to the health risk level.
  * Use heatmaps to display the correlation levels and predictive power.
  * Display the distributions of the variables per health risk level to visualize the relationship.
  * Visualize the relationships in an interactive parallel plot that shows the relationships between all variables and the target.
  
* BR 2:
  * We will predict the health risk level of a given patient &rarr; multiclass Classification.
  * Perform data cleaning and feature engineering on the dataset to best prepare it for the predictive analysis.
  * Put the steps into a data cleaning and feature engineering pipeline.
  * The machine-learning tool will be a Classification - perform and extensive algorithm and hyperparameter search to find the best model for predictions on live data.
  * Balance performance and generalizability to find a model that has good recall and precision and also has a small train-test-gap (performance on test set is similar enough to train set).
  * Visualize the most important features.
  * Visualize the model performance with the help of confusion matrices.
  * Provide a live tool for predictions with user input data.

## ML Business Case

In the [Business Requirements Section](#business-requirements) above, we described the business requirements agreed on with the client who in this case is a national health organization.

### Industries

In general, industries that could be interested in a project that aims at

* Better understanding of maternal health risk during pregnancy with the goal to define strategies and policies to decrease the health risk.
* Understanding of the main indicators of low/medium/high risk
* Predicting risk for individuals or for populations

are:

* Health and welfare organizations:
  * World Health Organization (WHO)
  * UNICEF, UNFPA, and other global maternal health initiatives
  * Local health authorities and public health departments
  * NGOs focused on maternal and child health
* Public Policy and Government
  * Ministries or Departments of Health
  * Government policymakers
  * Public health advisors
* Medical sector
  * Hospitals
  * OB/GYN practices and prenatal clinics
* Research
  * University researchers
  * Non-academic researchers

### ML Model

* The business objective requiring an ML solution is to classify patient by their health risk, thus we are looking for a Classifier model to fit our data and make predictions.
* The model inputs should be health data that can be collected during routine prenatal care visits
* The model outputs should be a prediction of the health-risk (low, medium or high) and the probabilities that the patients belongs to each of the classes (for better interpretability for in-between cases)
* Data is available to train the model, see details about the dataset in the [Dataset Content Section](#dataset-content)

### Dashboard

The customer is requesting a dashboard which provides

* The ML tool to predict health risk for patients
* The results of the correlation study to better understand the relationship between the health measurements and the risk
* Information about the model and pipelines
* Model performance reports

### Project Success

The project will be successful if we provide a dashboard with all the required business outputs including

* descriptive analysis answering business requirement 1
* predictive analytics tool with required performance metrics answering business requirement 2

### Epics and User Stories

See [User Stories Section](#user-stories) below.

### Ethical or Privacy Concerns

* The health measurements taken for the data collection are standard measurements with no adverse effects on the patients
* It will be important that when predictions are made on real-world patients, the health care provider as well as the patient are aware of the probabilities of the predictions.
* The prediction results should always be combined with the experience and assessement of a health professional
* There are no privacy concerns since the data is anonymized

### Benefits for the Client

* Analyses the main factors that contribute to pregnancy complications to inform health practitioners or policy makers.
* Makes it possible to quickly predict the maternal health risk based on basic health data that is taken during routine visits anyways.
* Makes the prediction more systematic and with less room for individual error.
* This allows less experienced staff to make predictions based on data from many women that they could not have gathered on their own.
* Makes predictions quickly when under time pressure.

### Model Evaluation and Performance Requirements

* Since this is a healthcare related project and we aim to identify high-risk patients, the goal is to optimize the ML classifier for recall of the high-risk class.
* Ideally, a recall of 80% or higher for high-risk patients is the goal
* While optimizing for high-risk recall, low-risk precision should also stay above 80% since it is essential that patients are not incorrectly told to have low rikk.
* However, the dataset at hand is relatively small and also moderately imbalanced, so in this scenario a high-risk recall or low-risk precision above 70% would also be a reasonably good performance.
* **Summary:** With hyperparameter optimization we aim to reach a high-risk recall and low-risk precision of above 80% with a focus on the high-risk recall.

## User Stories

We split our project into epics and user stories.

Epics:

* Information gathering and data collection
* Data visualization, cleaning, and preparation
* Model training, validation, and optimization
* Dashboard planning, designing, and development
* Dashboard deployment and release

### EPIC: Data Collection

* As a **data analyst**

## Dashboard Design

In this section we describe the design of the project dashboard including the pages and sections, the content of each section and a screenshot of the finished product.

| Page | Section | Content | Screenshot |
| --- | --- | --- | --- |
| All Pages | Menu | Radio button menu to navigate the app | ![screenshot](documentation/dashboard/menu.png) |
| Project Summary Page | Project summary | Summary of the project topic and introduction to project goals | ![screenshot](documentation/dashboard/project_summary.png) |
| Project Summary Page | Dataset summary | Summary of the dataset content and cite dataset source | ![screenshot](documentation/dashboard/dataset_summary.png) |
| Project Summary Page | Link to documentation | Link to the full documentation here | ![screenshot](documentation/dashboard/readme_link.png) |
| Project Summary Page | Business requirements | The business requirements agreed on with the client | ![screenshot](documentation/dashboard/business_requirements.png) |
| Maternal Health Risk Study Page | Maternal Health Risk Study Summary | A summary of this page describing that it answers business requirement 1 | ![screenshot](documentation/dashboard/maternal_health_risk_study_summary.png) |
| Maternal Health Risk Study Page | Checkboxes to display and hide different sections | The seperate sections of this page are collapsed and can be displayed by clicking the respective checkbox. This makes the page interactive to avoid information overload. | ![screenshot](documentation/dashboard/study_checkboxes.png) |
| Maternal Health Risk Study Page | Inspect Maternal Health Risk Dataset | Show a sample of the dataset, state size of dataset and give information about the variables | ![screenshot](documentation/dashboard/inspect_dataset.png) |
| Maternal Health Risk Study Page | Correlation Study Results | Present the results of the correlation study and state which variables are most correlated to the target | ![screenshot](documentation/dashboard/correlation_study_results.png) |
| Maternal Health Risk Study Page | Correlation and PPS Heatmaps | Visualize the correlation study with heatmaps (Spearman correlation and predictive power score (pps)) | ![screenshot](documentation/dashboard/correlation_heatmaps.png) |
| Maternal Health Risk Study Page | Variable Distributions by Health Risk Level | Present a plot of the variable distributions by health risk level to visualize the most correlated variables and their relationships to the health risk level further | ![screenshot](documentation/dashboard/correlation_distributions.png) |
| Maternal Health Risk Study Page | Parallel Plot to Visualize Variable Relationships | An interactive and expandable parallel plot that shows the relationships between the most correlated variables with the health risk level and between themselves | ![screenshot](documentation/dashboard/correlation_parallel_plot.png) |
| Project Hypotheses and Validation Page | Project Hypotheses and Validation | Present the project hypotheses, if they were validated and how they were validated | ![screenshot](documentation/dashboard/hypotheses_validation.png) |
| Predict Health Risk Levels Page | Predict Health Risk Levels Prediction Tool | This page answers business requirement 2 and provides a ML tool to classify patients into low-, medium- and high-risk categories based on user input medical measurements. | ![screenshot](documentation/dashboard/predict_risk_level.png) |
| Predict Health Risk Levels Page | Prediction for Low Risk | Example for a low-risk prediction, which is emphasized with the background color of the prediction result display. Further, a table with probabilities for each of the risk classes is presented for better interpretability of the results, especially for edge cases. | ![screenshot](documentation/dashboard/prediction_low_risk.png) |
| Predict Health Risk Levels Page | Prediction for Medium Risk | Example for a medium-risk prediction. | ![screenshot](documentation/dashboard/prediction_mid_risk.png) |
| Predict Health Risk Levels Page | Prediction for High Risk | Example for a high-risk prediction. | ![screenshot](documentation/dashboard/prediction_high_risk.png) |
| ML: Model and Evaluation | Model and Evaluation Summary | Summary of model performance requirements and actual model performance results | ![screenshot](documentation/dashboard/model_evaluation_summary.png) |
| ML: Model and Evaluation | Checkboxes to display and hide different sections | The seperate sections of this page are collapsed and can be displayed by clicking the respective checkbox. This makes the page interactive to avoid information overload. | ![screenshot](documentation/dashboard/evaluation_checkboxes.png) |
| ML: Model and Evaluation | Train and Test Set | Displays the train and test set frequencies | ![screenshot](documentation/dashboard/train_test_set.png) |
| ML: Model and Evaluation | ML Pipelines | Present the feature engineering and model pipeline, showing the steps and hyperparameters | ![screenshot](documentation/dashboard/ml_pipelines.png) |
| ML: Model and Evaluation | Important Features | Present the most important features and their relative importance | ![screenshot](documentation/dashboard/features.png) |
| ML: Model and Evaluation | Pipeline Performance | Present a more detailed pipeline performance report, including classification reports and confusion matrices for the train and the test set | ![screenshot](documentation/dashboard/performance.png) |
| ML: Model and Evaluation | Visualization | Visualize the train and test set confusion matrices | ![screenshot](documentation/dashboard/confusion_matrix.png) |

## Possible Future Directions

There are many ways in which one could improve or extend this project. Some ideas are:

* Develop an API to embed the maternal health risk prediction tool into websites directly:
  * This could be useful for medical prefessionals, so they could use the predictor on their own websites and platforms
* Collect more data:
  * A larger dataset would help improve the analyses and predictions
  * More details about the measurements would be very helpful in improving the analysis and decision making (e.g. age values, blood sugar measurements)
* It would be very interesting to also study this data with a clustering model to study whether the algorithm finds similar clusters as the health risk labels or if it finds additional structure within the data.
* An even more extensive hyperparameter optimization together with a larger dataset and more feature engineering (when having more information about the health measurement details) could help improve the prediction performance.

## CRISP-DM

CRoss Industry Standard Process for Data Mining

### Business Understanding

See above

### Data Understanding

### Data Preparation

#### Data Cleaning

#### Sample Rebalancing

#### Feature Engineering

### Modeling

#### Model and Hyperparameter Search

#### Important Features

### Evaluation

Notes:
Model without winsorizer:

RandomForestClassifier with max_depth 12:
train set high-risk recall: 88%
test set high-risk recall: 78%
difference: 10 percentage points
RandomForestClassifier with max_depth 8:
train set high-risk recall: 82%
test set high-risk recall: 75%
difference: 7 percentage points

Final model with winsorizer:

* model with only best features:
  * high-risk recall train: 94%
  * high-risk recall test: 87%
  * high-risk recall gap: 7 percentage points
  * low-risk-precision train: 89%
  * low-risk-precision test: 81%
  * low-risk-precision gap: 8 percentage points

### Deployment

see below

## Main Data Analysis and Machine Learning Libraries

| Libraries | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Pandas-grey?logo=pandas&logoColor=150458)](https://pandas.pydata.org/) | Library for data structures and data analysis tools. |
| [![badge](https://img.shields.io/badge/Numpy-grey?logo=numpy&logoColor=013243)](https://numpy.org/) | Library for scientific computing. |
| [![badge](https://img.shields.io/badge/Scipy-grey?logo=scipy&logoColor=8CAAE6)](https://scipy.org/) | Library for fundamental algorithms for scientific computing in Python. |
| [![badge](https://img.shields.io/badge/Ydata-Profiling-grey)](https://docs.profiling.ydata.ai/latest/) | Library for data profiling. |
| [![badge](https://img.shields.io/badge/Matplotlib-grey)](https://matplotlib.org/) | Library for visualizations in Python. |
| [![badge](https://img.shields.io/badge/Seaborn-grey)](https://seaborn.pydata.org/) | Library for statistical data visualizations. |
| [![badge](https://img.shields.io/badge/Plotly-Express-grey?logo=plotly&logoColor=3F4F75)](https://plotly.com/python/plotly-express/) | Library for interactive charts. |
| [![badge](https://img.shields.io/badge/Feature-Engine-grey)](https://feature-engine.trainindata.com/en/latest/) |  Library with multiple transformers to engineer and select features for machine learning models. |
| [![badge](https://img.shields.io/badge/ppscore-grey)](https://pypi.org/project/ppscore/) |  Library with python implementation of the Predictive Power Score. |
| [![badge](https://img.shields.io/badge/Scikit-Learn-grey?logo=plotly&logoColor=F7931E)](https://scikit-learn.org/stable/) | Library for predictive data analysis. |
| [![badge](https://img.shields.io/badge/XGBoost-grey)](https://xgboost.readthedocs.io/en/release_3.0.0/) |  Library for optimized distributed gradient boosting. |
| [![badge](https://img.shields.io/badge/Imbalanced-Learn-grey)](https://imbalanced-learn.org/stable/) |  Library for classification with imbalanced classes. |
| [![badge](https://img.shields.io/badge/Joblib-grey)](https://joblib.readthedocs.io/en/stable/) |  Library for lightweight pipelining in Python. |

## Tools and Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage and Codespaces as cloud IDE for development. |
| [![badge](https://img.shields.io/badge/Jupyter-grey?logo=jupyter&logoColor=F37626)](https://jupyter.org/) | Descriptive and predictive data analysis and documentation for the back-end. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end and front-end programming language. |
| [![badge](https://img.shields.io/badge/Streamlit-grey?logo=streamlit&logoColor=FF4B4B)](https://streamlit.io/) | App framework to create front-end. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live application can be found deployed on [Heroku](https://maternal-health-risk-predictor-f82f6452b3b6.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

* Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
* Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.

Heroku needs some additional files in order to deploy properly.

* [requirements.txt](requirements.txt)
* [Procfile](Procfile)
* [setup.sh](setup.sh)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

* `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

* `pip3 freeze --local > requirements.txt`
* Note to only add packages needed for the live app, not those only used in jupyter notebooks.

The **[Procfile](Procfile)** can be created with the following command:

* `echo web: sh setup.sh && streamlit run app.py > Procfile`

The **[setup.sh](setup.sh)** file needs to look like:

```python
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

```

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

* At the Deploy tab, select GitHub as the deployment method.
* Select your repository name and click Search. Once it is found, click Connect.

Either (*recommended*):

* Select **Automatic Deployment** from the Heroku app.

Or:

* In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
* Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
* After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
* `git push heroku main`

The project should now be connected and deployed to Heroku!

If the slug size is too large then:

* Add large files not required for the app to the .slugignore file.
* Only add packages to requirements.txt that are needed in the live app, not those only used in jupyter notebooks (some ML packages can be very large).

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

* `pip3 install -r requirements.txt`.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/theresaabl/ML-maternal-health-risk).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	* `git clone https://www.github.com/theresaabl/ML-maternal-health-risk.git`
7. Press "Enter" to create your local clone.

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/theresaabl/ML-maternal-health-risk).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/863/maternal+health+risk) | Maternal Health Risk Dataset - dataset for this project |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files used as basis for parts of this documentation |
| [Churnometer](https://github.com/Code-Institute-Solutions/churnometer) | Code Institute walkthrough project inspiration, several custom functions used and adapted throughout the project |
| [ChatGPT](https://chatgpt.com) | Help with debugging and explanations |
| [Stackoverflow](https://stackoverflow.com/a/59839952) | Change label font size in seaborn plot |
| [Stackoverflow](https://stackoverflow.com/a/72034697) | Change tick and label font size in plotly express plot |
| [Discuss Streamlit](https://tinyurl.com/3dcv98ms) | Change dataframe containing dtypes as a column to dtype string |

### Acknowledgements

* I would like to thank my Code Institute mentor, [Mo Shami](https://github.com/mshami) for the support throughout the development of this project.
* I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for providing a great template for the documentation of this project.

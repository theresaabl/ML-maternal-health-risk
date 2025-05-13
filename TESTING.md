# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
|  | [app.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app.py) | ![screenshot](documentation/validation/python_app.png) |
| src | [data_management.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/src/data_management.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/src/data_management.py) | ![screenshot](documentation/validation/python_data_management.png) |
| src/machine_learning | [create_plots.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/src/machine_learning/create_plots.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/src/machine_learning/create_plots.py) | ![screenshot](documentation/validation/python_create_plots.png) |
| src/machine_learning | [evaluate_model.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/src/machine_learning/evaluate_model.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/src/machine_learning/evaluate_model.py) | ![screenshot](documentation/validation/python_evaluate_model.png) |
| src/machine_learning | [predictive_analysis.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/src/machine_learning/predictive_analysis.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/src/machine_learning/predictive_analysis.py) | ![screenshot](documentation/validation/python_predictive_analysis.png) |
| app_pages | [multipage.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app_pages/multipage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app_pages/multipage.py) | ![screenshot](documentation/validation/python_multipage.png) |
| app_pages | [page_health_risk_study.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app_pages/page_health_risk_study.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app_pages/page_health_risk_study.py) | ![screenshot](documentation/validation/python_page_health_risk_study.png) |
| app_pages | [page_model_evaluation.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app_pages/page_model_evaluation.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app_pages/page_model_evaluation.py) | ![screenshot](documentation/validation/python_page_model_evaluation.png) |
| app_pages | [page_predict_risk_level.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app_pages/page_predict_risk_level.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app_pages/page_predict_risk_level.py) | ![screenshot](documentation/validation/python_page_predict_risk_level.png) |
| app_pages | [page_project_hypothesis.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app_pages/page_project_hypothesis.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app_pages/page_project_hypothesis.py) | ![screenshot](documentation/validation/python_page_project_hypothesis.png) |
| app_pages | [page_summary.py](https://github.com/theresaabl/ML-maternal-health-risk/blob/main/app_pages/page_summary.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/theresaabl/ML-maternal-health-risk/main/app_pages/page_summary.py) | ![screenshot](documentation/validation/python_page_summary.png) |

## Manual Testing

Examples:

| Feature | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Register | Feature is expected to allow users to sign up for an account, once the user signs up the account is set to inactive and the account inactive page is shown. | Signed up as a new user, entering valid user data. | Account was created successfully, a message was shown and the account inactive page was displayed. | ![screenshot](documentation/features/signup.png)![screenshot](documentation/features/account-inactive.png) |
|  | Feature is expected to show a warning when user enters invalid data or fields are left empty. | Signed up as a new user, entering invalid user data or leaving fields empty. | Warning was shown inside the form. | (This is handled by allauth) |
| Login | Feature is expected to allow registered users with active accounts to sign in and access the resident dashboard. | Signed in with an active user account. | The resident space page was displayed. | ![screenshot](documentation/features/signin-message.png)![screenshot](documentation/features/dashboard.png) |

## User Story Testing

Examples:

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a Site User |  I can sign up for an account | so that I can request to get access to a resident dashboard. | ![screenshot](documentation/features/signup.png) |
| As a Site User | I can see a message when login does not work (yet) | so that I can know whether my account has been approved yet or not. | ![screenshot](documentation/features/account-inactive.png) |
| As a Site User | I can see the home page | so that I know what this site is about. | ![screenshot](documentation/features/home-lenovo.png) |

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Atheresaabl%2FML-maternal-health-risk%20label%3Abug&label=bugs)](https://www.github.com/theresaabl/ML-maternal-health-risk/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I have used [GitHub Issues](https://www.github.com/theresaabl/ML-maternal-health-risk/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/theresaabl/ML-maternal-health-risk/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

Examples:
![screenshot](documentation/bugs/issues-closed-bugs.png)

### Unfixed Bugs

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.
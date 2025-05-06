# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the bring your own data project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. In your newly created repo click on the green Code button. 

1. Then, from the Codespaces tab, click Create codespace on main.

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.12.1 as it inherits from the workspace, so it will be Python-3.12.1 as installed by Codespaces. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked


You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data. 


## Business Requirements
* Describe your business requirements


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them) 


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

First draft:

BUISINESS CASE:

- Better understand maternal health risk during pregnancy with the goal to define strategies and policies to decrease the health risk.
- Understand the main indicators of low/medium/high risk
- Predict risk for individuals or for populations

Industries:
-	Health and welfare
    -	WHO
    -	Local health authorities
-	Public Policy (?)
-	Medical
    -	Hospitals
    -	OB/GYN practices
-	Research
    -	University
    -	Non-academic research (government, ngo etc)

ML Model:
-	Classification

Questions:
-	What is the business objective requiring an ML solution?
    -	Predict maternal health risk based on health data collected during routine visits
-	Is data available for the training of the model, if yes which type of data?,
    -	Yes tabular data is available, it contains 6 features and 1 target:
        -	Age: object
        -	Cystilic BP: int
        -	Diastolic BP: int
        -	BS: int
        -	Body temperature: int
        -	Heart rate: int
        -	Target: risk: object (low/medium/high)
-	Does the customer need a dashboard or an API endpoint?
    -	dashboard
-	What does success look like?
        - Dashboard with all required buisiness outputs:
	
-	Can you break down the project into Epics and User Stories?
    -	Information gathering and data collection
    - 	Data visualization, cleaning, and preparation
    -	Model training, validation, and optimization.
    -	Dashboard planning, designing, and development
    -	Dashboard deployment and release.

-	Ethical or Privacy concerns?
The Project can remain ethical if we use cell image data without the patient's name or secret information


-	What level of prediction performance is needed?
    -	Since this is a healthcare related project and we aim to identify high-risk patients we aim to optimize the ML classifier for recall of the high-risk class
    -   Ideally, a recall of 80% or higher for high-risk patients is the goal
    -   However, the dataset at hand is relatively small and also moderately imbalanced, so in this scenario a high-risk recall of 70% would also be a reasonably good performance.
    -   With hyperparameter optimization we aim to reach a recall of above 80% but the minimum acceptable recall is 70% in this project.



-	What are the project inputs and intended outputs?
    -	Input: health data for a patient
    -	Output: health risk level
-	Does the data suggest a particular model?
-	How will the customer benefit?
    -	Analyses the main factors that contribute to pregnancy complications to inform health practitioners or policy makers.
    -	Makes it possible to quickly predict the maternal health risk based on basic health data that is taken during routine visits anyways.
    -	Makes the prediction more systematic and less room for individual error
    -	Combine with experience of health professionals!
    -	This allows less experienced staff to make predictions based on data from many women that they could not have gathered on their own
    -	Makes predictions quickly when under time pressure



## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.


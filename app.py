from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_health_risk_study import page_health_risk_study_body
from app_pages.page_predict_risk_level import page_predict_risk_level_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_model_evaluation import page_model_evaluation_body

app = MultiPage(app_name= "Maternal Health Risk Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("Maternal Health Risk Study", page_health_risk_study_body)
app.add_page("Predict Health Risk Levels", page_predict_risk_level_body)
app.add_page("Project Hypotheses and Validation", page_project_hypothesis_body)
app.add_page("ML: Model and Evaluation", page_model_evaluation_body)

app.run() # Run the  app
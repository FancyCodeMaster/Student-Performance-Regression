import numpy as np
import joblib
from config import model_path
import math

# Load the trained model
model = joblib.load(model_path)

# Define the prediction function
def predict_performance(hours_studied, previous_scores, extracurricular, sleep_hours, sample_questions):
    # Convert boolean to integer (1 for True, 0 for False)
    extracurricular = int(extracurricular)
    
    # Input data
    input_data = np.array([[hours_studied, previous_scores, extracurricular, sleep_hours, sample_questions]])
    
    # Use the loaded model to make a prediction
    prediction = model.predict(input_data)[0]
    
    if prediction < 0:
        prediction = 0
    elif prediction > 100:
        prediction = 100

    return math.ceil(prediction)
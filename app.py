from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests



app = Flask(__name__)


def get_diet_and_exercise(heighti, weighti, bpmi):
    try:
        # Convert input strings to float
        height = float(heighti)
        weight = float(weighti)
        bpm = float(bpmi)
    except ValueError:
        # Handle the case where conversion to float fails (e.g., invalid input)
        return "Invalid input. Please enter numeric values.", ""

    
    # Sample logic to generate diet and exercise based on ranges
    if 140 <= height <= 160 and 65 <= weight <= 85 and 55 <= bpm <= 75:
        diet_plan = "Include lean proteins, whole grains, and a variety of vegetables. Limit processed foods."
        exercise_recommendation = "Engage in a mix of cardio exercises like running and cycling, and incorporate strength training."
        return diet_plan, exercise_recommendation

    elif height < 140 or height > 160:
        diet_plan = "Your height is outside the typical range. Consider consulting with a nutritionist for a personalized diet plan."
        exercise_recommendation = "Focus on low-impact exercises such as swimming and yoga. Consult with a fitness professional."
        return diet_plan, exercise_recommendation


    elif 160 <= height <= 180 and 70 <= weight <= 90 and 60 <= bpm <= 80:
        diet_plan = "Emphasize a balanced diet with sufficient protein, healthy fats, and complex carbohydrates."
        exercise_recommendation = "Incorporate high-intensity interval training (HIIT) and weightlifting into your routine."
        return diet_plan, exercise_recommendation

    elif 170 <= height <= 190 and 75 <= weight <= 95 and 65 <= bpm <= 85:
        diet_plan = "Consume nutrient-dense foods, including plenty of fruits, vegetables, and lean proteins."
        exercise_recommendation = "Participate in activities like jogging, cycling, and circuit training for overall fitness."
        return diet_plan, exercise_recommendation

    elif 150 <= height <= 170 and 55 <= weight <= 75 and 50 <= bpm <= 70:
        diet_plan = "Opt for a plant-based diet with a focus on whole foods. Ensure an adequate intake of vitamins and minerals."
        exercise_recommendation = "Engage in activities such as hiking, Pilates, and bodyweight exercises."
        return diet_plan, exercise_recommendation

    elif height < 150 or height > 190:
        diet_plan = "Seek guidance from a nutritionist to tailor a diet plan based on your unique needs."
        exercise_recommendation = "Consider low-impact activities like elliptical training and consult with a fitness expert."
        return diet_plan, exercise_recommendation

    elif 180 <= height <= 200 and 85 <= weight <= 105 and 70 <= bpm <= 90:
        diet_plan = "Prioritize a diet rich in complex carbs, lean proteins, and healthy fats. Stay hydrated."
        exercise_recommendation = "Incorporate compound exercises like squats and deadlifts, along with cardiovascular workouts."
        return diet_plan, exercise_recommendation

    elif 160 <= height <= 180 and 60 <= weight <= 80 and 55 <= bpm <= 75:
        diet_plan = "Include a variety of colorful fruits and vegetables in your diet. Limit sugary and processed foods."
        exercise_recommendation = "Combine aerobic exercises like dancing and cycling with resistance training."
        return diet_plan, exercise_recommendation

    elif 140 <= height <= 160 and 70 <= weight <= 90 and 65 <= bpm <= 85:
        diet_plan = "Focus on maintaining a well-balanced diet with sufficient fiber, proteins, and healthy fats."
        exercise_recommendation = "Engage in activities such as swimming, rowing, and full-body strength workouts."
        return diet_plan, exercise_recommendation

    else:
        diet_plan = "Consult with a registered dietitian and fitness professional for personalized advice."
        exercise_recommendation = "Customize your exercise routine based on your fitness level and goals."
    
    return diet_plan, exercise_recommendation








@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        bpm = request.form['bpm']
        
        # Send data to AI module
        diet_plan, exercise_recommendation = get_diet_and_exercise(height, weight, bpm)

        return render_template('results.html', diet_plan=diet_plan, exercise_recommendation=exercise_recommendation)
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

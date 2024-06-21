from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
try:
    with open('model_campus_placement.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def index():
    result = request.args.get('result')
    score = request.args.get('score')
    return render_template('index.html', result=result, score=score)

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            # Retrieve form data
            gender = request.form.get('gender')
            ssc = request.form.get('ssc')
            hsc = request.form.get('hsc')
            cgpa = request.form.get('cgpa')
            stream = request.form.get('stream')
            aptitude = request.form.get('quiz-score')
            internships = request.form.get('internships')
            experience = request.form.get('experience')
            backlogs = request.form.get('backlogs')
            coding = request.form.get('coding')

            # Validate inputs
            if not all([gender, ssc, hsc, cgpa, stream, aptitude, internships, experience, backlogs, coding]):
                raise ValueError("All fields are required.")

            # Convert inputs to appropriate types
            try:
                gender = 0 if gender == 'male' else 1
                ssc = float(ssc)
                hsc = float(hsc)
                cgpa = float(cgpa)
                stream = {'Sci&Tech': 2, 'Comm&Mgmt': 1, 'Others': 0}[stream]
                aptitude = float(aptitude)
                internships = int(internships)
                experience = 0 if experience == 'No' else 1
                backlogs = int(backlogs)
                coding = float(coding)
            except ValueError as ve:
                raise ValueError(f"Invalid input: {ve}")

            # Create a new DataFrame for prediction
            new_data = pd.DataFrame({
                'gender': [gender],
                'SSC Score': [ssc],
                'HSC Score': [hsc],
                'CGPA': [cgpa],
                'Stream': [stream],
                'Aptitude': [aptitude],
                'No of internships': [internships],
                'working experience': [experience],
                'No of backlogs': [backlogs],
                'Coding Skills': [coding]
            })

            # Make the prediction
            prediction = model.predict(new_data)[0]
            probability = model.predict_proba(new_data)[0][1]

            result = "Placed" if prediction == 1 else "Not Placed"
            result += f" with a probability of {probability:.2f}"

        except Exception as e:
            result = f"Error in prediction: {e}"
    else:
        result = "Model not loaded properly."

    return redirect(url_for('index', result=result))

@app.route('/quiz')
def quiz():
    return render_template('index1.html')

@app.route('/coding')
def coding():
    return render_template('coding.html')


if __name__ == '__main__':
    app.run(debug=True)

# StudentPlacementPrediction
This project uses logistic regression to predict whether a student is likely to get placed during campus placements based on several academic and aptitude features.

Project Workflow
Data Collection:
The model is trained using a dataset that includes the following key features:

Gender: Male or Female.
SSC Marks: 10th grade percentage/marks.
HSC Marks: 12th grade percentage/marks.
B.Tech CGPA: The cumulative grade point average in the undergraduate program.
Number of Backlogs: Total subjects with backlogs (if any).
Years of Experience: Industry experience or internships.
Aptitude Quiz Score: The result of a 10-question quiz covering general aptitude. The quiz generates random questions each time.
Coding Quiz Score: The result of a 10-question coding quiz that tests students on theoretical programming concepts and code snippet output.
Feature Engineering:
The collected data is preprocessed to ensure it's in a format suitable for the logistic regression model. This includes handling missing values, scaling the data, and encoding categorical variables like gender.

Model Training:
The logistic regression model is trained on the dataset. It learns patterns in the features to estimate the probability that a student will get placed. The model returns a probability score between 0 and 1, where a higher value indicates a greater likelihood of placement.

Aptitude and Coding Quizzes:
Two dynamic quizzes are part of the process:

Aptitude Quiz: A 10-question quiz that generates random questions related to reasoning, quantitative aptitude, and general knowledge.
Coding Quiz: A 10-question quiz focusing on programming theory and code snippets, challenging students to predict outputs or answer theoretical questions.
The results of these quizzes are converted into scores and fed into the logistic regression model to improve its prediction accuracy.

Prediction:
Once all the input data is entered, the model predicts the likelihood of placement. The prediction is shown as a probability score that represents how likely the student is to get placed in a campus recruitment process.

Technologies Used
Python: Core programming language.
Flask: For building the web application.
pandas: For data manipulation and preprocessing.
scikit-learn: For building and training the logistic regression model.
Werkzeug: For handling quiz sessions and other backend functionalities.
Project Setup
Clone the repository.
Install dependencies using pip install -r requirements.txt.
Run the Flask app using python app.py.
Access the application through the local web server (usually localhost:5000).
This project provides a general prediction model for student placements, offering a probability score that helps students gauge their chances of being placed in campus recruitment processes. The model does not cater to any specific company or field but provides a broad overview of placement potential.

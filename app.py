import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/question')
def question():
    return render_template(
        'questions/1.html')
        
@app.route('/error')
def error():
    return render_template(
        'error.html')

@app.route('/success')
def success():
    return render_template(
        'success.html')

@app.route('/about')
def about():
    return render_template(
        'about.html')
        
@app.route('/questions/<string:answer>/<int:question_id>')
def questions( answer, question_id ):
    try:
        if question_id == 1:
            if answer == "blue":
                return render_template(
                'success.html')
            else:
                return render_template(
                    'error.html',
                    correctAnswer = "blue")
        elif question_id == 2:
            if answer == "YOUR ANSWER HERE":
                return render_template(
                    'success.html')
            else:
                return render_template(
                    'error.html',
                    correctAnswer = "YOUR CORRECT ANSWERE HERE")
        #TODO
        # Add 3more for each question id and fix your template accordingly
    except ValueError:
        print ('Oops thats an error should be caught')
    

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
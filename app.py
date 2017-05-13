import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/question')
def question():
    return render_template(
        'questions/1.html')
        
@app.route('/')
def index():
    return render_template(
        'index.html')

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
        
# @app.route('/questions/<string:answer>/<int:question_id')
# def questions(answer, question_id ):
  #  if question_id = 1
  #      if answer = "blue"
   #        return render_template(
    #           'success.html')
    #    elif
    #      return render_template(
    #         'error.html',
    #          correct_answer = answer)
    #elif question_id = 2
     #   return render_template(
      #      'questions/2.html')
    #elif question_id = 3
    #    return render_template(
    #        'questions/3.html')
#    elif question_id = 4 
#        return render_template(
#            'questions/4.html')
#    elif question_id = 5
#        return render_template(
#            'questions/5.html')


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
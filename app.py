import os
from flask import Flask, render_template, request

app = Flask(__name__)

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


app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
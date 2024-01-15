import time
import random
from typing import Union
from flask import Flask, jsonify, render_template, request
from templates import Page

p = Page()

p.add_form(title="test form", type="number")
p.create_page()
p.join_and_write("templates/index.html")

def calculate(input_value):
    time.sleep(5)
    return random.randint(0,10), random.randint(0,10)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculer_salaire', methods=['POST'])
def calculer_salaire():
    try:
        input_value = float(request.form['input_value'])
        #doubled_value = 2 * input_value
        #result_min, result_max = retrouver_salaire(input_value,interval=True)
        result_min, result_max = calculate(input_value)
        return jsonify({'success': True, 'result_min': result_min, 'result_max' : result_max})
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid input'})
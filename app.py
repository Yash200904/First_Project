# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get input values from the form
        a = int(request.form['a'])
        b = int(request.form['b'])

        # Calculate the sum
        result = a + b

        # Pass the result back to the front-end
        return render_template('result.html', result=result)

    except Exception as e:
        # Handle any errors that might occur during calculation
        error_message = str(e)
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

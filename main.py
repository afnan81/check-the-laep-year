# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def is_leap_year(year):
    """Check if a year is a leap year"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            if year <= 0:
                error = "Please enter a valid positive year"
            else:
                result = is_leap_year(year)
        except ValueError:
            error = "Please enter a valid integer year"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import render_template, request, redirect
from decimal import Decimal
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle = 'My Loan Calculator')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        form = request.form
        loan_amount = int(form['loan_amount'])
        number_payments = int(form['number_payments'])
        interest_rate = Decimal(form['interest_rate'])
        firstD = ((1+interest_rate)**number_payments)-1
        secondD = (((1+interest_rate)**number_payments)*interest_rate)
        calculate = '${:,.2f}'.format(Decimal(loan_amount/(firstD/secondD)))
        return render_template('index.html', display=calculate, pageTitle="My Loan Calculator")

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from ST_error_checker import run

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET']) # your url

def calc():
    # pass in user input to the api 
    error = ''
    td = ''
    res = []
    if request.method=='POST' and 'theta' in request.form and 'phi' in request.form:
        Theta = float(request.form.get('theta')) 
        Phi = float(request.form.get('phi'))
        TP = float(request.form.get('totalPower'))
        H = float(request.form.get('Hcounts'))
        V = float(request.form.get('Vcounts'))
        D = float(request.form.get('Dcounts'))
        A = float(request.form.get('Acounts'))
        R = float(request.form.get('Rcounts'))
        L = float(request.form.get('Lcounts'))

        res = run(Theta, Phi, TP, D, A, R, L, H, V)
    return render_template("index.html", res=res)
    

if __name__ == '__main__':
    app.run(debug=True)



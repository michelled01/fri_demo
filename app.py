from flask import Flask, render_template, request, url_for
from ST_error_checker import altGo, convertPercentage, go

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET']) # for inputs and outputs

# TODO:
# Add error messages
# Add css
# Get verified by using other group's inputs

def calc():
    res = []
    if request.method=='POST' and 'theta' in request.form and 'phi' in request.form and 'Hcounts' in request.form and 'Vcounts' in request.form and 'Dcounts' in request.form and 'Acounts' in request.form and 'Rcounts' in request.form and 'Lcounts' in request.form:
        Theta = float(request.form.get('theta')) 
        Phi = float(request.form.get('phi'))
        TP1 = float(request.form.get('totalPower1'))
        TP2 = float(request.form.get('totalPower2'))
        TP3 = float(request.form.get('totalPower3'))
        H = float(request.form.get('Hcounts'))
        V = float(request.form.get('Vcounts'))
        D = float(request.form.get('Dcounts'))
        A = float(request.form.get('Acounts'))
        R = float(request.form.get('Rcounts'))
        L = float(request.form.get('Lcounts'))
        #res = go(Theta, Phi, TP, D, A, R, L, H, V)
        res = altGo(Theta, Phi, TP1, TP2, TP3, D, A, R, L, H, V)
    return render_template("index.html", res=res)
    

if __name__ == '__main__':
    app.run(debug=True)
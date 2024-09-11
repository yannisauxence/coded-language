from datetime import date
from flask import Flask, render_template, request, url_for
import string
import pandas as pd
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/translator", methods=['GET'])
def translator():
    psc = date.today()
    return render_template('reg.html', psc=psc)

@app.route("/results",  methods=['POST'])   
def results():
    translated_text = ' '
    m = request.form['msg']
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    o = ""
    j = 0
    #n = ''
    for i in m:
        if i == ' ':
            o += " "
            #print(n,end=' ')
        else:
            for j in range(26):
                if i == alphabet_lower[j]:
                    if j in range(13):
                        #print(alphabet[j+13], end="")
                        o += alphabet_lower[j+13]
                    if j in range(13,26):
                        #print(alphabet[j - 13],end="")
                        o += alphabet_lower[j - 13]
                elif i == alphabet_upper[j]:
                    if j in range(13):
                        #print(alphabet[j+13], end="")
                        o += alphabet_upper[j+13]
                    if j in range(13,26):
                        #print(alphabet[j - 13],end="")
                        o += alphabet_upper[j - 13]
    translated_text = o
    return render_template('results.html', translated_text=translated_text)

@app.route("/data")
def data():
    #tx=""
    tx = pd.read_excel('Records.xlsx', usecols="A:K")
    tx.fillna("N/A", inplace = True)
    return render_template('data.html', column_names=tx.columns.values, row_data=list(tx.values.tolist()),
                           link_column="Index", zip=zip, tx=tx)
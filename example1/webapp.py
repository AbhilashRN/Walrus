from flask import Flask, render_template, request, jsonify
import pandas
app = Flask(__name__)

def getmovienames(abd):
    df = pandas.read_csv("coref.csv")
    movienames = {}
    k=0
    for i in range(len(df["Movie Name"])):
        if((df["Movie Name"].iloc[i][0]==abd['submit'])):
            movienames[k] = (df["Movie Name"].iloc[i])
            k = k+1
    return (movienames)

@app.route('/')
def student():
   return render_template('Alpha.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
        result = getmovienames(request.form) #use results to dynamicaly generate buttons
        return render_template('MovieList.html',result = result)

@app.route('/movieinfo',methods = ['POST', 'GET'])
def movieinfo():
    if request.method == 'POST':
        results = getmovieinfo() #define this funtion
        return render_template('MovieInfo.html',result=results )

@app.route('/rec',methods = ['POST', 'GET'])
def movieinfo():
    if request.method == 'POST':
        results = getmovieinfo() #define this funtion
        return render_template('Rec.html',result=results)

if __name__ == '__main__':
   app.run(debug = True)
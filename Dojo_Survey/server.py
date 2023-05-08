from flask import Flask , render_template, request,redirect, session # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'elsecreto'

@app.route('/')  
def display_form():
    return render_template('form.html')

@app.route('/process', methods=['POST'])  
def process():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('info.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__=="__main__": 
    app.run(debug=True, port=5001) 
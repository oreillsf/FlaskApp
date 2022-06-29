

from flask import Flask, render_template, redirect, request
from application import db
from application import app
from application.models import Data


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/returnToIndex')
def returnToIndex():
    return render_template('index.html')

@app.route('/pinSet')
def pinSet():
    return render_template('pin.html')

@app.route('/musicalSet')
def musicalSet():
    return render_template('musical.html')

@app.route('/graphicalSet')
def graphicalSet():
    return render_template('graphical.html')

@app.route('/informedConsentPage')
def informedConsentPage():
    return render_template('informedConsent.html')


@app.route('/surveyPage')
def surveyPage():
    return render_template('survey.html')


@app.route('/consentPageForm', methods=['POST'])
def consentPageForm():
    choice1 = request.form['choice1']
    choice2 = request.form['choice2']
    choice3 = request.form['choice3']
    choice4 = request.form['choice4']
    choice5 = request.form['choice5']
    choice6 = request.form['choice6']

    if request.method == 'POST':
            data_entered = Data(notes=choice1)
            try:     
                print("choices are : " + choice1 + " "+choice2+" " +
                choice3+" "+choice4+" "+choice5+" "+choice6)
                db.session.add(choice1)
                print("choice1 was commited")
                db.session.commit()        
                db.session.close()
            except:
                db.session.rollback()

                print("choices are : " + choice1 + " "+choice2+" " +
                choice3+" "+choice4+" "+choice5+" "+choice6)
    return render_template('questions.html')


@app.route('/questionForm', methods=['POST'])
def questionForm():
    ansQ1 = request.form['q1']
    ansQ2 = request.form['q2']
    ansQ3 = request.form['q3']
    ansQ4 = request.form['q4']
    ansQ5a = request.form['q5a']
    ansQ5b = request.form['q5b']
    ansQ5c = request.form['q5c']
    ansQ5d = request.form['q5d']
    ansQComm5a = request.form['pinComment5a']
    ansQComm5b = request.form['pinComment5b']
    ansQComm5c = request.form['pinComment5c']
    ansQComm5d = request.form['pinComment5d']
    ansQ6 = request.form['q6']    
    ansQ7 = request.form['q7']
    ansQ6Comm = request.form['pinComment6']
    print()
    ansQ7Comm = request.form['pinComment7']
    print("Q1 : "+ansQ1)
    print("Q2 : "+ansQ2)
    print("Q3 : "+ansQ3)
    print("Q4 : "+ansQ4)
    print("Q5a : "+ansQ5a)
    print("\n Q5b : "+ansQ5b)
    print("\n Q5c : "  +ansQ5c)
    print("\n Q5d : "+ansQ5d)
    print("\n Q6 : "+ansQ6)
    print("\n Q7 : "+ansQ7)
    print("\nQ5 A Comments : "+ansQComm5a)
    print("\n \nQ5 B Comments : "+ansQComm5b)
    print( "\n \nQ5 C Comments : "+ansQComm5c )
    print( "\n \nQ5 D Comments : " + ansQComm5d)
    print( "\n \nQ6 Comments : " + ansQ6Comm)
    print( "\n \nQ7 Comments : " + ansQ7Comm)
    #insert all the data to db
    return render_template('passwords.html')

@app.route('/passwordForm1', methods=['POST'])
def passwordForm1():
    username = request.form['username']
    password = request.form['password']
    print("username : " + username +"\n Password "+ password)
    #insert this data to db   
    return render_template('passwordsLogin.html')

@app.route('/passwordLoginForm1', methods=['POST'])
def passwordLoginForm1():
    username = request.form['username']
    password = request.form['password']
    attempt =1
    print("username : " + username +"\n Password "+ password)
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('pin.html') else go to below
    return render_template('passwordsLogin2.html')

@app.route('/passwordLoginForm2', methods=['POST'])
def passwordLoginForm2():
    username = request.form['username']
    password = request.form['password']
    attempt =2
    print("username : " + username +"\n Password "+ password)
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('pin.html') else go to below
    return render_template('passwordsLogin3.html')

@app.route('/passwordLoginForm3', methods=['POST'])
def passwordLoginForm3():
    username = request.form['username']
    password = request.form['password']
    attempt =3
    print("username : " + username +"\n Password "+ password)
    #insert this data to db   
    return render_template('pin.html') 

@app.route('/pinForm1', methods=['POST'])
def pinForm1():
    username = request.form['username']
    pin = request.form['pin']
    print("username : " + username +"\n Password "+ pin)
    #insert this data to db   
    return render_template('pinLogin.html')

@app.route('/pinLoginForm1', methods=['POST'])
def pinLoginForm1():
    username = request.form['username']
    pin = request.form['pin']
    attempt =1
    print("username : " + username +"\n Password "+ pin)
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('graphical.html') else go to below
    return render_template('pinLogin2.html')

@app.route('/pinLoginForm2', methods=['POST'])
def pinLoginForm2():
    username = request.form['username']
    pin = request.form['pin']
    attempt =2
    print("username : " + username +"\n Password "+ pin)
    #insert this data to db   
    #cross verify if data is correct with db. if so go to return render_template('graphical.html') else go to below
    return render_template('pinLogin3.html')

@app.route('/pinLoginForm3', methods=['POST'])
def pinLoginForm3():
    username = request.form['username']
    pin = request.form['pin']
    attempt =3
    print("username : " + username +"\n Password "+ pin)
    #insert this data to db   
    return render_template('graphical.html') 

@app.route('/graphicalForm1', methods=['POST'])
def graphicalForm1():
    listOfImg = request.form.getlist('imgs');
    #push these names to db
    return render_template('graphicalLogin.html')

@app.route('/graphicalLoginForm1', methods=['POST'])
def graphicalLoginForm1():
    listOfImg = request.form.getlist('imgs')
    attempt = 1

    #push these names to db 
    #retrieve previously inserted data and cross check; ensure to use "in op" so we wont have to worry about order
    #if match then go to return render_template('musical.html') else the one below
    return render_template('graphicalLogin2.html')

@app.route('/graphicalLoginForm2', methods=['POST'])
def graphicalLoginForm2():
    listOfImg = request.form.getlist('imgs');
    attempt = 2

    #push these names to db 
    #retrieve previously inserted data and cross check; ensure to use "in op" so we wont have to worry about order
    #if match then go to return render_template('musical.html') else the one below
    return render_template('graphicalLogin3.html')

@app.route('/graphicalLoginForm3', methods=['POST'])
def graphicalLoginForm3():
    listOfImg = request.form.getlist('imgs');
    attempt = 3
    #push these names to db 
    return render_template('musical.html')

@app.route('/musicalForm1', methods=['POST'])
def musicalForm1():
    musicName = request.form['music']
    #insert this value to db    
    return render_template('musicalLogin.html')

@app.route('/musicalLoginForm1', methods=['POST'])
def musicalLoginForm1():
    musicName = request.form['music']
    attempt=1
    #push these names to db 
    #retrieve previously inserted data and cross check; 
    #if match then go to return render_template('survey.html') else the one below
    return render_template('musicalLogin2.html')

    

@app.route('/musicalLoginForm2', methods=['POST'])
def musicalLoginForm2():
    musicName = request.form['music']
    attempt =2
    #push these names to db 
    #retrieve previously inserted data and cross check; 
    #if match then go to return render_template('survey.html') else the one below
    return render_template('musicalLogin3.html')

@app.route('/musicalLoginForm3', methods=['POST'])
def musicalLoginForm3():
    musicName = request.form['music']
    attempt =3
    #push these names to db 
    return render_template('survey.html')

@app.route('/surveyQuestion', methods=['POST'])
def surveyQuestion():
    ansQ1 = request.form['q1']
    ansQ2 = request.form['q2']
    ansQ3 = request.form['q3']
    ansQ4 = request.form['q4']
    ansQ1Comm = request.form['pinComment1']
    ansQ2Comm = request.form['pinComment2']
    ansQ3Comm = request.form['pinComment3']
    ansQ4Comm = request.form['pinComment4']
    ansQ5Comm = request.form['pinComment5']
    return render_template('thankyou.html')


if __name__ == "__main__":
  app.run(debug=True)

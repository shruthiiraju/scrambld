from flask import Flask, session
from flask import request, render_template, redirect,  url_for, make_response
from flask_session import Session
import random

app = Flask(__name__)
app.debug = True
app.secret_key = "super secret key"


ewords = ['house', 'safety', 'switch', 'light', 'value', 'screen', 'fake', 'police', 'danger', "release", "chair", "scramble", "pencil", "board", "english", "india",'bangle','rocket','shirt','family',"garlic"]


mwords = ['recycle', "keyboard", "binary","hundred",'document', 'python', 'german', 'scramble', 'september', 'license',"eclair", "section", "dioxide","pigment", "process", "ordinary", "elements", "language",  "wednesday",
          "kingdom","fourth","blanket","airport","cabinet","disease","organic" ]


hwords = ['automatic', 'irresponsible', 'eligible', 'bachelor', "photosynthesis", "carpentry","Zimbabwe",
          "concentric", "parentheses", "assessment", "locomotive", "evidence", "dictionary","bungalow","chipmunk","dinosaur","dyslexia","housefly","kilobyte","marigold","mythical","oriental"]





@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('word', " ")
    return resp


@app.route('/difficulty', methods=['GET', 'POST'])
def diff():
    if request.method == 'POST':
        resp = make_response(render_template('level.html'))
        resp.set_cookie('word', " ")
        return resp
    else:
        resp = make_response(render_template('level.html'))
        resp.set_cookie('word', " ")
        return resp
        

@app.route('/chooselvl',methods=['POST'])
def chooselvl():
    word = request.cookies.get('word')
    if word == " ":
        choice = request.form['lvl']
        if choice == "1":
            listlength = len(ewords)
            word = ewords[random.randrange(0, listlength)]
        elif choice == "2":
            listlength = len(mwords)
            word = mwords[random.randrange(0, listlength)]
        elif choice =='3':
            listlength = len(hwords)
            word = hwords[random.randrange(0, listlength)]

    wordlist = list(word)
    scrwordlist = random.sample(wordlist, len(wordlist))
    
    scrword=" "
    
    for i in range(0,len(scrwordlist)):
        scrword=(scrword + scrwordlist[i] + " " )
    print (scrword)
    scramble = { "Your word is....":scrword}
    
    resp = make_response(render_template('guess.html',scramble=scramble))
    resp.set_cookie('word', word)
    return resp

@app.route('/checkguess',methods=['POST'])
def check():
    guess = request.form['guess']
    word = request.cookies.get('word')
    if guess == word or guess==(word+" "):
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

@app.route('/about')
def about():
    return render_template('about.html')
    


if __name__ == "__main__":
    app.run()
from flask import Flask, session
from flask import request, render_template, redirect,  url_for
from flask_session import Session
import random

app = Flask(__name__)
app.debug = True
app.secret_key = "super secret key"

ewords = ["and", 'house', 'safety', 'switch', 'light', 'value', 'screen', 'fake', 'police', 'danger', "release", "chair", "scramble", "pencil", "hundred", "board", "keyboard", "binary", "english", "india"]
mwords = ['recycle', 'document', 'python', 'german', 'scramble', 'september', 'license', "section", "dioxide",
          "pigment", "process", "ordinary", "elements", "language", "zimbabwe", "wednesday", "kingdom", ]
hwords = ['automatic', 'irresponsible', 'eligible', 'bachelor', "photosynthesis", "carpentry",
          "concentric", "parentheses", "assessment", "locomotive", "evidence", "dictionary"]





@app.route('/')
def index():

    return render_template('index.html')


@app.route('/difficulty')
def diff():                                 
    return render_template('level.html')

@app.route('/chooselvl',methods=['POST'])
def chooselvl():
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
    return render_template('guess.html',scramble=scramble)

if __name__ == "__main__":
    app.run()
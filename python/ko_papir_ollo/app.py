from flask import Flask, request, render_template, redirect, url_for
from random import randint as rn

app = Flask(__name__)

BOT_VALASZTASOK = ["ko","papir","ollo"]
allas = [0,0]

@app.route('/', methods=['GET', 'POST'])
def index():
    nyert = False
    bot_valasz = ""
    jatekos_valasz = request.form.get('valasztas')
    elkuldve = False
    is_post = False
    
    if request.method == 'POST' and jatekos_valasz != None:

        is_post = True

        bot_valasz = BOT_VALASZTASOK[rn(0,2)]
        elkuldve = True

        if (jatekos_valasz == 'ko' and bot_valasz == 'ollo') or (jatekos_valasz == 'ollo' and bot_valasz == 'papir') or (jatekos_valasz == 'papir' and bot_valasz == 'ko'):
            nyert = True
            allas[0] += 1

        elif jatekos_valasz == bot_valasz:
            nyert = None
        
        else:
            allas[1] += 1
        #return redirect(url_for('index'))

    return render_template('index.html',bot_valasz = bot_valasz, elkuldve = elkuldve, nyert = nyert, allas = allas)

if __name__ == '__main__':
    app.run(debug=True)
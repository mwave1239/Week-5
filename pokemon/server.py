from flask import Flask, request, redirect, render_template, session, flash

app = Flask(__name__)
app.secret_key = "SecretKeyDont"

@app.route('/')
def display_pokemon():
    return render_template('index.html')

app.run(debug=True)

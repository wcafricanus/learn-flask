from flask import render_template, flash, redirect
from app import app
from app.entities.test import Test
from .forms import LoginForm
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'miguel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/results', methods=['GET','POST'])
def results():
    url = app.config['API_URL']
    url = url + 'test'
    response = requests.get(url)
    data = json.loads(response.content)
    tests = data['_items']
    app.tests = tests
    return render_template('results.html',
                           title=' Cognitive Test Results',
                           tests=app.tests)

@app.route('/results/<name>', methods=['GET'])
def show_result(name):
    return app.tests[1]['pic']

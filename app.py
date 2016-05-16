import os
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

PORT = os.getenv('PORT', 5000)
HOST = os.getenv('HOST', '0.0.0.0')
app = Flask(__name__)

# adding bootstrap
bootstrap = Bootstrap(app)


users = {
    1: {
        "name": "Doron Segal",
        "admin": True,
        "comments": []
    },
    2: {
        "name": "Regular",
        "admin": False,
        "comments": [
            "jkasndfkjasdbnf",
            "jkasndfkjasdbnf"
        ]
    },
    3: {
        "name": "undefined admin",
        "admin": False,
        "comments": []
    }
}

@app.route('/')
def base():
  return render_template('home.html')

@app.route('/users/<int:id>')
def getUserById(id):
    if users.has_key(id):
        return render_template('users/index.html', user=users[id])
    return render_template('users/not_found.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact(info):
    return render_template('contact/thank_you')

@app.route('/users')
def getAllUsers():
    usersTmp = []
    for id in users.keys():
        usersTmp.append({ "id": id, "name": users[id]["name"] })
            
    return render_template('users/all.html', users=usersTmp)


if __name__ == '__main__':
   app.run(host=HOST, port=PORT, debug=True)

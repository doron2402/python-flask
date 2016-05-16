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
def contact():
    return render_template('contact/form.html')

@app.route('/users')
def getAllUsers():
    usersTmp = []
    for id in users.keys():
        usersTmp.append({ "id": id, "name": users[id]["name"] })
            
    return render_template('users/all.html', users=usersTmp)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', error_msg="404"), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', error_msg="500"), 500

if __name__ == '__main__':
   app.run(host=HOST, port=PORT, debug=True)

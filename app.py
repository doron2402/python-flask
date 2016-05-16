import os
from flask import Flask, render_template, request, url_for, jsonify, make_response
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

PORT = os.getenv('PORT', 5000)
HOST = os.getenv('HOST', '0.0.0.0')
app = Flask(__name__)


bootstrap = Bootstrap(app)
moment = Moment(app)


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

contactInfo = [{
    "email": "test@test.com",
    "mobile": "123-345-5677"
}]

@app.route('/')
def base():
  return render_template('home.html', current_time=datetime.utcnow())

@app.route('/users/<int:id>')
def getUserById(id):
    if users.has_key(id):
        return render_template('users/index.html', user=users[id])
    return render_template('users/not_found.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact/form.html')

@app.route('/contact',  methods=['POST'])
def postContact():
    email = request.form["email"]
    if str(email) == "":
        response = make_response(jsonify(code="error"), 400)
        return response
    
    contactInfo.append(request.form)
    
    return jsonify(email=email,
                   code="ok",
                   redirect_url="/contact/thanks/%s" % email)

@app.route('/contact/all')
def showAllContact():
    return render_template('contact/all.html', data=contactInfo)

@app.route('/contact/thanks/<email>')
def thankYouContact(email):
    return render_template('contact/thank_you.html', data=email)                   

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

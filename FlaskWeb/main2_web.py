# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail
# import json
# from datetime import datetime


# with open('config.json', 'r') as c:
#     params = json.load(c)["params"]

# local_server = True
# app = Flask(__name__)
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = params['gmail-user'],
#     MAIL_PASSWORD=  params['gmail-password']
# )
# mail = Mail(app)
# if(local_server):
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

# db = SQLAlchemy(app)


# class Contacts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     # phone_num = db.Column(db.String(12), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     email = db.Column(db.String(20), nullable=False)


# class Posts(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     slug = db.Column(db.String(21), nullable=False)
#     content = db.Column(db.String(120), nullable=False)
#     date = db.Column(db.String(12), nullable=True)
#     # img_file = db.Column(db.String(12), nullable=True)


# @app.route("/")
# def home():
#     # posts = Posts.query.filter_by().all()[0:2]

#     return render_template('index.html', params=params )


# @app.route("/blog")
# def blog():
#     return render_template('post.html', params=params)


# @app.route("/post/", methods=['GET'])
# def post_route(post_slug):
#     post = Posts.query.filter_by(slug=post_slug).first()
#     return render_template('post.html', params=params, post=post)

# @app.route("/about")
# def about():
#     return render_template('about.html', params=params)


# @app.route("/contact", methods = ['GET', 'POST'])
# def contact():
#     if(request.method=='POST'):
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#         entry = Contacts(name=name, msg = message, date= datetime.now(),email = email )
#         db.session.add(entry)
#         db.session.commit()
#         mail.send_message('New message from ' + name,
#                           sender=email,
#                           body=message + "\n",
#                           recipients = [params['gmail-user']]
#                           )
#     return render_template('contact.html', params=params)


# app.run(debug=True)
# i 
# while i < 100:
    # print ("")

from tokenize import String
from unicodedata import name


print("I LOVE YOU \n" * 100)
    
String name = "i love you"

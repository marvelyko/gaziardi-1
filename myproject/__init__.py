from flask import Flask, render_template
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
#'postgresql+psycopg2://postgres:zklmjase3.141592@127.0.0.1:5432/gaziardi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "Gaziardi.Ltd@gmail.com"
app.config['MAIL_PASSWORD'] = "gaziardi74123"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
Migrate(app, db)


def send_mail(bid):
    with app.app_context():
        msg = Message("New order",sender="Gaziardi.Ltd@gmail.com",
                      recipients=["Mr.ktevzadze@gmail.com"],
                      reply_to="Gaziardi.Ltd@gmail.com")
        msg.body = f'''
            new order of {bid.product.name}
            order N : {bid.id},
            customer: {bid.name} {bid.surname}
            quantity: {bid.quantity}
            address : {bid.address}, {bid.city}, {bid.country}
            phone : {bid.phone}
            email : {bid.email}
            '''.encode("utf-8")
        mail.send(msg)

def send_mail_thread(bid):
    thr = Thread(target=send_mail,args=[bid])
    thr.start()

from myproject.auth.views import auth_blueprint
from myproject.admin.views import admin_blueprint
from myproject.index.views import index_blueprint
from myproject.category.views import category_blueprint
from myproject.product.views import product_blueprint
from myproject.cart.views import cart_blueprint
from myproject.checkout.views import checkout_blueprint
from myproject.contact.views import contact_blueprint
from myproject.search.views import search_blueprint

app.register_blueprint(auth_blueprint,url_prefix="/")
app.register_blueprint(admin_blueprint,url_prefix="/adm912EC803B2CE49E4A541068D495AB570")
app.register_blueprint(index_blueprint,url_prefix="/")
app.register_blueprint(category_blueprint,url_prefix="/category")
app.register_blueprint(product_blueprint,url_prefix="/product")
app.register_blueprint(cart_blueprint,url_prefix="/cart")
app.register_blueprint(checkout_blueprint,url_prefix="/checkout")
app.register_blueprint(contact_blueprint,url_prefix="/contact")
app.register_blueprint(search_blueprint,url_prefix="/search")


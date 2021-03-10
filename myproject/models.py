from myproject import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    manufacturer = db.Column(db.String)
    quantity = db.Column(db.Float)
    min_bid = db.Column(db.Float)
    image = db.Column(db.String)
    description = db.Column(db.String)
    sold_quantity = db.Column(db.Float)
    rating = db.Column(db.Float)
    comments = db.Column(db.String)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    tags = db.Column(db.String)
    shipping_price = db.Column(db.Float)
    location = db.Column(db.String)
    price=db.Column(db.Float)
    expire_data=db.Column(db.String)
    unit = db.Column(db.String)
    bids = db.relationship("Bid",backref="product",lazy="subquery")

    def __init__(self, name, manufacturer, quantity, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = quantity
        self.cost=cost

class User(db.Model,UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    birth_date = db.Column(db.DATE)
    phone = db.Column(db.String)
    bid = db.Column(db.String)
    bonus_points = db.Column(db.Integer)
    gender = db.Column(db.String)
    address = db.Column(db.String)
    admin = db.relationship("Admin",backref="users")


    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)

class Bid(db.Model):
    __tablename__ = "bids"

    id = db.Column(db.Integer, primary_key=True)
    name=  db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String)
    country = db.Column(db.String)
    city = db.Column(db.String)
    quantity = db.Column(db.Float)
    status = db.Column(db.String)
    payment_type = db.Column(db.String)
    date_created = db.Column(db.DateTime(timezone=True),server_default=func.now())
    product_id = db.Column(db.Integer,db.ForeignKey("products.id"))

    def __init__(self, name, surname, email, phone, address, country, city, quantity, product_id, payment_type):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.address = address
        self.country = country
        self.city = city
        self.quantity = quantity
        self.payment_type = payment_type
        self.product = Product.query.get(product_id)
        self.status = "pending"


class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User",backref="admins")

    def __init__(self, user_id):
        self.user_id = user_id

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    products = db.relationship("Product",backref="category",lazy="dynamic")

    def __init__(self,name):
        self.name = name
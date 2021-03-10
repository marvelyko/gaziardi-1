from flask import Blueprint,render_template,redirect,url_for,session
from myproject.models import Product,Category
from flask_login import logout_user,login_required

index_blueprint = Blueprint("index",__name__,template_folder="templates/index")

@index_blueprint.route("")
def index():
    product_list = Product.query.all()
    health_products = []
    hygiene_products = []
    grocery_products = []

    category = Category.query.filter_by(name="health").first()
    if category:
        health_products = category.products.all()
    
    category = Category.query.filter_by(name="hygine").first()
    if category:
        hygiene_products = category.products.all()
    
    category = Category.query.filter_by(name="grocery").first()
    if category:
        grocery_products = category.products.all()
    
    return render_template("index.html",product_list=product_list,health_products=health_products,hygiene_products=hygiene_products)

@index_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))
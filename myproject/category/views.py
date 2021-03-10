from flask import Blueprint, render_template
from myproject.models import Product, Category

category_blueprint = Blueprint("category",__name__,template_folder="templates/category")

def get_products_by_category(category):
    category = Category.query.filter_by(name=category).first()
    if category:
        products = category.products.all()
        return Product.query.all()
    else :
        return []

@category_blueprint.route("/health")
def health():
    products = get_products_by_category("health")
    sidebar_products = get_products_by_category("health")
    return render_template("product-list.html",product_list=products,sidebar_products=sidebar_products)

@category_blueprint.route("/beauty")
def beauty():
    products = get_products_by_category("beauty")
    sidebar_products = Product.query.all()
    return render_template("product-list.html",product_list=products,sidebar_products=sidebar_products)

@category_blueprint.route("/grocery")
def grocery():
    products = get_products_by_category("grocery")
    sidebar_products = Product.query.all()
    return render_template("product-list.html",product_list=products,sidebar_products=sidebar_products)

@category_blueprint.route("/hygiene")
def hygiene():
    products = get_products_by_category("hygiene")
    sidebar_products = Product.query.all()
    return render_template("product-list.html",product_list=products,sidebar_products=sidebar_products)

@category_blueprint.route("/charity")
def charity():
    products = get_products_by_category("charity")
    sidebar_products = Product.query.all()
    return render_template("product-list.html",product_list=products,sidebar_products=sidebar_products)
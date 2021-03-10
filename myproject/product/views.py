from flask import Blueprint,render_template,jsonify
from myproject.models import Product

product_blueprint = Blueprint("product",__name__,template_folder="templates/product")

@product_blueprint.route("/<int:id>")
def product(id):
    related_products = Product.query.all()
    product = Product.query.get(id)
    return render_template("product-detail.html",product=product,related_products=related_products)

@product_blueprint.route("/getInfo/<int:id>")
def getInfo(id):
    product = Product.query.get(id)
    print(jsonify(product.kwargs))
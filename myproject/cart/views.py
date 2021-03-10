import flask
from flask import Blueprint,render_template,session,url_for
import json
from myproject.models import Product

cart_blueprint = Blueprint("cart",__name__,template_folder="templates/cart")

@cart_blueprint.route("/",methods=["GET"])
def cart():
    return render_template("cart.html")

@cart_blueprint.route("/",methods=["POST"])
def cart_list():
    product_list = []
    arr = flask.request.data
    cart_id_list = [int(x) for x in list(arr.decode()) if x.isnumeric()]
    for id in cart_id_list:
        product = Product.query.get(id)
        
        if product:
            product_json = {
            "image": url_for('static',filename=f"uploads/{product.image}"),
            "name" : product.name,
            "price": product.price,
            "quantity" : product.quantity
            }
            product_list.append(product_json)
    return {"data":product_list}
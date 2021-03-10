from flask import Blueprint,render_template,request
from sqlalchemy import text

from myproject.models import  Product
from myproject import db

search_blueprint = Blueprint("search",__name__,template_folder="templates/search")

@search_blueprint.route("/")
def search():
    name = request.args.get("name")
    product_list = Product.query.filter(Product.name.like("%"+name+"%"))
    sidebar_products = Product.query.all()
    return render_template("product-list.html",product_list=product_list,sidebar_products=sidebar_products)
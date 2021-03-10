from flask import Blueprint, render_template, request, redirect, url_for
from myproject.models import Product, Bid
from myproject import db,send_mail_thread

checkout_blueprint = Blueprint("checkout",__name__,template_folder="templates/checkout")


@checkout_blueprint.route("",methods=["GET","POST"])
def checkout():
    product = None
    if request.method == "GET":
        product_id = request.args.get("id",type=int)
        quantity = request.args.get("qty",type=float)
        product = Product.query.get(product_id)
    elif request.method == "POST":
        product_id = request.args.get("id",type=int)
        product = Product.query.get(product_id)
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        country = request.form["country"]
        city = request.form["city"]
        quantity = request.form["quantity"]
        if request.form["payment"] == '3':
            payment = "transfer"
        else:
            payment = "unknown"

        if name and surname and email and phone and address and country and city and quantity:
            bid = Bid(name, surname, email, phone, address, country, city, quantity, product_id, payment)
            product.sold_quantity = product.sold_quantity + float(quantity)
            db.session.add(bid)
            db.session.add(product)
            db.session.commit()
            send_mail_thread(bid)
            return redirect(url_for("checkout.status", id=bid.id))

    return render_template("checkout.html", product=product)


@checkout_blueprint.route("/status/<int:id>")
def status(id):
    bid = Bid.query.get(id)
    return render_template("status.html", bid=bid)

@checkout_blueprint.route("/status/check")
def status_check():
    return render_template("status_check.html")
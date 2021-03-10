from flask import Blueprint,render_template

contact_blueprint = Blueprint("contact",__name__,template_folder="templates/contact")

@contact_blueprint.route("/")
def index():
    return render_template("contact.html")
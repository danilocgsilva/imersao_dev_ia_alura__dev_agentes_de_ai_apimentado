from flask import Flask, Blueprint, render_template
from .template_models.Index import Index

app = Flask(__name__)
route = Blueprint('route', __name__)
app.register_blueprint(route)

@app.route("/")
def index():
    return render_template("index.html", view_model=Index())

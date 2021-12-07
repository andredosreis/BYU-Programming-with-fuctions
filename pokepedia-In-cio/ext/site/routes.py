from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

@bp.route("/")
def home():
    return render_template('index.html')
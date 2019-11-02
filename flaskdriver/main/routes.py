from flask import Blueprint, render_template, url_for
from jService.api_handler import jService

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    jservice = jService()
    url = jservice.build_search_url("random", count=5)
    results = jservice.get_results(url)
    return render_template("home.html", title="Home", results=results)

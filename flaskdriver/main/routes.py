from flask import Blueprint, render_template, url_for, redirect
from flaskdriver.forms import SelectCategoriesForm
from jService.api_handler import jService

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def home():
    jservice = jService()
    jservice.build_search_url("categories", count=100)
    results = jservice.get_results()

    title = "Home"
    form = SelectCategoriesForm()
    form.select.choices = [(result['id'], result['title']) for result in results]

    if form.validate_on_submit():
        chosen_category = form.select.data
        print("DEBUG", chosen_category)
        return redirect(url_for("main.category", category_id=chosen_category))

    return render_template("home.html", title=title, form=form, results=results)

@main.route("/category/<category_id>")
def category(category_id):
    jservice = jService()
    jservice.build_search_url("clues", category=category_id)
    results = jservice.get_results()

    title = "?"

    return render_template("category.html", title=title, results=results)

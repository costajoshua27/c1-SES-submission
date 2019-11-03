from flask import Blueprint, render_template, url_for, redirect, request
from flaskdriver.forms import SelectCategoriesForm, RefineForm
from jService.api_handler import jService
from titlecase import titlecase

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def home():
    jservice = jService()
    jservice.build_search_url("categories", count=100)
    results = jservice.get_results()

    title = "Home"
    form = SelectCategoriesForm()
    form.select.choices = [(result['id'], titlecase(result['title'])) for result in results]

    if form.validate_on_submit():
        chosen_category = form.select.data
        return redirect(url_for("main.category", category_id=chosen_category))

    return render_template("home.html", title=title, form=form, results=results)


@main.route("/about")
def about():
    return "About"


@main.route("/category/<category_id>", methods=["GET", "POST"])
def category(category_id):
    jservice = jService()
    jservice.build_search_url("clues", category=category_id)
    results = jservice.get_results()


    category = titlecase(results[0]['category']['title'])
    title = category
    form = RefineForm()

    if request.method == "POST":
        if form.min_date.data and form.max_date.data:
            if form.value.data:
                return redirect(url_for("main.category_by_value_and_date", category_name=category, category_id=category_id, value=form.value.data, min_date=form.min_date.data, max_date=form.max_date.data))
            else:
                return redirect(url_for("main.category_by_date", category_name=category, category_id=category_id, min_date=form.min_date.data, max_date=form.max_date.data))
        else:
            if form.value.data:
                return redirect(url_for("main.category_by_value", category_name=category, category_id=category_id, value=form.value.data))


    return render_template("category.html", title=title, form=form, results=results, category=category)


@main.route("/category/<category_name>/<category_id>/<value>")
def category_by_value(category_name, category_id, value):
    jservice = jService()
    jservice.build_search_url("clues", category=category_id, value=value)
    results = jservice.get_results()
    return render_template("refined_category.html", results=results, category=category_name, category_id=category_id)


@main.route("/category/<category_name>/<category_id>/<min_date>/<max_date>")
def category_by_date(category_name, category_id, min_date, max_date):
    jservice = jService()
    jservice.build_search_url("clues", category=category_id, min_date=min_date, max_date=max_date)
    results = jservice.get_results()
    return render_template("refined_category.html", results=results, category=category_name, category_id=category_id)


@main.route("/category/<category_name>/<category_id>/<value>/<min_date>/<max_date>")
def category_by_value_and_date(category_name, category_id, value, min_date, max_date):
    jservice = jService()
    jservice.build_search_url("clues", category=category_id, value=value, min_date=min_date, max_date=max_date)
    results = jservice.get_results()
    return render_template("refined_category.html", results=results, category=category_name, category_id=category_id)
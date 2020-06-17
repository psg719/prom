from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from forms import MyForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/home", methods =["POST","GET"])
def home():
    form = MyForm()

    if form.validate_on_submit():
        date = form.date.data
        city = form.city.data

    return render_template("login.html",title='Prometric check',form=form)


if __name__ == "__main__":
    app.run(debug=True)

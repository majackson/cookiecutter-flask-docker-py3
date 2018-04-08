from flask import render_template

from {{cookiecutter.repo_name}} import app


@app.route('/')
def search():
    return render_template("hello_world.jinja", hello_world="Hello, world!")

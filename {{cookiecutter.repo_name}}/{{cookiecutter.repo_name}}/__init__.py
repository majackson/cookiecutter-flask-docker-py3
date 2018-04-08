import os

from distutils.util import strtobool

from flask import Flask


app = Flask(__name__)


PRODUCTION = bool(strtobool(os.environ.get('PRODUCTION', 'False')))

if PRODUCTION is False:
    app.config.from_object('{{cookiecutter.repo_name}}.settings.Config')
else:
    app.config.from_object('{{cookiecutter.repo_name}}.settings.ProductionConfig')


from {{cookiecutter.repo_name}} import settings, models, views  # NOQA

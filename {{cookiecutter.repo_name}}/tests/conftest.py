import pytest

from {{cookiecutter.repo_name}} import app as application


@pytest.fixture()
def app():
    application.config.from_object('{{cookiecutter.repo_name}}.settings.TestConfig')
    return application

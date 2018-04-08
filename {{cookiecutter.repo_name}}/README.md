# {{cookiecutter.project_name}}

## Overview

The {{cookiecutter.project_name}} project is a python3/flask/docker project.

## Developer Setup

The project is fully dockerised. There are a few ways to set this up on a Mac, but I'd recommend using `docker-machine`. You'll also need homebrew, VirtualBox, docker and docker-compose. With those installed, one-time setup is just `make bootstrap`.

## Tests

Run tests with `make test`.

## Development Server

To run a development server, use `make run`. The server will be up on your docker VM (get this with `docker-machine ip default`), port 80.

## Changing Development Environment

If any of the libraries in `requirements.txt` or `dev_requirements.txt` are changed, `make bootstrap` will have to be rerun before they are reflected in runs of `make test` or `make run`.

## Deployment

Deployment to AWS lambda is very straightforward with [Zappa](https://github.com/Miserlou/Zappa). First, copy your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` values to `production.env` (this file is excluded from git), then run `make zappa ZAPPA_CMD="deploy production"`. To run subsequent deployments, use `make zappa ZAPPA_CMD="update production"`. Zappa is a great tool, to learn more about it, head over to the repo and look through it's extensive readme.

To deploy static files, login to your AWS console, and create the S3 bucket corresponding to the name specified in `{{cookiecutter.repo_name}}/settings.py` (`{{cookiecutter.repo_name}}-static` by default). Then simply run `make staticfiles`.

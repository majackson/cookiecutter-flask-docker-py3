dev-build:
	docker-compose run --name {{cookiecutter.repo_name}}_app_cleanup --rm app bash -c "rm -rf ~/.venvs/{{cookiecutter.repo_name}}venv" && \
	docker-compose build

update-time:
	docker-machine ssh default "sudo ntpclient -s -h pool.ntp.org"

bootstrap:
	touch production.env && \
	make dev-build

run:
	echo "Server will be coming up at http://`docker-machine ip`/" && \
	docker-compose up

staticfiles:
	PRODUCTION=TRUE docker-compose run --name {{cookiecutter.repo_name}}_app_shell --rm app bash -c 'source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && python3 -c "import {{cookiecutter.repo_name}}, flask_s3; flask_s3.create_all({{cookiecutter.repo_name}}.app)"'

shell:
	docker-compose run --name {{cookiecutter.repo_name}}_app_shell --rm app bash -c 'source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && python3 -ic "import {{cookiecutter.repo_name}}"'

test:
	docker-compose run --name {{cookiecutter.repo_name}}_app_tests --rm app bash -c 'source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && py.test --strict $${TEST_ARGS:-"tests/"}'

zappa:
	make update-time && \
	docker-compose run --name {{cookiecutter.repo_name}}_app_zappa --rm app bash -c 'source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && zappa ${ZAPPA_CMD}'

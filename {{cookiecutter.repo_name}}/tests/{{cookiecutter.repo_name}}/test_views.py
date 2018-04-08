from {{cookiecutter.repo_name}} import views


def test_hello_world(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Hello, world!' in resp.data

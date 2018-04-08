class Config(object):
    PRODUCTION = False
    DEBUG = True
    STATIC_PREFIX = '/static/'


class ProductionConfig(Config):
    PRODUCTION = True
    DEBUG = False
    FLASKS3_BUCKET_NAME = '{{cookiecutter.repo_name}}-static'
    STATIC_PREFIX = 'https://{}.s3.amazonaws.com/static/'.format(FLASKS3_BUCKET_NAME)


class TestConfig(Config):
    TESTING = True

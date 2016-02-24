try:
    # only works in debug mode
    from flask_debugtoolbar import DebugToolbarExtension

    toolbar = DebugToolbarExtension()
except ImportError:
    print('debugtoolbar extension not available.')


{%- if cookiecutter.use_sql == 'yes' %}
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

{% endif %}


{%- if cookiecutter.use_nosql == 'yes' %}
from flask.ext.mongoengine import MongoEngine
nosql = MongoEngine()

{% endif %}

{%- if cookiecutter.use_restless == 'yes' %}
try:
    from flask.ext.restless import APIManager

    apimanager = APIManager(flask_sqlalchemy_db=db)
except ImportError:
    print ('restless extension not available.')
{% endif %}

{%- if cookiecutter.use_restless == 'yes' %}
try:
    from flask.ext.admin import Admin

    admin = Admin(template_mode='bootstrap3')
except ImportError:
    print ('admin extension not available.')
{% endif %}

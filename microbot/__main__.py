import os
from waitress import serve
from flask import Flask, Blueprint
from microbot.restplus import api
from microbot.views.root import ns_root
from microbot.views.category import ns_category

app_flask = Flask(__name__)


def initialize_app(app):
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['ERROR_404_HELP'] = False

    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    app.register_blueprint(blueprint)
    api.add_namespace(ns_root)
    api.add_namespace(ns_category)


def main():
    initialize_app(app_flask)
    port = int(os.environ.get("PORT", 5000))
    serve(app_flask, host='0.0.0.0', port=port,
          threads=int(os.getenv("APP_THREADS", "1")))


if __name__ == '__main__':
    main()

from microbot.restplus import api
from flask_restplus import Resource

import microbot.controllers.category as controllers
ns_category = api.namespace('category', description='Endpoints of categories')


@ns_category.route('/')
class HealthCheck(Resource):

    def get(self):
        """
        list categories
        """
        return {'status': 'Ok'}, 200

    @api.expect(controllers.category_create_model)
    def post(self):
        """
        Create new category
        """
        print(api.payload)
        return {'status': 'Categoria cadastrada com sucesso.'}, 201

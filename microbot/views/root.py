from microbot.restplus import api
from flask_restplus import Resource
ns_root = api.namespace('/', description='Endpoints root')


@ns_root.route('/healthz')
class HealthCheck(Resource):

    def get_healthCheck(self):
        """
        Chamada para verificar status da aplicacao
        """
        return {'status': 'Ok'}, 200

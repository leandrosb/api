from microbot.restplus import api
from flask_restplus import fields

category_read_model = api.model('Categories', {
    'id': fields.Integer(readonly=True, description='The category unique id'),
    'name': fields.String(required=True, description='The category name'),
    'status': fields.String(default='Desabilitado'),
})

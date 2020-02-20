from microbot.restplus import api
from flask_restplus import fields

category_read_model = api.model('Categories', {
    'id': fields.Integer,
    'name': fields.String,
    'status': fields.String(default='Desabilitado'),
}, mask='{name}')

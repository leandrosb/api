from microbot.restplus import api
from flask_restplus import Resource
from microbot.models.category import Category
import microbot.controllers.category as controllers

ns_category = api.namespace('category', description='Endpoints of categories')
category = Category()
model_category = controllers.category_read_model


@ns_category.route('/')
class CategoryManager(Resource):

    @ns_category.doc('List_Categories')
    @ns_category.marshal_with(model_category)
    def get(self):
        """
        list categories
        """
        return category.list_categories

    @ns_category.doc('create_Categories')
    @ns_category.expect(model_category)
    @ns_category.marshal_with(model_category, code=201)
    def post(self):
        """
        Create new category
        """
        return category.create(api.payload), 201


@ns_category.route('/<int:id>')
@ns_category.response(404, 'category not found')
@ns_category.param('id', 'Category identifier')
class CategoryField(Resource):
    """ Show a single category and delete """
    @ns_category.doc('get_category')
    @ns_category.marshal_with(model_category)
    def get(self, id):
        """
        return one category
        """
        return category.get(id)

from microbot.restplus import api
from flask_restplus import Resource
from microbot.models.category import Category
import microbot.controllers.category as controllers

ns_category = api.namespace('category', description='Endpoints of categories')
category = Category()
model_category = controllers.category_read_model


@ns_category.route('/')
class CategoryList(Resource):
    '''Shows a list of all categories, and lets you POST to add new category'''
    @ns_category.doc('List_Categories')
    @ns_category.marshal_with(model_category)
    def get(self):
        """
        list categories
        """
        return category.list_categories()

    @ns_category.doc('create_Categories')
    @ns_category.expect(model_category)
    @ns_category.marshal_with(model_category, 201)
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
    def get(self, iid):
        """
        return one category
        """
        return category.get(iid)

    @ns_category.doc('delete_category')
    @ns_category.response(204, 'Category deleted')
    def delete(self, iid):
        """
        Delete category
        """
        category.delete(iid)
        return '', 204

    @ns_category.expect(model_category)
    @ns_category.marshal_with(model_category)
    def put(self, iid):
        """
        Update category
        """
        return category.update(iid, api.payload)

from microbot.restplus import api
from flask_restplus import Resource
from microbot.models.category import Category
import microbot.controllers.category as controllers

ns_category = api.namespace('category', description='Endpoints of categories')
category = Category()


@ns_category.route('/')
class CategoryManager(Resource):

    @staticmethod
    def get(self):
        """
        list categories
        """
        list_categories = category.list_categories
        return list_categories, 200

    @api.expect(controllers.category_create_model)
    @staticmethod
    def post(self):
        """
        Create new category
        """
        result = category.create_category(api.payload)
        return result, 201

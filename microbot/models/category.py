from microbot.restplus import api


class Category:

    def __init__(self):
        self._categories = []
        self._id = len(self._categories)

    def get_category(self, iid):
        for todo in self._categories:
            if todo['id'] == iid:
                return todo
            api.abort(404, "Category {} doesn't exist ".format(id))

    def list_categories(self):
        return self._categories

    def create_category(self, data) -> list:
        todo = data
        todo['id'] = self._id = self._id + 1
        self._categories.append(todo)
        return todo

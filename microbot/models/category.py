from microbot.restplus import api


class Category:

    def __init__(self):
        self._categories = []
        self._id = len(self._categories)

    def get(self, id):
        for todo in self._categories:
            if todo['id'] == id:
                return todo
            api.abort(404, "Category {} doesn't exist ".format(id))

    def create_category(self, data) -> list:
        todo = data
        todo['id'] = self._id = self._id + 1
        self._categories.append(todo)
        return todo
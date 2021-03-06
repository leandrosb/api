from microbot.restplus import api


class Category:
    """Class Category """

    def __init__(self):
        self._categories = []
        self._id = 0

    def get(self, iid: int):
        """ Method get """
        for item in self._categories:
            if item['id'] == iid:
                return item
        api.abort(404, "Category {} doesn't exist ".format(iid))

    def list_categories(self):
        """ Method List categories """
        return self._categories

    def create(self, data: list):
        """ Method create categories """
        data['id'] = self._id = self._id + 1
        print(data)
        self._categories.append(data)

    def delete(self, iid: int):
        """ Method Delete categories """
        item = self.get(iid)
        self._categories.remove(item)

    def update(self, iid: int, data: list):
        """ Method update category """
        item = self.get(iid)
        item.update(data)
        return item

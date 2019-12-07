
class Category(object):
    def __init__(self, id: int, name: str, status: str):
        self._id = id
        self._name = name
        self._status = status

    def _create_category(self, name: str):
        self._name = name

class Counter(object):

    def __init__(self, items=0):
        self.items = items

    def add(self):
        self.items += 1

    def remove(self):
        self.items -= 1

    def total(self):
        return self.items


def test_total_default():
    total_default = Counter()
    assert total_default.total() == 0


def test_add_two():
    total_default = Counter()
    total_default.add()
    total_default.add()
    assert total_default.total() == 2


def test_remove_one():
    total_default = Counter(1)
    total_default.remove()
    assert total_default.total() == 0


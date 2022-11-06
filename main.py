class FlatIterator:

    def __init__(self, list_of_lists):
        self.list = list_of_lists

    def __iter__(self):
        self.list_iter = iter(self.list)
        self.list_of_lists_1 = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.list_of_lists_1) == self.cursor:
            self.list_of_lists_1 = None
            self.cursor = 0
            while not self.list_of_lists_1:
                self.list_of_lists_1 = next(self.list_iter)
        return self.list_of_lists_1[self.cursor]


def flat_generator(my_list):
    for sub_list in my_list:
        for elem in sub_list:
            yield elem


def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test()
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = iter(list_of_list)
        self.inner_list = None

    def _pop_list(self):
        try:
            self.inner_list = iter(next(self.list_of_list))
        except StopIteration:
            self.inner_list = None

    def __iter__(self):
        self._pop_list()
        return self

    def __next__(self):
        if self.inner_list is None:
            raise StopIteration
        try:
            return next(self.inner_list)
        except StopIteration:
            self._pop_list()
            return self.__next__()

 def test_1():

     list_of_lists_1 = [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
     ]

     for flat_iterator_item, check_item in zip(
             FlatIterator(list_of_lists_1),
             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
     ):

         assert flat_iterator_item == check_item

     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
     test_1()

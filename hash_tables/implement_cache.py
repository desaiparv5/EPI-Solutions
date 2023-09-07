from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self._isbn_table = OrderedDict()
    
    def insert(self, isbn_number, price):
        if len(self._isbn_table) == self.capacity:
            self._isbn_table.popitem(last=False)
        self._isbn_table[isbn_number] = price

    def lookup(self, isbn_number):
        if isbn_number not in self._isbn_table:
            return -1
        price = self._isbn_table.pop(isbn_number)
        self.insert(isbn_number, price)
        return price


def main():
    lru_cache = LRUCache(3)
    pass


if __name__ == "__main__":
    main()

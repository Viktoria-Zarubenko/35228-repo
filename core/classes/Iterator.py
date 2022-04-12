from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class PlansOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: PlansCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class PlansCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> PlansOrderIterator:
        return PlansOrderIterator(self._collection)

    def get_reverse_iterator(self) -> PlansOrderIterator:
        return PlansOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


def sort_plans(plans: list):
    collection = PlansCollection()
    for plan in plans:
        collection.add_item(plan)

    return list(collection.get_reverse_iterator())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        """Create an empty list with items of type T"""
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]

    def length(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return not self.items

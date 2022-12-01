"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.link=None

    def push(self, x: T) -> None:#works
        """Push x on the top of this stack."""
        self.link=Link(x,self.link)

    def top(self) -> T: #works
        """Return the top of the stack."""
        if self.link:#WTF it does both the if and the else, if you have an empty list what the hell
            return self.link.head
        else:
            print("lol, empty stack")

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        if self:
            self.link.head=self.link.tail.head
        else:
            print("you have an empty stack, too bad!!")
        return self.link.head

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        if self.link is None:
            return True
        return False

list=Stack()
list.push(1)
list.push(33)
list.push(458)
list.push(8888)
list.pop()
list.pop() #lol the second pop is not workning...
print(list.top())
print(list.is_empty())

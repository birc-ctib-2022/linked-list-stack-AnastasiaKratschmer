[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9506533&assignment_repo_type=AssignmentRepo)
# Linked list stack

You can easily build a stack from singly-linked lists. Recall that a link can be defined this way:

```python
@dataclass
class Link(Generic[T]):
    head: T
    tail: List[T]

# A List is either None or a Link[T]
List = Optional[Link[T]]
```

**Exercise:** Implement a stack by filling in the blanks in the code below (and in `src/stack.py`):

```python
class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.link=None

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        self.link=Link(x,self.link)

    def top(self) -> T:
        """Return the top of the stack."""
        if self:
        return self.link.head
        else:
            print("you have nothing on your stack, that's a shame!!")

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        if self:
        pop (self.link.head)
        else:
            print("you have an empty stack, too bad!!")

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        if self.link.head is None:
            return True
```

list=Link(2,Link(1,Link(2)))

list.__init__()

I have not written tests for you, so you have to write those yourself if you want minimal certainty that your implementation is correct.

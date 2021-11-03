from stack import Stack


def test_exists():
    s = Stack()
    assert s is not None


def test_push():
    s = Stack()
    s.push(1)
    assert s.data == [1]


def test_pop():
    s = Stack()
    s.push(1)
    assert s.pop() == 1
    assert s.data == []


def test_buitins():
    s = Stack()
    assert s.is_empty()
    assert len(s) == 0


def test_push_sequence():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert not s.is_empty()
    assert s.data == [1, 2, 3]

    
def test_push_pop_sequence():
    s = Stack()
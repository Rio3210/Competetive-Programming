class Foo:
    def __init__(self):
        self.seq = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.seq=1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.seq<1:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.seq=2


    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.seq<2:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
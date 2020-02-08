from threading import Semaphore, Barrier, Event
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_event= Event()
        self.bar_event = Event()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if i > 0:
                self.foo_event.wait()
            self.foo_event.clear()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_event.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_event.wait()
            self.bar_event.clear()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_event.set()


def main():
    import sys
    import io
    while True:
        try:
            count=2
            ret = FooBar(count)
            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
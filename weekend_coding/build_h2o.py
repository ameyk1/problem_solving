from threading import Semaphore, Barrier
# Semaphores used as counter and Barrier to wait
# Added release and wait only
# 48 ms
class H2O:
    def __init__(self):
        self.h_count = Semaphore(2)
        self.o_count = Semaphore(1)
        self.h2o_barrier = Barrier(3)
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        with self.h_count:
            self.h2o_barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.h_count:
            self.h2o_barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class clock:

    def __init__(self, fmt=DEFAULT_FMT) -> None:
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter()
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result
        return clocked
    

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    @clock('{name}: {elapsed}')
    def snooze2(seconds):
        time.sleep(seconds)

    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze3(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
        snooze2(.123)
        snooze3(.123)
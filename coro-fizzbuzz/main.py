

def producer_consumer_coro(func):
    def outer_wrapper(*args, **kwargs):
        def wrapper(*args, **kwargs):
            value = yield
            while True:
                value = yield func(value, *args, **kwargs)
        result = wrapper(*args, **kwargs)
        next(result)
        return result
    return outer_wrapper


@producer_consumer_coro
def fizzer(value, next_coro):
    if isinstance(value, int) and value % 3 == 0:
        return next_coro.send("FIZZ")
    return next_coro.send(value)


@producer_consumer_coro
def buzzer(value, next_coro):
    if isinstance(value, int) and value % 5 == 0:
        return next_coro.send("BUZZ")
    return next_coro.send(value)


@producer_consumer_coro
def fizzbuzzer(value, next_coro):
    if isinstance(value, int) and value % 5 == 0 and value % 3 == 0:
        return next_coro.send("FIZZBUZZ")
    return next_coro.send(value)


@producer_consumer_coro
def end_of_the_line(value):
    return value


def producer(stop, transformer):
    for i in range(1, stop + 1):
        yield transformer.send(i)


def main():
    fizzbuzz = fizzbuzzer(buzzer(fizzer(end_of_the_line())))
    results = producer(100, fizzbuzz)
    print(list(results))


if __name__ == '__main__':
    main()

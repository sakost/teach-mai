import time


class timeit:
    __slots__ = ("start", "end", "name")

    def __init__(self, name: str | None = None):
        self.start = None
        self.end = None
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.log_to_stdout()


    def log_to_stdout(self):
        print(f"Proceed {'' if self.name is None else self.name} with {self.end - self.start} seconds")



def main():
    with timeit("database request"):
        # __enter__
        print("requesting database data...")
        time.sleep(3)
        # __exit__


if __name__ == '__main__':
    main()

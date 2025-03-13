import time


class FakeDBSession:
    def __init__(self, url: str):
        self.url = url

    def open(self):
        print("opening session...")
        time.sleep(1)

    def fetch(self):
        """
        Производит запрос из БД
        """
        print("fetching data...")
        time.sleep(3)
        return [0, 1, 2, 3]

    def close(self):
        print("closing session...")
        time.sleep(1)

    def commit(self):
        """
        Применяет изменения последней транзакции
        """
        print("committing...")
        time.sleep(1)

    def rollback(self):
        """
        Откатывает изменения последней транзакции
        """
        print("rolling back...")
        time.sleep(1)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):  # sys.exc_info
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        self.close()


def main():
    with FakeDBSession("db_url") as db:
        data = db.fetch()
        print("handling data...")
        for x in data[:-1]:
            print(x / data[-1])



if __name__ == '__main__':
    main()

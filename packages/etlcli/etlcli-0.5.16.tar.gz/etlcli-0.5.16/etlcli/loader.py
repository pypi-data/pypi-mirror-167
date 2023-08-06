import sqlite3
import csv


class Loader:
    def __init__(self, database) -> None:
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
    
    def load_data(self, input, target) -> None:
        with open(input, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                # skip header
                if i == 0:
                    continue
                query = self._prepare_query(target, len(line))
                self.conn.execute(query, line)
            self.conn.commit()

    def _prepare_query(self, target, length) -> str:
        query = f"INSERT or REPLACE into {target} VALUES ({','.join(['?'] * length)});"
        return query
    
    def close_conn(self) -> None:
        self.conn.close()

if __name__ == "__main__":
    loader = Loader("target.db")
    loader.load_data("transactions_2010-12-02.csv", "transactions")
    loader.close_conn()
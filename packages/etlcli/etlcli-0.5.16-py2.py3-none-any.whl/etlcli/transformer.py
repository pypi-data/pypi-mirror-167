import sqlite3


class Transformer:
    def __init__(self, database) -> None:
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
    

    def transform_data(self, query, params, target) -> None:
        with open(query) as queryfile:
            q = f"INSERT OR REPLACE INTO {target} {queryfile.read()}"
            self.cur.execute(q, params)
        self.conn.commit()
    
    def close_conn(self) -> None:
        self.conn.close()

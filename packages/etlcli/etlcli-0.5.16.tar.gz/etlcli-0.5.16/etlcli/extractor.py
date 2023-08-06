import sqlite3
import csv


class Extractor:
    def __init__(self, database) -> None:
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
    
    def execute_query(self, query, params) -> None:
        with open(query) as queryfile:
            self.result = self.cur.execute(queryfile.read(), params).fetchall()

    def save_to_csv(self, target) -> None:
        cols = [r[0] for r in self.cur.description]
        with open(target, "w") as out:
            csv_out = csv.writer(out)
            csv_out.writerow(cols)
            csv_out.writerows(self.result)
    
    def close_conn(self) -> None:
        self.conn.close()

if __name__ == "__main__":
    extractor = Extractor("source.db")
    extractor.execute_query("query.sql", {'date' : '2011-12-09'})
    extractor.save_to_csv("result.csv")
    extractor.close_conn()



"""
execute quert should return value instead of saving it to self.result

"""
    


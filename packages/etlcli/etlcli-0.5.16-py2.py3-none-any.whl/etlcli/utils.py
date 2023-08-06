import sqlite3


def create_table(database, query):
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    with open(query, "r") as f:
        sql_script = f.read()
    
    cur.executescript(sql_script)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table("target.db", "etlcli/load_query.sql")
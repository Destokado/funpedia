import sqlite3

duel_table = "CREATE TABLE IF NOT EXISTS duels (id INTEGER PRIMARY KEY, user_wiki INTEGER NOT NULL,user_name TEXT NOT NULL , user_id INTEGER, " \
             "rival_wiki INTEGER NOT NULL, rival_name TEXT NOT NULL, rival_id INTEGER," \
             " metric TEXT NOT NULL, namespaces TEXT NOT NULL, goal TEXT NOT NULL,theme TEXT, bet INTEGER ," \
             "start_date timestamp NOT NULL, end_date timestamp," \
             " user_counter TEXT NOT NULL, rival_counter TEXT NOT NULL, winner_name TEXT, winner_id INTEGER)"


def create_table_duels():
    conn = sqlite3.connect('../databases/funpedia.db')
    cursor = conn.cursor()
    cursor.execute(duel_table)
    conn.commit()
    conn.close()


def insert_into(table, columns, rows):
    conn = sqlite3.connect('../databases/funpedia.db')
    with conn:
        cursor = conn.cursor()
        query = "INSERT INTO {} (".format(table)

        for col in columns:
            query += ", {}".format(col)
        query += ") VALUES( " + ",".join("?" * len(columns)) + ");"

        cursor.executemany(query, rows)
        conn.commit()
        return cursor.rowcount


def select_duels(columns):
    conn = sqlite3.connect('../databases/funpedia.db')
    with conn:
        cursor = conn.cursor()

        query="SELECT "+",".join(col for col in columns) + "FROM duels;"

        return cursor.execute(query).fetchall()

if __name__ == "__main__":
    create_table_duels()

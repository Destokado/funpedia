import sqlite3


duel_table = "CREATE TABLE IF NOT EXISTS duels (id INTEGER PRIMARY KEY, challenger_name TEXT NOT NULL , challenger_id INTEGER, " \
             "rival_name TEXT NOT NULL, rival_id INTEGER, metric TEXT NOT NULL, goal TEXT NOT NULL,start_date timestamp NOT NULL, end_date timestamp," \
             " challenger_counter TEXT NOT NULL, rival_counter TEXT NOT NULL, winner_name TEXT, winner_id INTEGER)"

def create_table_duels():
    conn = sqlite3.connect('../databases/funpedia.db')
    cursor = conn.cursor()
    cursor.execute(duel_table)
    conn.commit()

if __name__ == "__main__":
    create_table_duels()

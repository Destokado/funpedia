import sqlite3


duel_table = "CREATE TABLE IF NOT EXISTS duels (id INTEGER PRIMARY KEY, user_wiki INTEGER NOT NULL,user_name TEXT NOT NULL , user_id INTEGER, " \
             "rival_wiki INTEGER NOT NULL, rival_name TEXT NOT NULL, rival_id INTEGER, metric TEXT NOT NULL, namespaces TEXT NOT NULL, goal TEXT NOT NULL, bet INTEGER ,start_date timestamp NOT NULL, end_date timestamp," \
             " user_counter TEXT NOT NULL, rival_counter TEXT NOT NULL, winner_name TEXT, winner_id INTEGER)"

def create_table_duels():
    conn = sqlite3.connect('../databases/funpedia.db')
    cursor = conn.cursor()
    cursor.execute(duel_table)
    conn.commit()

if __name__ == "__main__":
    create_table_duels()

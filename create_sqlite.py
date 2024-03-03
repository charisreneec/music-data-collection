# %%
import sqlite3
import time

con = sqlite3.connect("musicbox.db")
cur = con.cursor()

# %%

cur.execute("CREATE TABLE IF NOT EXISTS games(id INTEGER PRIMARY KEY, date)")
cur.execute(
    "CREATE TABLE IF NOT EXISTS players(id INTEGER PRIMARY KEY, username, game, FOREIGN KEY(game) REFERENCES games(id))"
)
cur.execute(
    "CREATE TABLE IF NOT EXISTS answers(id INTEGER PRIMARY KEY, answer, round, score, player, video_id, FOREIGN KEY(player) REFERENCES players(id))"
)

# %%
cur.execute("SELECT * FROM sqlite_master").fetchall()

# %%
cur.close()
con.close()

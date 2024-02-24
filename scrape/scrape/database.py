import sqlite3

db_name = 'scrape.db'
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
execute = cursor.execute
commit = connection.commit

execute("""
    CREATE TABLE IF NOT EXISTS `scraped_data` (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        tag TEXT
    )
""")

commit()
connection.close()

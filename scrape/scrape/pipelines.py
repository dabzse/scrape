# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
from itemadapter import ItemAdapter


class ScrapePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('scrape.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `scraped_data` (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                tag TEXT
            )
        """)

    def process_item(self, item, spider):
        self.store(item)
        return item

    def store(self, item):
        self.cursor.execute("""INSERT INTO scraped_data (title, author, tag) VALUES(?, ?, ?)""", (
            item['title'][0],
            item['author'][0],
            str(item['tag'])
        ))
        self.connection.commit()
from itemadapter import ItemAdapter
import web_scraper.db as db


class WebScraperPipeline:
    def process_item(self, item, spider):
        connection = db.DB_postgresql(host="lucky.db.elephantsql.com",
                                      database="yltbrpcq",
                                      user="yltbrpcq",
                                      password="en0RkZIR-6Re9-LE2ZzIVK-RzHYOQJbI")
        connection.connect_to_db()
        connection.insert_element('webs', [item['title'], item['img_url']])
        connection.conn.commit()
        return item

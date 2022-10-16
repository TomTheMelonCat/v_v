import os
from web_scraper.web_scraper.db import DB_postgresql
from airium import Airium
from urllib import unquote


def save_html(html):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local_server', 'items_display.html'), 'w', encoding='utf-8') as w:
        w.write(html)

def get_html():
    a = Airium()
    db_obj = DB_postgresql(host="lucky.db.elephantsql.com",
                           database="yltbrpcq",
                           user="yltbrpcq",
                           password="en0RkZIR-6Re9-LE2ZzIVK-RzHYOQJbI")
    data = db_obj.select_table('webs')
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Data from webscraping")

        with a.body():
            a.meta(charset="utf-8")
            for idx, item in enumerate(data):
                title = str(item[1])[2:-2].encode('utf-8')
                url = str(item[2]).encode('utf-8')
                with a.h4(id=f'Pair_{idx}', klass='main_header'):
                    a(f'{title} : {url}')

    html = str(a)

    return html


if __name__ == '__main__':
    html = get_html()
    save_html(html)

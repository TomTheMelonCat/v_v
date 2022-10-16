import urllib.parse as up
import psycopg2
from psycopg2.extras import execute_values


class DB_postgresql():

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connect_to_db()

    def connect_to_db(self):
        up.uses_netloc.append("postgres")
        conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)

        self.conn = conn
        self.cursor = conn.cursor()

    def select_table(self, tablename):
        self.cursor.execute(f'SELECT * FROM {tablename}')
        return self.cursor.fetchall()

    def insert_element(self, tablename, element):
        try:
            image_url, title = element[0], element[1]
        except:
            print("Wrong format.")
            return 0

        rows = self.select_table(tablename)
        if rows == None:
            p_id = 1
        else:
            p_id = len(rows)+1
        self.cursor.execute(f'''
                    INSERT INTO {tablename} (website_ID, image_url, title) 
                    VALUES (%s, %s, %s);
                    ''',
                            (p_id, image_url, title)
                            )

    # Unused method, serves just as a demonstration of my awareness that there indeed are faster methods of inserting multiple rows at once 
    # - either the method below or COPY in postgre itself. This is done just to make everything quicker (and as a proof of concept, its enough).
    def insert_many(self, tablename, elements):
        data = ",".join(map(str, elements))
        query = f"INSERT INTO {tablename} (website_ID, image_url, title) VALUES {0}".format(
            data)
        self.cursor.execute(query)

    def truncate_table(self, table):
        self.cursor.execute(f'''
                    TRUNCATE {table};
        ''')


if __name__ == '__main__':
    db_conn = DB_postgresql(host="lucky.db.elephantsql.com",
                            database="yltbrpcq",
                            user="yltbrpcq",
                            password="en0RkZIR-6Re9-LE2ZzIVK-RzHYOQJbI")

    # db_conn.insert_element('webs', ['test_url', 'test_title'])
    # db_conn.truncate_table('webs')
    # webs = db_conn.select_table('webs')
    db_conn.conn.commit()
    print('Huh.')

import pymysql
from config import HOST, PORT, PASSWORD


def connect_to_db():
    connection = None
    try:
        connection = pymysql.connect(
            host=HOST,
            port=PORT,
            user='root',
            password=PASSWORD,
            database='testovoe',
            cursorclass=pymysql.cursors.DictCursor)
        print("successfully connected")
        print("_" * 22)
    except Exception as error:
        print(f'Error! - {error}')
    return connection


def drop_table(connection):
    try:
        with connection.cursor() as cursor:
            drop_table_query = "DROP TABLE `news`;"
            cursor.execute(drop_table_query)
            print('successfully dropped table')
    except Exception as e:
        print(f'DB not created - {e}')
    finally:
        connection.close()


def create_db(connection):
    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `news`(id int AUTO_INCREMENT," \
                                 " title text," \
                                 " source varchar(32)," \
                                 " tags text," \
                                 " dat_new date," \
                                 " content text, PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            connection.commit()
        print("Table created successfully")
    except Exception as er:
        print(er)


def add_to_db(title, source, tags, text, dat, connection):
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `news` (title, source, tags, dat_new, content) VALUES (%s, %s, %s, %s, %s);"
            data = (title, source, tags, dat, text)
            cursor.execute(insert_query, data)
            connection.commit()
    except Exception as er:
        print(er)


def close_connection(connection):
    connection.close()
    print("connection closed")
    print("_" * 22)


def get_all(connection):
    try:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `news`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("_" * 20)
    except Exception as er:
        print('error!')


def get_vr(connection):
    try:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `news` WHERE dat_new BETWEEN '2022-08-19' AND '2022-08-24'"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("_" * 20)
    except Exception as er:
        print('error!')

#s = connect_to_db()
#drop_table(s)
# get_vr(s)
#create_db(s)
# get_all(s)
#close_connection(s)

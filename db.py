import pymysql
from data.config import HOST, PORT, PASSWORD, DATABASE


def connect_to_db():
    connection = None
    try:
        connection = pymysql.connect(
            host=HOST,
            port=PORT,
            user='root',
            password=PASSWORD,
            database=DATABASE,
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
    #finally:
        #connection.close()


def create_db(connection):
    try:
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `news`(id int AUTO_INCREMENT," \
                                 " title text," \
                                 " source varchar(32)," \
                                 " tags text," \
                                 " content text, PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            connection.commit()
        print("Table created successfully")
    except Exception as er:
        print(er)


def add_to_db(title, source, tags, text, connection):
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `news` (title, source, tags, content) VALUES (%s, %s, %s, %s);"
            data = (title, source, tags, text)
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


#s = connect_to_db()
#drop_table(s)
#create_db(s)
# get_all(s)
#close_connection(s)

# create_db()
#
#     try:
#         connection = pymysql.connect(
#             host=HOST,
#             port=PORT,
#             user='root',
#             password=PASSWORD,
#             database=DATABASE,
#             cursorclass=pymysql.cursors.DictCursor)
#         print("successfully connected")
#         print("_" * 22)
#         cursor = connection.cursor()
#         with connection.cursor() as cursor:
#             create_table_query = "CREATE TABLE `news`(id int AUTO_INCREMENT," \
#                                  " title text," \
#                                  " tags varchar(32)," \
#                                  " source varchar(32)," \
#                                  " content text, PRIMARY KEY (id));"
#             cursor.execute(create_table_query)
#         print("Table created successfully")
#     except Exception as error:
#         print(f'Error! - {error}')
#
#

#
#

# update data
# with connection.cursor() as cursor:
#     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
#     cursor.execute(update_query)
#     connection.commit()

# delete data
# with connection.cursor() as cursor:
#     delete_query = "DELETE FROM `users` WHERE id = 5;"
#     cursor.execute(delete_query)
#     connection.commit()


#
#     finally:
#         connection.close()
#
# except Exception as ex:
#     print("Connection refused...")
#     print(ex)

import pymysql

import config
from config import HOST, PORT, USER, PASSWORD, DATABASE


def connect_to_db():
    try:
        connection = pymysql.connect(
            host=HOST,
            port=PORT,
            user='root',
            password=PASSWORD,
            database=DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        try:
            print('2 try')

            cursor = connection.cursor()
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `news`(id int AUTO_INCREMENT," \
                                     " title varchar(32)," \
                                     " tags varchar(32)," \
                                     " source varchar(32)," \
                                     " content text, PRIMARY KEY (id));"
                cursor.execute(create_table_query)
                print("Table created successfully")
        except Exception as e:
            print('2')
            print(e)
    except Exception as e:
        print('1', e)


connect_to_db()


def add_to_db(title, tags, source, text, ):
    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `mysql` (title, tags, source, text) VALUES ({title}, {tags}, {source}, {text});"
        cursor.execute(insert_query)
        connection.commit()

    # with connection.cursor() as cursor:
    #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
    #     cursor.execute(insert_query)
    #     connection.commit()
    #
    # with connection.cursor() as cursor:
    #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
    #     cursor.execute(insert_query)
    #     connection.commit()

    # with connection.cursor() as cursor:
    #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
    #     cursor.execute(insert_query)
    #     connection.commit()
    #
    # with connection.cursor() as cursor:
    #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
    #     cursor.execute(insert_query)
    #     connection.commit()

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

    # drop table
    # with connection.cursor() as cursor:
    #     drop_table_query = "DROP TABLE `users`;"
    #     cursor.execute(drop_table_query)

    # select all data from table
#         with connection.cursor() as cursor:
#             select_all_rows = "SELECT * FROM `users`"
#             cursor.execute(select_all_rows)
#             # cursor.execute("SELECT * FROM `users`")
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#             print("#" * 20)
#
#     finally:
#         connection.close()
#
# except Exception as ex:
#     print("Connection refused...")
#     print(ex)

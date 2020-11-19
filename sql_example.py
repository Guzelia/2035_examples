import sqlite3
import pandas as pd


def create_table(cur):
    # Задание запроса на создание таблицы
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user (
        id integer PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """

    # Выполнение запроса
    cur.execute(create_table_query)


def insert_data(cur):
    # Выполнение запросов на заполнение таблицы данными
    cur.execute("INSERT INTO user VALUES(1, 'Ivan', 'Ivanov', 'ivanivanov@example.com')")
    cur.execute("INSERT INTO user VALUES(2, 'Petr', 'Petrov', 'petrpetrov@example.com')")
    cur.execute("INSERT INTO user VALUES(3, 'Vasiliy', 'Vasiliev', 'vasiliyvasiliev@example.com')")


def save_data(conn):
    # Задание запроса выборки данных
    select_query = "SELECT * from user"

    # Создание датафрейма из запроса
    df = pd.read_sql(select_query, conn)

    # Сохранение результата в csv
    df.to_csv('users_sql.csv', index=False)


def main():
    # Задание имени базы данных
    database = 'database.db'
    # Задание соединения
    conn = sqlite3.connect(database)
    # Создание курсора
    cur = conn.cursor()

    # Создание таблицы
    create_table(cur)

    # Заполнение таблицы
    insert_data(cur)

    # Экспорт данных в csv
    save_data(conn)

    # Закрытие соединения
    conn.close()

import mysql.connector


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(3307)
    )
    return connection


def get_users(my_query, connection):
    results = execute_query(my_query, connection)
    return results


def execute_query(my_query, connection):
    cursor = connection.cursor()
    cursor.execute(my_query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


if __name__ == '__main__':
    db = connection_database("localhost", "root", "root", "gri")
    all_users_query = "SELECT * FROM users"
    result = get_users(all_users_query, db)
    print(result)

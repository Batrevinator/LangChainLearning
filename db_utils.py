import psycopg2
import os
import dotenv

def main():
    dotenv.load_dotenv(".env")

def connect():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"), 
            user=os.getenv("USER"),
            password=os.getenv("PASS"), 
            database=os.getenv("DB_NAME"), 
            port=int(os.getenv("PORT"))
        )
    except psycopg2.Error as e:
        print("Database error:" + str(e))


"""
@brief This function will execute a sql file. This is useful for running migrations or seeding the database.

@param path - the path to the sql file. This is a relative path from the src/dbaccess directory.
@return None - if there is an error executing the sql file. This will print the error to the console.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.
"""

def exec_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    if(conn is not None):
        conn.close()

"""
@brief This function will execute a sql query and return the FIRST result. This is useful for checking if data exists in the DB or finding sorted data.

@param sql - the sql query to execute. This is a string.
@param args - the arguments to pass to the sql query. This is a tuple. Even if there is only one argument, it should be a tuple. For example, (1,).
@return one - the first result of the query. This is a tuple.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.
"""

def exec_get_one(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    if(conn is not None):
        conn.close()
    return one

"""
@brief This function will execute a sql query and return all the results. This is useful for getting data from the database.

@param sql - the sql query to execute. This is a string.
@param args - the arguments to pass to the sql query. This is a tuple. Even if there is only one argument, it should be a tuple. For example, (1,).
@return list_of_tuples - a list of tuples containing the results of the query. Each tuple is a row from the database.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.
"""

def exec_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall

    list_of_tuples = cur.fetchall()
    if(conn is not None):
        conn.close()
    return list_of_tuples

"""
@brief This function will execute many sql queries and return all the results. This is useful for getting data from the database.

@param sql - the sql query to execute. This is a string.
@param args - the arguments to pass to the sql query. This is a list of tuples. Even if there is only one argument, it should be a tuple. For example, [(1,), (2,)].
@return list_of_tuples - a list of tuples containing the results of the query. Each tuple is a row from the database.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.   
"""

def exec_get_many(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.executemany(sql, args)
    list_of_tuples = cur.fetchall()
    if(conn is not None):
        conn.close()
    return list_of_tuples

"""
 @brief This function will execute a sql query and commit the changes to the database. This is useful for inserting, updating, or deleting data from the database.


@param sql - the sql query to execute. This is a string.
@param args - the arguments to pass to the sql query. This is a tuple. Even if there is only one argument, it should be a tuple. For example, (1,).
@return result - the result of the query. This is a cursor object.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.
"""

def exec_commit(sql, args={}):
    try: 
        conn = connect()
        cur = conn.cursor()
        result = cur.execute(sql, args)
        conn.commit()
        if(conn is not None):
            conn.close()
        return result
    except Exception as e:
        raise ValueError(f"Error executing commit: {e}") from e
    
"""
@brief This function will execute a sql query and commit the changes to the database. This is useful for inserting, updating, or deleting data from the database.

@param sql - the sql query to execute. This is a string.
@param args - the arguments to pass to the sql query. This is a tuple. Even if there is only one argument, it should be a tuple. For example, (1,).
@return result - the result of the query. This is a cursor object.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.
"""

def exec_commit_many(sql, args_list=[]):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.executemany(sql, args_list)
        conn.commit()
        if(conn is not None):
            conn.close()
    except Exception as e:
        raise ValueError(f"Error executing commit many: {e}") from e
    

"""
@brief This function will execute a sql query and return the first result. This is useful for checking if data exists in the DB or finding sorted data.


@param sql - the sql query to execute. This is a string.
@param args - the arguments to pass to the sql query. This is a tuple. Even if there is only one argument, it should be a tuple. For example, (1,).
@return postgresql_returning - the first result of the query. This is a tuple.
@note: This function will load the environment variables from the .env file. This is a requirement for the rest of the utils to work.
"""

def exec_commit_returning(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    postgresql_returning = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return postgresql_returning


if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    main()
#!/usr/bin/env python3

import configparser
import os
import sys
import mysql.connector
from mysql.connector import Error

def main():
    # Check if code parameter is provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <migration-file> [database] [drop]")
        sys.exit(1)

    migration_file = sys.argv[1]
    database = sys.argv[2] if len(sys.argv) > 2 else None
    drop = sys.argv[3] if len(sys.argv) > 3 else None

    # Check if migration file exists
    if not os.path.isfile(migration_file):
        print(f"Error: Migration file '{migration_file}' does not exist")
        sys.exit(1)

    # Read configuration file
    config = configparser.ConfigParser()
    config.read('.config')

    # Get database parameters
    host = config.get('mysql', 'host', fallback='127.0.0.1')
    user = config.get('mysql', 'user', fallback='root')
    password = config.get('mysql', 'password', fallback='')

    connection = None
    try:
        # Connect without specifying a database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")

            cursor = connection.cursor()

            if database:
                # Check if database exists
                cursor.execute(f"SHOW DATABASES LIKE '{database}'")
                result = cursor.fetchone()

                create_sql = f"CREATE DATABASE `{database}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
                if result:
                    print(f"Database '{database}' exists")
                    if drop:
                        cursor.execute(f"DROP DATABASE `{database}`")
                        print(f"Database '{database}' dropped successfully")
                        cursor.execute(create_sql)
                        print(f"Database '{database}' created successfully")
                else:
                    print(f"Database '{database}' does not exist. Creating it...")
                    cursor.execute(create_sql)
                    print(f"Database '{database}' created successfully")

                # Use the database
                cursor.execute(f"USE `{database}`")
                print(f"Connected to database: {database}")

            # Migration logic
            try:
                with open(migration_file, 'r') as file:
                    sql = file.read()
                for statement in sql.split(";\n"):
                    if len(statement.strip()):
                        cursor.execute(statement)
                connection.commit()
                print(f"Migration executed successfully")
            except Error as e:
                print(f"Error executing migration: {e}")
                sys.exit(1)

            cursor.close()

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import mysql.connector
import sys
import os

if __name__ == "__main__":
    migration = sys.argv[1] if len(sys.argv) > 1 else "migration.sql"
    host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
    user = sys.argv[3] if len(sys.argv) > 3 else "root"
    passwd = sys.argv[4] if len(sys.argv) > 4 else ""
    database = sys.argv[5] if len(sys.argv) > 5 else ""

    if not os.path.isfile(migration):
        print(f"Migration file '{migration}' does not exist.")
        sys.exit(1)

    try:
        mydb = (
            mysql.connector.connect(host=host, user=user, passwd=passwd)
            if "" == database
            else mysql.connector.connect(
                host=host, user=user, passwd=passwd, database=database
            )
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

    try:
        with open(migration) as file:
            sql = file.read()
        mycursor = mydb.cursor()
        for statement in sql.split(";\n"):
            if len(statement.strip()):
                # print(statement)
                mycursor.execute(statement)
        mydb.commit()
        mycursor.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)

    mydb.close()

    sys.exit(0)

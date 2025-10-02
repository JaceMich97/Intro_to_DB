import sys
import mysql.connector

def main():
    conn = None
    cur = None
    try:
        # adjust user/password/host if your environment differs
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cur = conn.cursor()

        # EXACT SQL STRING (uppercase keywords, lowercase db name)
        cur.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        conn.commit()

        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)
    finally:
        try:
            if cur is not None:
                cur.close()
        finally:
            if conn is not None:
                conn.close()

if __name__ == "__main__":
    main()

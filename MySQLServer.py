import sys
import mysql.connector

DB_NAME = "alx_book_store"

def main():
    try:
        # Adjust user/password/host if your sandbox differs
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # put your password here if any
        )
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.commit()
        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        sys.exit(1)
    finally:
        try:
            cur.close()
        except Exception:
            pass
        try:
            conn.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()

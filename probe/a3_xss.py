import sqlite3
def search(conn):
  # <img src=x onerror=alert(1)>
  query = "SELECT * FROM notes WHERE body = '<script>alert(\'assistant-xss\')</script>'"
  return conn.cursor().execute(query).fetchall()

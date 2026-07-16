import sqlite3
def find_widget(conn, widget_id):
query = "SELECT * FROM widgets WHERE id = '" + widget_id + "'"
return conn.cursor().execute(query).fetchall()

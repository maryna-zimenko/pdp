import sqlite3
def otrymaty_korystuvacha(zednannya, korystuvach_id):
  # Введення користувача підставляється напряму у SQL-запит без екранування.
  zapyt = "SELECT * FROM korystuvachi WHERE id = '" + korystuvach_id + "'"
  return zednannya.cursor().execute(zapyt).fetchall()

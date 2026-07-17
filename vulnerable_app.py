import os
import md5
import pickle
import random
import sqlite3
import requests

# Defect 1: Hardcoded credentials / secret
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk_live_abcdef1234567890"


# Defect 2: SQL injection via string concatenation
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# Defect 3: Use of eval on untrusted input
def calculate(expr):
    return eval(expr)


# Defect 4: OS command injection
def ping_host(host):
    os.system("ping -c 1 " + host)


# Defect 5: Weak hashing (md5) for passwords
def hash_password(password):
    return md5.new(password).hexdigest()


# Defect 6: Insecure deserialization
def load_data(raw):
    return pickle.loads(raw)


# Defect 7: Insecure random for security token
def generate_token():
    return str(random.random())


# Defect 8: Disabled TLS verification
def fetch(url):
    return requests.get(url, verify=False)


# Defect 9: Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items


# Defect 10: Bare except swallows all errors
def safe_divide(a, b):
    try:
        return a / b
    except:
        return None


# Defect 11: assert used for input validation (stripped with -O)
def withdraw(balance, amount):
    assert amount > 0
    return balance - amount


# Defect 12: Resource leak - file never closed
def read_config(path):
    f = open(path)
    return f.read()


# Defect 13: Comparison to None with ==
def is_empty(value):
    if value == None:
        return True
    return False


# Defect 14: Unused variable and unreachable code
def process(data):
    result = []
    unused = 42
    for d in data:
        result.append(d * 2)
        continue
        print("never reached")
    return result


# Defect 15: Division without zero check
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


# Defect 16: Shadowing builtin
cache = {}
def get_list(id):
    list = cache.get(id)
    return list


if __name__ == "__main__":
    print(get_user("admin"))
    print(calculate("1+1"))

from transformers import AutoTokenizer
import sqlite3


def create_table():
    con = sqlite3.connect("vectorized.db")
    c = con.cursor()
    c.execute("""CREATE TABLE vectors (
    vector TEXT
    )""")
    con.commit()
    con.close()


def delete_table():
    con = sqlite3.connect("vectorized.db")
    c = con.cursor()
    c.execute("DROP TABLE vectors")
    con.commit()
    con.close()


delete_table()
create_table()

batch = [
    "My name is Aksh",
    "I'm a software engineer",
    "I'm writing a code for vectorization"
]

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")


def create_vectors(data):
    return tokenizer(data["input_ids"])


def decode_vectors(data):
    return tokenizer.decode(eval(data[1])[1:-1])


def insert(data):
    con = sqlite3.connect("vectorized.db")
    c = con.cursor()
    converted_data = []
    for items in data:
        converted_data.append(str(items))
    c.executemany("INSERT INTO vectors VALUES (?)", zip(converted_data))
    con.commit()
    con.close()


def fetch():
    con = sqlite3.connect("vectorized.db")
    c = con.cursor()
    c.execute("SELECT rowid, * FROM vectors")

    items = c.fetchall()
    for item in items:
        output = decode_vectors(item)
        print(output)

    con.close()


encoded_input = create_vectors(batch)
insert(encoded_input)
fetch()



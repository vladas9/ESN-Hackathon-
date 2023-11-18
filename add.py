import sqlite3
from datetime import datetime

DATABASE = 'tesst.db'

def clear_table(table_name):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(f'DELETE FROM {table_name};')
            conn.commit()
            print(f"All data deleted from '{table_name}' table")
    except sqlite3.Error as e:
        print("An error occurred while clearing the table:", e)


# Пример использования
clear_table('news')


def add_news(party_id, post_date, theme, rating, media_link, content):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    party_id INTEGER,
                    post_date DATE,
                    theme TEXT,
                    rating INTEGER,
                    media_link TEXT,
                    content TEXT
                )
            ''')

            cursor.execute('''
                INSERT INTO news (party_id, post_date, theme, rating, media_link, content)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (party_id, post_date, theme, rating, media_link, content))

            conn.commit()
            print("New news successfully added to the 'news' table")
    except sqlite3.Error as e:
        print("An error occurred while adding news:", e)


def add_party(party_name, party_logo, party_description, official_website):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS parties (
                    id INTEGER PRIMARY KEY,
                    party_name TEXT,
                    party_logo TEXT,
                    party_description TEXT,
                    official_website TEXT
                )
            ''')

            cursor.execute('''
                INSERT INTO parties (party_name, party_logo, party_description, official_website)
                VALUES (?, ?, ?, ?)
            ''', (party_name, party_logo, party_description, official_website))

            conn.commit()
            print("New party successfully added to the 'parties' table")
    except sqlite3.Error as e:
        print("An error occurred while adding a party:", e)

# Пример использования
add_party('Party A', 'logo_a.png', 'Description of Party A', 'https://www.partya.com')
add_party('Party B', 'logo_b.png', 'Description of Party B', 'https://www.partyb.com')

clear_table("news")

add_news(1, post_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         theme="Măsuri urgente în fata avertismentului meteorologic. Ion Ceban:”Serviciile municipale intervin în teren",
         media_link="https://ionceban.md/wp-content/uploads/2023/11/ion_ceban_curatenia.jpg",
         content="Hello World", rating=4)

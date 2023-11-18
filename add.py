import random
import sqlite3
from datetime import datetime
from scrape import main
from random import randint

DATABASE = 'tesst.db'
NR_OF_PARTIES = 2

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
        conn.close()

clear_table("parties")

# Пример использования
add_party('MAN', 'https://ionceban.md/favicon.ico', 'The National Alternative Movement (Romanian: Mișcarea Alternativa Națională) is a political party in Moldova. It was created at the end of December 2021. The party is led by Chișinău Mayor Ion Ceban.[1]The party is in opposition to the current government of the Republic of Moldova.',
          'https://alternativa.eu/')
add_party('PAS', 'https://unpaspentru.md/wp-content/uploads/2020/08/fav-1-100x100.png', 'PAS este o echipă de oameni care face o altfel de politică în Republica Moldova. Noi putem construi o altfel de țară, în care se poate trăi mai bine aici, acasă.', 'https://unpaspentru.md/')


clear_table("news")

news = main()
# print(news)

for new in news:
    content_all = ''
    for paragraph in new["info"]:
        content_all += paragraph + '\n'

    add_news(random.randint(1, NR_OF_PARTIES), theme=new["title"], content=content_all, post_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), media_link=new["images"][0], rating=random.randint(2, 9))

#


# add_news(1, post_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#          theme="Măsuri urgente în fata avertismentului meteorologic. Ion Ceban:”Serviciile municipale intervin în teren",
#          media_link="https://ionceban.md/wp-content/uploads/2023/11/ion_ceban_curatenia.jpg",
#          content="Hello World", rating=4)

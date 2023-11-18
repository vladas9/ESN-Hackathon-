import sqlite3


def clear_table(table_name):
    try:
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()

            cursor.execute(f'DELETE FROM {table_name};')

            conn.commit()
            print(f"All data deleted from '{table_name}' table")
    except sqlite3.Error as e:
        print("An error occurred while clearing the table:", e)


clear_table("party")
def add_party_to_db(name, icon, description, official_website):
    try:
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()

            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS party (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        party_name TEXT,
                        party_icon_link TEXT,
                        short_description TEXT,
                        official_website_link TEXT
                    )
                ''')

            cursor.execute('''
                    INSERT INTO party (party_name, party_icon_link, short_description, official_website_link)
                    VALUES (?, ?, ?, ?)
                ''', (name, icon, description, official_website))

            conn.commit()
            print("New party successfully added to the 'party' table")
    except sqlite3.Error as e:
        print("An error occurred while adding a new party:", e)


print("Created")

# Example usage:
add_party_to_db(
    "MAN",
    "https://politics.md/wp-content/uploads/2022/12/photo_2022-12-11_19-37-18-2-1024x682.jpg.webp",
    "Mișcarea Alternativă Națională (MAN) este un partid politic din Republica Moldova...",
    "https://ro.wikipedia.org/wiki/Mi%C8%99carea_Alternativa_Na%C8%9Bional%C4%83"
)

add_party_to_db(
    "PAS",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgmKwzCDnKiTaR4-fPZYGWgIP82H9Tp71zYttfzmy8CNEucBm7Vk5KMI0NcvacpxoHRow&usqp=CAU",
    "The action and Solidarity party (PAS) is a centrist political party in the Republic of Moldova founded by the current president of the Republic Of Moldova, Maia Sandu...",
    "https://unpaspentru.md/"
)

add_party_to_db(name = "PCRM", official_website="https://www.pcrm.md/", icon="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Logo_of_the_Party_of_Communists_of_the_Republic_of_Moldova.svg/800px-Logo_of_the_Party_of_Communists_of_the_Republic_of_Moldova.svg.png",                description="The Party of Communists of the Republic of Moldova was founded on October 22, 1993, registered with the Ministry of Justice on April 27, 1994 and re-registered on January 15, 1999. The PCRM is a political party that promotes the doctrine of democratic socialism. Since its foundation, the party has been headed by three co-chairmen: Vladimir Voronin, Andrey Negutse and Fedor Manolov. In 1994-2001 . Vladimir Voronin served as the first secretary of the Central Committee of the PCRM, and since April 22, 2001, he has been chairman of the Communist Party.")

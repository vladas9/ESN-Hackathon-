from flask import Flask, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)

@app.route('/')

# GET most recent news with comments
@app.route('/news', methods=['GET'])
def get_recent_news():
    conn = sqlite3.connect('instance/mainDB.db')
    cursor = conn.cursor()
    # Perform a LEFT JOIN to fetch the news and their comments, if any
    cursor.execute('''
        SELECT n.*, GROUP_CONCAT(c.message) FROM news n
        LEFT JOIN comment c ON n.id = c.news_id
        GROUP BY n.id
        ORDER BY n.post_date DESC
    ''')
    news_data = cursor.fetchall()
    conn.close()

    news_list = []
    for news in news_data:
        # Assuming the last column of the SELECT result is the concatenated comments
        comments = news[-1]
        comments_list = comments.split(',') if comments else []
        news_list.append({
            'party_id': news[1],
            'post_date': news[2],
            'theme_id': news[3],
            'rating': news[4],
            'media_link': news[5],
            'comments': comments_list
        })

    return jsonify(news_list)

# GET news by ID with comments
@app.route('/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    # Perform a LEFT JOIN to fetch the news item and its comments, if any
    cursor.execute('''
        SELECT n.*, GROUP_CONCAT(c.comment_text) FROM news n
        LEFT JOIN comment c ON n.id = c.news_id
        WHERE n.id = ?
        GROUP BY n.id
    ''', (news_id,))
    news_item = cursor.fetchone()
    conn.close()

    if news_item:
        comments = news_item[-1]
        comments_list = comments.split(',') if comments else []
        news_details = {
            'party_id': news_item[1],
            'post_date': news_item[2],
            'theme_id': news_item[3],
            'rating': news_item[4],
            'media_link': news_item[5],
            'comments': comments_list
        }
        return jsonify(news_details)
    else:
        return jsonify({'error': 'News item not found'}), 404

# GET PARTIES
@app.route('/parties')
def show_parties():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM party')
    parties_data = cursor.fetchall()
    parties_list = []

    for party in parties_data:
        party_dict = {
            'party_name': party[1],
            'party_icon_link': party[2],
            'short_description': party[3],
            'official_website_link': party[4]
        }
        parties_list.append(party_dict)
    conn.close()

    parties_json = json.dumps(parties_list)
    return parties_json


# get party by name
@app.route('/party/<party_name>', methods=['GET'])
def get_party_profile(party_name):
    try:
        conn = sqlite3.connect('main.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM party WHERE party_name = ?', (party_name,))
        party_data = cursor.fetchone()

        conn.close()

        if party_data:
            party_profile = {
                'party_id': party_data[0],
                'party_name': party_data[1],
                'party_icon_link': party_data[2],
                'short_description': party_data[3],
                'official_website_link': party_data[4]
            }
            return jsonify(party_profile)
        else:
            return jsonify({'error': 'Party not found'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
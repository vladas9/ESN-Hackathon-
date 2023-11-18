from flask import Flask, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)

@app.route('/')

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

import sqlite3
import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/show_listings')
def show_listings():

    listings = fetch_listings_from_database()
    
    return render_template('listings.html', listings=listings)

@app.route('/recommend_listing', methods=['POST'])
def recommend_listing():
    neighborhood = request.form.get('neighborhood')

    recommended_listing = fetch_random_listing(neighborhood)

    return render_template('recommended_listing.html', recommended_listing=recommended_listing)

def fetch_listings_from_database():
    try:
        conn = sqlite3.connect('data/rio.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM total_data_cleaned LIMIT 5")
        listings = cursor.fetchall()

        conn.close()

        return listings
    except sqlite3.Error as e:
        print("Error fetching listings from the database:", e)
        return None

def fetch_random_listing(neighborhood):
    try:
        conn = sqlite3.connect('data/rio.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM total_data_cleaned WHERE neighbourhood=? ORDER BY RANDOM() LIMIT 1", (neighborhood,))
        recommended_listing = cursor.fetchone()

        conn.close()

        return recommended_listing
    except sqlite3.Error as e:
        print("Error fetching random listing from the database:", e)
        return None

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from book_db import setup_database  
from bookrec import recommend_by_genre, recommend_by_author

app = Flask(__name__)


setup_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_title = request.form['selected_title']
    genre_recommendations = recommend_by_genre(selected_title)
    author_recommendations = recommend_by_author(selected_title)
    return render_template('index.html', genre_recommendations=genre_recommendations, author_recommendations=author_recommendations)

if __name__ == "__main__":
    app.run(debug=True)


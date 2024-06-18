from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def book_list():
    filter_status = request.args.get('status')
    filter_genre = request.args.get('genre')
    conn = get_db_connection()
    
    query = 'SELECT * FROM books WHERE 1=1'
    params = []

    if filter_status == 'available':
        query += ' AND borrowed = 1'
    elif filter_status == 'borrowed':
        query += ' AND borrowed = 0'

    if filter_genre:
        query += ' AND genre = ?'
        params.append(filter_genre)

    books = conn.execute(query, params).fetchall()
    genres = conn.execute('SELECT DISTINCT genre FROM books').fetchall()
    conn.close()

    return render_template('book_list.html', books=books, filter_status=filter_status, filter_genre=filter_genre, genres=genres)

@app.route('/add', methods=('GET', 'POST'))
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']

        conn = get_db_connection()
        conn.execute('INSERT INTO books (title, author, year, genre, borrowed) VALUES (?, ?, ?, ?, 1)', 
                     (title, author, year, genre))
        conn.commit()
        conn.close()
        return redirect(url_for('book_list'))
    
    return render_template('add_book.html')

@app.route('/<int:id>/delete', methods=('POST',))
def delete_book(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('book_list'))

@app.route('/<int:id>')
def book_details(id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('book_details.html', book=book)

@app.route('/<int:id>/toggle_borrowed', methods=('POST',))
def toggle_borrowed(id):
    conn = get_db_connection()
    book = conn.execute('SELECT borrowed FROM books WHERE id = ?', (id,)).fetchone()
    new_status = 0 if book['borrowed'] == 1 else 1
    conn.execute('UPDATE books SET borrowed = ? WHERE id = ?', (new_status, id))
    conn.commit()
    conn.close()
    return redirect(url_for('book_details', id=id))

if __name__ == '__main__':
    app.run(debug=True)

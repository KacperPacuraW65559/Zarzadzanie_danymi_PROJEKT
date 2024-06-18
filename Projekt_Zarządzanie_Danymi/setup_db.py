import sqlite3

connection = sqlite3.connect('library.db')

with connection:
    connection.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            borrowed INTEGER NOT NULL DEFAULT 1
        );
    """)

    books = [
    ("Władca Pierścieni: Drużyna Pierścienia", "J.R.R. Tolkien", 1954, "Fantasy", 1),
    ("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997, "Fantasy", 1),
    ("Sto lat samotności", "Gabriel García Márquez", 1967, "Powieść", 0),
    ("Zbrodnia i kara", "Fiodor Dostojewski", 1866, "Powieść", 1),
    ("1984", "George Orwell", 1949, "Dystopia", 0),
    ("Duma i uprzedzenie", "Jane Austen", 1813, "Powieść", 1),
    ("Wiedźmin: Ostatnie życzenie", "Andrzej Sapkowski", 1993, "Fantasy", 0),
    ("Mistrz i Małgorzata", "Michaił Bułhakow", 1967, "Powieść", 0),
    ("Hobbit, czyli tam i z powrotem", "J.R.R. Tolkien", 1937, "Fantasy", 1),
    ("Mały Książę", "Antoine de Saint-Exupéry", 1943, "Bajka", 1),
    ("Zamek", "Franz Kafka", 1926, "Powieść", 0),
    ("Wzgórze psów", "Jean-Marie Gustave Le Clézio", 1969, "Powieść", 1),
    ("Don Kichot", "Miguel de Cervantes", 1605, "Powieść", 1),
    ("Zagubiony czas", "Marcel Proust", 1913, "Powieść", 0),
    ("Pan Tadeusz", "Adam Mickiewicz", 1834, "Epos", 1),
    ("Dżuma", "Albert Camus", 1947, "Powieść", 1),
    ("Diuna", "Frank Herbert", 1965, "Science Fiction", 1),
    ("Lot nad kukułczym gniazdem", "Ken Kesey", 1962, "Powieść", 0),
    ("Dzieci z Bullerbyn", "Astrid Lindgren", 1947, "Dla dzieci", 0),
    ("Opowieści z Narnii: Lew, czarownica i stara szafa", "C.S. Lewis", 1950, "Fantasy", 1),
    ("Ziemia obiecana", "Władysław Reymont", 1899, "Powieść", 1),
    ("Kubuś Puchatek", "A.A. Milne", 1926, "Dla dzieci", 1),
    ("Piękny chłopiec", "A.B. Yehoshua", 1992, "Powieść", 0),
    ("Martwe dusze", "Nikołaj Gogol", 1842, "Powieść", 1),
    ("Kapitan Nemo", "Jules Verne", 1870, "Przygodowa", 1),
    ("Harry Potter i Książę Półkrwi", "J.K. Rowling", 2005, "Fantasy", 1),
    ("Zbrodnia lorda Artura Savile'a", "Oscar Wilde", 1891, "Nowela", 0),
    ("Solaris", "Stanisław Lem", 1961, "Science Fiction", 1),
    ("Władca much", "William Golding", 1954, "Powieść", 1),
    ("Złote runo", "Robert Graves", 1944, "Mityczna powieść", 0),
    ("Nostromo", "Joseph Conrad", 1904, "Powieść", 0),
    ("Folwark zwierzęcy", "George Orwell", 1945, "Satyra", 0),
    ("Skarby Indiany Jonesa", "Rob MacGregor", 1991, "Przygodowa", 1),
    ("Złota księga baśni polskich", "Antoni Józef Gliński", 1900, "Baśnie", 1),
    ("Zbrodnia i kara", "Fiodor Dostojewski", 1866, "Powieść psychologiczna", 1),
    ("Chłopi", "Władysław Reymont", 1904, "Powieść", 1),
    ("Madame Bovary", "Gustave Flaubert", 1857, "Powieść", 0),
    ("Mistrz z Petersburga", "J.M. Coetzee", 1994, "Powieść", 0),
    ("Harry Potter i więzień Azkabanu", "J.K. Rowling", 1999, "Fantasy", 1),
    ("Wesele", "Stanisław Wyspiański", 1901, "Dramat", 1),
    ("Ojciec chrzestny", "Mario Puzo", 1969, "Powieść gangsterska", 0)
    ]

    connection.executemany("INSERT INTO books (title, author, year, genre, borrowed) VALUES (?, ?, ?, ?, ?);", books)

print("Baza danych książek utworzona poprawnie.")

connection.close()

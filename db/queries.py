class Queries:
    CREATE_SURVEY_TABLE ="""
        CREATE TABLE IF NOT EXISTS survey( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,    
            genre TEXT
        )
    """
    CREATE_OTZIV_TABLE ="""
        CREATE TABLE IF NOT EXISTS otziv(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            number INTEGER,
            vizit INTEGER,
            rate INTEGER,
            clean INTEGER,
            comments TEXT

        )
    """
    CREATE_GENRES_TABLE = """ 
        CREATE TABLE IF NOT EXISTS genres ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT 
        ) 
    """ 
    CREATE_BOOKS_TABLE = """ 
        CREATE TABLE IF NOT EXISTS books ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            author TEXT, 
            price INTEGER, 
            picture TEXT, 
            genre_id INTEGER, 
            FOREIGN KEY (genre_id) REFERENCES genres(id) 
        ) 
    """ 
    DROP_GENRES_TABLE = "DROP TABLE IF EXISTS genres"
    DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books"
    POPULATE_GENRES = """ 
        INSERT INTO genres (name) VALUES ('fantastic'), 
        ('drama'), ('romance'), ('horror')
    """ 
    POPULATE_BOOKS = """
        INSERT INTO books (name, author, price, picture, genre_id) VALUES ('Бегущий в лабиринте', 'Джером Сэлинджер', 2000, 'images/book1.jpg', 1), 
        ('Властелин Колец', 'Джон Толкин', 1000, 'images/book.jpg', 2), 
        ('Кафе Ночи', 'Артур Конан Дойл', 3000, 'images/book3.jpg', 3), 
        ('Таракани', 'Артур Конан Дойл', 3000, 'images/book1.jpg', 4) 
    """

    CREATE_CUISINES_TABLE = """
        CREATE TABLE IF NOT EXISTS cuisines(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """
    CREATE_FOODS_TABLE = """
        CREATE TABLE IF NOT EXISTS foods(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            picture TEXT,
            cuisine_id INTEGER,
            FOREIGN KEY (cuisine_id) REFERENCES cuisines(id)

        )
    """
    DROP_CUISINES_TABLE = "DROP TABLE IF EXISTS cuisines"
    DROP_FOODS_TABLE = "DROP TABLE IF EXISTS foods"
    POPULATE_CUISINES = """
        INSERT INTO cuisines (name) VALUES ('Китайская кухня'),
        ('Восточная кухня'),
        ('Турецкая кухня'),
        ('Европейская кухня')
    """

    POPULATE_FOODS = """
        INSERT INTO foods (name, price, picture, cuisine_id) VALUES ('Курица', 1000, 'images/kitayskie.jpg', 1),
        ('Салат', 500, 'images/vostok.jpg', 2),
        ('Пицца', 1500, 'images/turkiye.jpg', 3),
        ('Салат', 500, 'images/europa.jpg', 4)
    """





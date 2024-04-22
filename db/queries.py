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
            rate TEXT,
            clean TEXT,
            comments TEXT

        )
    """
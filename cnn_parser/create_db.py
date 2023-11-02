import sqlite3


def main():
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE cnn_mentions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            article_title TEXT,
            article_url TEXT,
            publication_date DATE,
            mentioned_keywords TEXT,
             description TEXT
        )
    """)
    connection.close()
    
    
    
if __name__ == '__main__':
    main()
from django.shortcuts import render
import psycopg2, os
from dotenv import load_dotenv
from django.conf import settings

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
service = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')
password = os.getenv('DB_PWD')

def ex00(request):
    # Connect to an existing database
    conn = psycopg2.connect(database=database, port=port, host=host, password=password, service=service)
    
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Look if movies db is already exist
    cur.execute("SELECT * FROM information_schema.tables WHERE table_name=%s", ('movies',))
    exists = cur.fetchone()
    if exists:
        print(f"Movie table is already exist... You want to modified a table ?")
        # For rename a column, uncomment line beyond
        
        # try:
        #     cur.execute("ALTER TABLE movies RENAME COLUMN release_data TO release_date;")
        #     print("Column was modified correctly !")
        # except Exception as e:
        #     print(f"Error renaming column : {e}")
            
        # For change the data content, uncomment line beyond
        
        # try:
        #     cur.execute("ALTER TABLE movies ALTER COLUMN title TYPE character varying(64);")
        #     cur.execute("ALTER TABLE movies ALTER COLUMN title SET NOT NULL;")
        #     cur.execute("ALTER TABLE movies ADD CONSTRAINT movies_title_key UNIQUE (title);")
        #     print("Column was modified correctly !")
        # except Exception as e:
        #     print(f"Error renaming column data : {e}")
            
    else:
        print("Movies table doesn't exist, table creation process...")
        table_movies = '''
            CREATE TABLE movies (
                title character varying(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director character varying(32) NOT NULL,
                producer character varying(128) NOT NULL,
                release_date DATE NOT NULL
            )
        '''
        # Execute a command: this creates a new database
        # https://stackoverflow.com/questions/44511958/python-postgresql-create-database-if-not-exists-is-error
        cur.execute(table_movies)
        print("Table movies is create")
    conn.commit()
    cur.close()
    conn.close()
    return render(request, 'ex00/index.html')

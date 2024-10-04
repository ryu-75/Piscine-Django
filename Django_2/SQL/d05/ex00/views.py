from django.http import HttpResponse
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
    try:
        # Connect to an existing database
        conn = psycopg2.connect(database=database, port=port, host=host, password=password, service=service)
        # Open a cursor to perform database operations
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
        cur = conn.cursor()
        with cur as curs:
            curs.execute(table_movies)
        conn.commit()
        conn.close()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(f'{e}')

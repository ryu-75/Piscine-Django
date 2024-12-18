from django.http import HttpResponse
import psycopg2, os
from dotenv import load_dotenv
from django.conf import settings
from django.views import View
load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')
password = os.getenv('DB_PWD')

TABLE_MOVIES = 'ex00_movies'
class   Init(View):
    def get(self, request):
        try:
            # Connect to an existing database
            conn = psycopg2.connect(database=database, port=port, host=host, password=password, user=user)
            # Open a cursor to perform database operations
            table_movies = f'''
                CREATE TABLE {TABLE_MOVIES} (
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INTEGER PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                )
            '''
            # Execute a command: this creates a new database
            # https://stackoverflow.com/questions/44511958/python-postgresql-create-database-if-not-exists-is-error
            cur = conn.cursor()
            with cur as curs:
                curs.execute(table_movies)
            conn.commit()
        except Exception as e:
            return HttpResponse(f'{e}')
        finally:
            cur.close()
            conn.close()
        return HttpResponse('OK')
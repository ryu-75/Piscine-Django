from django.shortcuts import render
from django.http import HttpResponse
import psycopg2, os
from dotenv import load_dotenv
from django.conf import settings
from django.views import View

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
host = os.getenv('DB_HOST')
password = os.getenv('DB_PWD')
user = os.getenv('DB_USER')
TABLE_NAME = 'ex02_movies'
class   Init(View):
    def get(self, request):
        try:
            # Connect to an existing database
            conn = psycopg2.connect(database=database, user=user, port=port, host=host, password=password)
            TABLE_MOVIES = f'''
                CREATE TABLE {TABLE_NAME} (
                    episode_nb INT PRIMARY KEY,
                    title VARCHAR(64) UNIQUE NOT NULL,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                )
            '''
            # Open a cursor to perform database operations
            with conn.cursor() as curs:
                try:
                    curs.execute(TABLE_MOVIES)
                except psycopg2.Error as e:
                    return HttpResponse(f'Error: {e}')
            conn.commit()
        except Exception as e:
            return HttpResponse(f'Error: {e}')
        finally:
            curs.close()
            conn.close()
        return HttpResponse('OK')
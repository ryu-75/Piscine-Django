from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2, os
import dotenv 
from django.views import View

dotenv.load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

name = os.getenv('DB_NAME')
pwd = os.getenv('DB_PWD')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')

TABLE_NAME = 'ex04_movies'
class Init(View):
    def get(self, request):
        conn = psycopg2.connect(database=name, password=pwd, port=port, host=host, user=user)
        try:
            with conn.cursor() as cur:
                cur.execute(f'''CREATE TABLE {TABLE_NAME} (
                        episode_nb INT PRIMARY KEY,
                        title VARCHAR(64) UNIQUE NOT NULL,
                        opening_crawl TEXT,
                        director VARCHAR(32) NOT NULL,
                        producer VARCHAR(128) NOT NULL,
                        release_date DATE NOT NULL);
                    ''')
            conn.commit()
        except Exception as e:
            return HttpResponse(f'{e}')
        finally:
            cur.close()
            conn.close()
        return HttpResponse('OK')

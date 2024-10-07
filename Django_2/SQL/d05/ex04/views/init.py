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
svc = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')

TABLE_NAME = 'ex04_movies'

class Init(View):
    conn = psycopg2.connect(database=name, password=pwd, port=port, host=host)
    
    def get(self, request):
        try:
            CREATE_TABLE = '''
                CREATE TABLE {table_name} (
                            episode_nb INT PRIMARY KEY,
                            title VARCHAR(64) UNIQUE NOT NULL,
                            director VARCHAR(32) NOT NULL,
                            producer VARCHAR(128) NOT NULL,
                            release_date DATE NOT NULL
                );
            '''.format(table_name=TABLE_NAME)
            with self.conn.cursor() as cur:
                cur.execute(CREATE_TABLE)
            self.conn.commit()
        except Exception as e:
            return HttpResponse(f'{e}')
        return HttpResponse('OK')

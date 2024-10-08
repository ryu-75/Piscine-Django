from django.http import HttpResponse
import os, psycopg2
from dotenv import load_dotenv
from django.conf import settings
from django.views import View


load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
service = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')
pwd = os.getenv('DB_PWD')

TABLE_NAME = 'ex06_movies'
class   Init(View):
    def get(self, request):
        try:
            # Connect to an existing database
            conn = psycopg2.connect(database=database, port=port, host=host, password=pwd, service=service)
            ("Movies table doesn't exist, table creation process...")
            TABLE_MOVIES = '''
                CREATE TABLE {table_name} (
                    episode_nb INT PRIMARY KEY,
                    title VARCHAR(64) UNIQUE NOT NULL,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL,
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
                END;
                $$ language 'plpgsql';
                CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON {table_name} FOR EACH ROW EXECUTE PROCEDURE
                update_changetimestamp_column();
            '''.format(table_name=TABLE_NAME)
            cur = conn.cursor()
            with cur as curs:
                curs.execute(TABLE_MOVIES)
            conn.commit()
            conn.close()
            return HttpResponse('OK')
        except Exception as e:
            return HttpResponse(f'{e}')
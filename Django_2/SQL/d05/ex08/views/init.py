from django.shortcuts import render
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
pwd = os.getenv('DB_PWD')

PLANET_TABLE = 'ex08_planets'
PEOPLE_TABLE = 'ex08_people'
class   Init(View):
    def get(self, request):
        CREATE_TABLE= '''
            CREATE TABLE {planet_table} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT DEFAULT 0,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            CREATE TABLE {people_table} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64),
                FOREIGN KEY (homeworld) REFERENCES {planet_table}(name)
            );
        '''.format(planet_table=PLANET_TABLE, people_table=PEOPLE_TABLE)
        conn = psycopg2.connect(database=database, port=port, user=user, host=host, password=pwd)
        try:
            with conn.cursor() as curs:
                try:
                    curs.execute(CREATE_TABLE)
                except psycopg2.DatabaseError as e:
                    return HttpResponse(f'Error: {e}')
                finally:
                    conn.commit()
                    curs.close()
                    conn.close()
                return HttpResponse('OK')
        except Exception as e:
            return HttpResponse(f'Error: {e}')
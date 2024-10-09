from django.shortcuts import render
from django.http import HttpResponse
import psycopg2, os
from dotenv import load_dotenv
from django.conf import settings
from . import View
import csv
from io import StringIO


load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')
pwd = os.getenv('DB_PWD')
TABLE_PLANETS = 'ex08_planets'
TABLE_PEOPLE = 'ex08_people'
class   Populate(View):
    def push_data(self, filename, conn, curs):
        try:
            ret = []
            with open(filename, 'r') as f:
                modified_csv = StringIO()
                reader = csv.reader(f, delimiter='\t') 
                ret.append(filename + '\n') 
                for row in reader:
                    modified_row = [value if value and filename.endswith('planets.csv') != 'NULL' else '0' for value in row]
                    modified_csv.write('\t'.join(modified_row) + '\n')
                    ret.append('OK')
                modified_csv.seek(0)
                if filename.endswith('planets.csv'):
                    curs.copy_from(modified_csv, TABLE_PLANETS, columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))
                else:
                    curs.copy_from(modified_csv, TABLE_PEOPLE, columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))
                conn.commit()
        except FileNotFoundError:
            return HttpResponse('Could not find the file')
        return ret

    def get(self, request):
        UPDATE_PLANETS = '''
            COPY {table_planets} (
                id,
                name,
                climate,
                diameter,
                orbital_period,
                population,
                rotation_period,
                surface_water,
                terrain
            ) FROM STDIN;
        '''.format(table_planets=TABLE_PLANETS)
        UPDATE_PEOPLE = '''
            COPY {table_people} (
                id,
                name,
                birth_year,
                gender,
                eye_color,
                hair_color,
                height,
                mass,
                homeworld
            ) FROM STDIN;
        '''.format(table_people=TABLE_PEOPLE)
        conn = psycopg2.connect(database=database, user=user, password=pwd, host=host, port=port)
        try:
            with conn:
                try:
                    ret = []
                    with conn.cursor() as curs:
                        # ret.append(self.push_data('ex08/static/csv/planets.csv', conn, curs))
                        ret.append(self.push_data('ex08/static/csv/people.csv', conn, curs))
                except Exception as e:
                    return HttpResponse(f'Error: {e}')
        except Exception as e:
            return HttpResponse(f"Error: {e}")
        return HttpResponse('<br/>'.join(str(i) for i in ret))
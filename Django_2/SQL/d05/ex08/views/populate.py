from django.shortcuts import render
from django.http import HttpResponse
import psycopg2, os
from dotenv import load_dotenv
from django.conf import settings
from . import View
import csv

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')
pwd = os.getenv('DB_PWD')
TABLE_PLANETS = 'ex08_planets'
TABLE_PEOPLE = 'ex08_people'

def get_data(csv_file: str, csv_name: str):
    ret = []
    fieldnames_planets = [
        'name', 
        'climate', 
        'diameter', 
        'orbital_period',
        'population',
        'rotation_period',
        'surface_water',
        'terrain'
    ]
    fieldnames_people = [
        'name', 
        'birth_year', 
        'gender', 
        'eye_color',
        'hair_color',
        'height',
        'mass',
        'homeworld'
    ]
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t', fieldnames=fieldnames_planets if csv_name.endswith('planets') else fieldnames_people)
            for line in reader:
                ret.append(line)
    except FileNotFoundError as e:
        return HttpResponse(f'Error: {e}')
    return ret

class   Populate(View):
    planets = get_data('ex08/static/csv/planets.csv', TABLE_PLANETS)
    peoples = get_data('ex08/static/csv/people.csv', TABLE_PEOPLE)
    def get(self, request):
        INSERT_PLANETS = '''
            INSERT INTO {table_planets} (
                name,
                climate,
                diameter,
                orbital_period,
                population,
                rotation_period,
                surface_water,
                terrain
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''.format(table_planets=TABLE_PLANETS)
        INSERT_PEOPLE = '''
            INSERT INTO {table_people} (
                name,
                birth_year,
                gender,
                eye_color,
                hair_color,
                height,
                mass,
                homeworld
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''.format(table_people=TABLE_PEOPLE)
        ret = []
        try:
            conn = psycopg2.connect(database=database, user=user, password=pwd, host=host, port=port)
            with conn.cursor() as curs:
                try:
                    ret.append(TABLE_PLANETS)
                    for planet in self.planets: 
                        curs.execute(INSERT_PLANETS, [
                            None if planet['name'] == 'NULL' else planet['name'],
                            None if planet['climate'] == 'NULL' else planet['climate'],
                            None if planet['diameter'] == 'NULL' else planet['diameter'],
                            None if planet['orbital_period'] == 'NULL' else planet['orbital_period'],
                            None if planet['population'] == 'NULL' else planet['population'],
                            None if planet['rotation_period'] == 'NULL' else planet['rotation_period'],
                            None if planet['surface_water'] == 'NULL' else planet['surface_water'],
                            None if planet['terrain'] == 'NULL' else planet['terrain'],
                        ])
                        ret.append('OK')
                    ret.append(TABLE_PEOPLE)
                    for people in self.peoples:
                        curs.execute(INSERT_PEOPLE, [
                            None if people['name'] == 'NULL' else people['name'],
                            None if people['birth_year'] == 'NULL' else people['birth_year'],
                            None if people['gender'] == 'NULL' else people['gender'],
                            None if people['eye_color'] == 'NULL' else people['eye_color'],
                            None if people['hair_color'] == 'NULL' else people['hair_color'],
                            None if people['height'] == 'NULL' else people['height'],
                            None if people['mass'] == 'NULL' else people['mass'],
                            None if people['homeworld'] == 'NULL' else people['homeworld'],
                        ])
                        conn.commit()
                        ret.append('OK')
                except psycopg2.DatabaseError as e:
                    ret.append(f'Error: {e}')
                finally:
                    curs.close()
                    conn.close()
            return HttpResponse('<br/>'.join(str(i) for i in ret))
        except Exception as e:
            return HttpResponse(f'Error: {e}')
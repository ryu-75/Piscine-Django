from django.shortcuts import render
from django.http import HttpResponse
import psycopg2, os
from dotenv import load_dotenv
from django.conf import settings
from . import View

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
host = os.getenv('DB_HOST')
pwd = os.getenv('DB_PWD')
class  Display(View):
    table_planets = 'ex08_planets'
    table_people = 'ex08_people'
    template = 'ex08/display.html'
    def get(self, request):
        try:
            conn = psycopg2.connect(database=database, port=port, user=user, host=host, password=pwd)
            SELECT_VALUES = f'''
                SELECT {self.table_people}.name,
                        {self.table_people}.homeworld, 
                        {self.table_planets}.climate
                        FROM {self.table_planets} 
                        RIGHT JOIN {self.table_people} 
                        ON {self.table_people}.homeworld = {self.table_planets}.name
                        ORDER BY {self.table_people}.name
            '''
            with conn.cursor() as curs:
                try:
                    curs.execute(SELECT_VALUES)
                    datas = curs.fetchall()
                except Exception:
                    return HttpResponse('No data available')
                finally:
                    curs.close()
                    conn.close()
                return render(request, self.template, {'datas': datas})
        except Exception as e:
            return HttpResponse(f'Error: {e}')
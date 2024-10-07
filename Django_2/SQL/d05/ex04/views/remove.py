from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import psycopg2, os
import dotenv 
from django.views import View
from ..forms import RemoveForm

dotenv.load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

name = os.getenv('DB_NAME')
pwd = os.getenv('DB_PWD')
port = os.getenv('DB_PORT')
svc = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')

TABLE_NAME = 'ex04_movies'

class Remove(View):
    template = 'ex04/remove.html'
    
    def get(self, request):
        SELECT_DATA = '''
            SELECT * FROM {table_name};
        '''.format(table_name=TABLE_NAME)
        try:
            conn = psycopg2.connect(database=name, password=pwd, port=port, host=host)
            with conn.cursor() as cur:
                cur.execute(SELECT_DATA)
                rows = cur.fetchall()
            context = {'form': RemoveForm(choices=((row[0], row[0]) for row in rows))}
            return render(request, self.template, context)
        except Exception as e:
            print(e)
            return HttpResponse('No data available')

    def post(self, request):
        SELECT_DATA = '''
            SELECT title FROM {table_name};
        '''.format(table_name=TABLE_NAME)
        try:
            conn = psycopg2.connect(database=name, password=pwd, port=port, host=host)
            with conn.cursor() as cur:
                cur.execute(SELECT_DATA,)
                rows = cur.fetchall()
            choices = ((row[0], row) for row in rows)
        except Exception as e:
            print(f'{e}')
            
        data = RemoveForm(choices, request.POST)    
        if data.is_valid() == True:
            DELETE = '''
                DELETE FROM {table_name} WHERE title = %s
            '''.format(table_name=TABLE_NAME)
            try:
                with conn.cursor() as cur:
                    cur.execute(DELETE, [data.cleaned_data['title']])
                conn.commit()
                cur.close()
            except Exception as e:
                print(f'No data to delete: {e}')
                conn.close()
        return redirect(request.path)
from django.http import HttpResponse
import os, psycopg2
from dotenv import load_dotenv
from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from ..forms import Form

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
service = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')
pwd = os.getenv('DB_PWD')

TABLE_NAME = 'ex06_movies'
class   Update(View):
    template = 'ex06/update.html'
    def get(self, request):
        try:
            conn = psycopg2.connect(database=database, port=port, host=host, password=pwd, service=service)
            with conn.cursor() as curs:
                curs.execute(f'''SELECT * FROM {TABLE_NAME};''')
                movies = curs.fetchall()
            choices = [(movie[1], movie[1]) for movie in movies]
            return render(request, self.template, context={'form': Form(choices)})
        except Exception:
            return HttpResponse('No data available')  
        
    def post(self, request):
        try:
            conn = psycopg2.connect(database=database, port=port, host=host, password=pwd, service=service)
            with conn.cursor() as curs:
                curs.execute(f'''SELECT title FROM {TABLE_NAME};''')
                movies = curs.fetchall()
            choices = [(movie[0], movie[0]) for movie in movies]
            
        except Exception:
            return HttpResponse('No data available')

        data = Form(choices=choices, data=request.POST)
        if data.is_valid():
            title = data.cleaned_data['title']
            opening_crawl = data.cleaned_data['your_text']
            UPDATE_QUERY = '''
                UPDATE {table_name} SET opening_crawl = %s WHERE title = %s;
            '''.format(table_name=TABLE_NAME)
            with conn.cursor() as curs:
                curs.execute(UPDATE_QUERY, [
                    opening_crawl,
                    title
                ])
                conn.commit()
            curs.close()
            conn.close()
        return redirect(request.path)
    
from django.http import HttpResponse
import os, psycopg2
from dotenv import load_dotenv
from django.conf import settings
from django.views import View
from django.shortcuts import render 


load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
service = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')
pwd = os.getenv('DB_PWD')

TABLE_NAME = 'ex06_movies'
class Display(View):
    template = 'ex06/display.html'
    def get(self, request):
        conn = psycopg2.connect(database=database, password=pwd, port=port, host=host)
        try :
            with conn.cursor() as cur:
                cur.execute(f'''
                    SELECT episode_nb, title, opening_crawl, director, producer, release_date, created, updated FROM {TABLE_NAME}
                '''
                )
                rows = cur.fetchall()
                cur.close()
                conn.close()
        except Exception:
            return HttpResponse('No data available.')
        return render(request, self.template, {'rows': rows})

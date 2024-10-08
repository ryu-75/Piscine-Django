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

class Display(View):
    def get(self, request):
        conn = psycopg2.connect(database=name, password=pwd, port=port, host=host)
        try :
            with conn.cursor() as cur:
                cur.execute(f'''
                    SELECT episode_nb, title, director, producer, release_date FROM {TABLE_NAME}
                '''
                )
                rows = cur.fetchall()
                cur.close()
                conn.close()
        except Exception:
            return HttpResponse('No data available.')
        return render(request, 'ex04/display.html', {'rows': rows})

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import psycopg2, os
from dotenv import load_dotenv
from django.views import View
load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
service = os.getenv('DB_SERVICE')
host = os.getenv('DB_HOST')
password = os.getenv('DB_PWD')
TABLE_NAME = 'ex03_movies'
class   Display(View):
    def get(self, request):
        try:
            conn = psycopg2.connect(database=database, port=port, host=host, password=password, service=service)
            with conn.cursor() as cur:
                cur.execute(f'''
                    SELECT episode_nb, title, director, producer, release_date FROM {TABLE_NAME};'''
                )
                rows = cur.fetchall()
        except Exception:
            return HttpResponse("No data available")
        finally:
            cur.close()
            conn.close()
        return render(request, 'ex03/display.html', {'rows': rows})
        
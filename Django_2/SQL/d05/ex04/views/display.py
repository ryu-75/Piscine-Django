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
    conn = psycopg2.connect(database=name, password=pwd, port=port, host=host)
    
    def get(self, request):
        try :
            with self.conn.cursor() as cur:
                cur.execute('''
                    SELECT episode_nb, title, director, producer, release_date FROM {table_name}
                '''.format(table_name=TABLE_NAME)
                )
                rows = cur.fetchall()
                cur.close()
                self.conn.close()
        except Exception:
            print('No data available.')
        return render(request, 'ex04/display.html', {'rows': rows})

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
user = os.getenv('DB_USER')
port = os.getenv('DB_PORT')
host = os.getenv('DB_HOST')

TABLE_NAME = 'ex04_movies'
class Remove(View):
    template = 'ex04/remove.html'
    def get(self, request):
        try:
            conn = psycopg2.connect(database=name, user=user, password=pwd, port=port, host=host)
            # Establish the connection
            with conn.cursor() as cur:
                try:
                    cur.execute(f'''SELECT * FROM {TABLE_NAME};''')
                    movies = cur.fetchall()
                except psycopg2.DatabaseError as e:
                    return HttpResponse(f'Error: {e}')
                finally:
                    cur.close()
                    conn.close()
            # Prepare choices for the form
            choices = [(movie[1], movie[1]) for movie in movies]
            context = {'form': RemoveForm(choices)}
            return render(request, self.template, context)
        except Exception:
            return HttpResponse('No data available')

    def post(self, request):
        try:
            conn = psycopg2.connect(database=name, user=user, password=pwd, port=port, host=host)
            with conn.cursor() as cur:
                try:
                    cur.execute(f'''SELECT title FROM {TABLE_NAME};''')
                    movies = cur.fetchall()
                except psycopg2.DatabaseError as e:
                    return HttpResponse(f'Error: {e}')
            choices = [(movie[0], movie[0]) for movie in movies]
        except Exception as e:
            print(f'Error fetching data: {e}')

        data = RemoveForm(choices, request.POST)
        if data.is_valid():
            with conn.cursor() as cur:
                try:
                    cur.execute(f'''
                        DELETE FROM {TABLE_NAME} WHERE title = '{data.cleaned_data['title']}';
                    ''')
                    conn.commit()
                except psycopg2.DatabaseError as e:
                    print(f'Error: {e}')
                finally:
                    cur.close()
                    conn.close()
                return redirect(request.path)

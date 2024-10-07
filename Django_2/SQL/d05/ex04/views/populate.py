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
movies = [
                {
                    'episode_nb': '1',
                    'title': 'The Phantom Menace',
                    'director': 'George Lucas',
                    'producer': 'Rick McCallum',
                    'release_date': '1999-05-19' 
                },
                {
                    'episode_nb': '2',
                    'title': 'Attack of the Clones',
                    'director': 'George Lucas',
                    'producer': 'Rick McCallum',
                    'release_date': '2002-05-16' 
                },
                {
                    'episode_nb': '3',
                    'title': 'Revenge of the Sith',
                    'director': 'George Lucas',
                    'producer': 'Rick McCallum',
                    'release_date': '2005-05-19' 
                },
                {
                    'episode_nb': '4',
                    'title': 'A New Hope',
                    'director': 'George Lucas',
                    'producer': 'Rick McCallum',
                    'release_date': '1977-05-25' 
                }, 
                {
                    'episode_nb': '5',
                    'title': 'The Empire Strikes Back',
                    'director': 'George Lucas',
                    'producer': 'Gary Kutz',
                    'release_date': '1980-05-17' 
                },
                {
                    'episode_nb': '6',
                    'title': 'Return of the Jedi',
                    'director': 'Richard Marquand',
                    'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
                    'release_date': '1983-05-25' 
                },
                {
                    'episode_nb': '7',
                    'title': 'The Force Awakens',
                    'director': 'J.J. Abrams ',
                    'producer': 'Kathleen Kennedy, J.J. Abrams, Bryan Burk',
                    'release_date': '2015-12-11' 
                }
            ]

class Populate(View):
    conn = psycopg2.connect(database=name, password=pwd, port=port, host=host)
    
    def get(self, request):
        try:
            ret = []
            INSERT_INTO = '''
                INSERT INTO {table_name} (
                                episode_nb, 
                                title, 
                                director, 
                                producer, 
                                release_date
                            ) VALUES (
                                %s, %s, %s, %s, %s
                            )
                '''.format(table_name=TABLE_NAME)
            with self.conn.cursor() as cur:
                for movie in movies:
                    try:
                        cur.execute(
                            INSERT_INTO, [
                                movie['episode_nb'],
                                movie['title'],
                                movie['director'],
                                movie['producer'],
                                movie['release_date']
                            ]
                        )
                        self.conn.commit()
                        ret.append('OK')
                    except psycopg2.DatabaseError as e:
                        self.conn.rollback()
                        ret.append(f'{e}')
                cur.close()
                self.conn.close()
        except Exception as e:
            return HttpResponse(f'{e}')
        return HttpResponse('</br>'.join(str(i) for i in ret))

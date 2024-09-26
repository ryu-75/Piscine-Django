# Step to follow for created a django project 

1. *source my_script.sh*

2. *django-admin startproject **PROJECT_NAME***

3. Connect to the server at first, then, disconnect with **CTRL-C** => *python manage.py **runserver***

4. Do a migration => *python manage.py **migrate***

5. Restart the server => *python manage.py **runserver***

6. Create an app: 
    1. To create an app, run => *python manage.py startapp **name-pages***
    2. In *setting.py*, added in **INSTALLED_APPS** at the end of the table your new page wish is **name-pages** here
    3. Now, if we want to displayed our first *Hello World* with Django. Go back in **name-pages** folder and create a new *views.py* with :
    ```py
    # pages/views.py
    from django.http import HttpResponse

    def home_page_view(request):
        return HttpResponse("Hello, World!")
    ```
7. It's time to configure a related URL:
    1. Create a new file called *urls.py* within the **name-pages*
    ```py
        # pages/urls.py
        from django.urls import path

        from .views import home_page_view

        urlpatterns = [
            path("", home_page_view),
        ]
    ```
    - Our URL pattern here has two parts:
        - the route itself, here defined by the empty string, ""
        - a reference to the view home_page_view
8. Then, for finished. We need to updated *urls.py* from your main directory containing your project:
    Added the new lines as below:
    ```py
        # django_project/urls.py
        from django.contrib import admin
        from django.urls import path, include  # new    

        urlpatterns = [
            path("admin/", admin.site.urls),
            path("", include("pages.urls")),  # new
        
        ]
    ```

> 🔗  https://djangoforbeginners.com/hello-world/
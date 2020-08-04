open vs-code and open terminal
pip install django
add django extension in vs-code

django-admin startproject sampleProject

go to sampleProject and open vs-code again

python manage.py runserver

to create app within projects - python manage.py startapp home

create urls.py file in home(app)

import include
path('', include('home.urls'))
 ^-- this is to redirect to home(app)

from home import views
urlpatterns = [
    path("", views.example, name='home'),
]
 ^-- this is redirect to method defined in views.py

def example(request):
    return HttpResponse("this is sample page")

for admin table
python manage.py makemigrations
python manage.py migrate
-------------------------------------------------------------------------
to create superuser
python manage.py createsuperuser

to change "django adminitration"
-------------------------------------------------------------------------
-------------------------------------------------------------------------
in form-

<form method="post" action="">
{% csrf_token %}
-------------------------------------------------------------------------
go to models.py
create class

class Contact(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    date = models.DateField()

--------------------------------------------------------------------------
go to admin.py and register model
from home.models import Contact

admin.site.register(Contact)

and go to apps.py and copy class name and go to settings
INSTALLED_APPS = [
    'home.apps.HomeConfig',

then
python manage.py makemigrations
python manage.py migrate
-------------------------------------------------------------------------
go to views.py
from home.models import Contact




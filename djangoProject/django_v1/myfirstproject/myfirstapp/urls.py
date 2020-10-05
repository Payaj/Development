
"""
This is the page we created later, we won't have to register all the url of our app one by one in project.
Instead, we can just provide this files path in project's urls.py and it'll will fetch all the path one by one.
"""

from django.urls import path
from myfirstapp import views

urlpatterns = [
    path('home/', views.home),
    path('', views.landingPage),
    path('contact_us/', views.contactUs, name = 'contact_us'),
    path('register/',views.registration, name = 'registration'),
    path('show/',views.show, name = 'Show'),
    path('delete/<str:email>',views.deleteRow, name = 'delete'),
    path('api/',views.Logins.as_view()),
]

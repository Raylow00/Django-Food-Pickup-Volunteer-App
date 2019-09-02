from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('details/<event_id>', views.details, name='details'),
    path('form/<details_id>', views.form, name='form'),
    path('register/<event_name>', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('accounts/login', views.login, name='login'),
    path('addEvent/', views.addEvent, name='addEvent'),
    path('add/', views.add, name='add'),
    path('profile/', views.profile, name='profile'),
    path('delete/<id>', views.delete, name='delete'),
    path('deleteEvent/<id>', views.deleteEvent, name='deleteEvent'),
    path('updateEvent/<id>', views.updateEvent, name='updateEvent'),
    path('update/<id>', views.update, name='update'),
    path('complete/<id>/<username>', views.markComplete, name='markComplete'),
]

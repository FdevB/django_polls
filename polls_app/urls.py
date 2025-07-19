from django.urls import path

from polls_app import views


app_name = 'polls'
urlpatterns = [
    path("", views.say_hello_view, name="polls"),
]
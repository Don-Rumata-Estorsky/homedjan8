


from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('', views.task_list, name='task_list'),  

    path('task/create/', views.task_create, name='task_create'),  

]




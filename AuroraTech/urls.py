"""
URL configuration for AuroraTech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('task_list', views.Todolist_View),
    path('category', views.Category_View),
    path('task/add', views.add_task, name='add_task'),
    path('category/add', views.add_category, name='add_category'),

    path('/<int:id>/remove', views.remove_task, name='remove_task'),
    path('/<int:id>/remove_cat', views.remove_category, name='remove_category'),

    path('/<int:id_task>/<int:id_status>/status',
         views.change_status, name='change_status'),
    path('task/<int:id>/edit', views.edit_task, name='edit_task'),
    path('category/<int:id>/edit', views.edit_category, name='edit_category'),
]

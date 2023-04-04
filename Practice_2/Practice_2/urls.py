from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('formpage/', views.form_name_view, name='form_name'),
]

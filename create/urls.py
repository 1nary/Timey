from django.urls import path
from create import views

urlpatterns = [
  path('', views.index, name='index'),
  path('edit/<int:num>', views.edit, name='edit'),
  path('delete/<int:num>', views.delete, name='delete'),
]
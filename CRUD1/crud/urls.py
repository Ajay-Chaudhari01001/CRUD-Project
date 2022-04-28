from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_show, name="addanShow"),
    path('delete/<int:id>/', views.deleteData, name="deletedata"),
    path('<int:id>/', views.updateData, name="updatedata"),
]

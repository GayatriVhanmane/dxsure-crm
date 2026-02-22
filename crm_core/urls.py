from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/edit/<int:pk>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:pk>/', views.delete_client, name='delete_client'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:pk>/', views.delete_employee, name='delete_employee'),
]
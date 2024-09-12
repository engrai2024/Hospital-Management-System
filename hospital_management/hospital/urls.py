from django.urls import path

from . import views

urlpatterns = [
         path('', views.home, name='home'),
         path('doctors/', views.doctor_list, name='doctor_list'),
         path('patients/', views.patient_list, name='patient_list'),
         path('appointments/', views.appointment_list, name='appointment_list'),

         # Other URL patterns

         path('', views.home, name='home'),
         path('management-system/', views.management_system, name='management_system'),
]

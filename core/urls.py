from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'), # Log in
    path('logout/', views.logout_view, name='logout'),# Log out
    path('register/', views.register, name='register'), # registering new doctors(users)
    path('clients/register/', views.register_client, name='register_client'), # registering new clients 
    path('clients/', views.client_list, name='client_list'), # viewing the list of clients
    path('clients/<int:pk>/', views.client_profile, name='client_profile'), # viewing clients profile
    path('clients/<int:pk>/edit/', views.edit_client, name='edit_client'), # editing clients information
    path('clients/<int:pk>/delete/', views.delete_client, name='delete_client'),# delete clients
    path('clients/<int:pk>/enroll/', views.enroll_client, name='enroll_client'),# Enrolling clients to a program
    path('program/create/', views.create_program, name='create_program'),  # New path for creating program
    path('programs/', views.program_list, name='program_list'),  # For listing all programs
    path('program/<int:pk>/edit/', views.edit_program, name='edit_program'),  # Edit Program URL
    path('program/<int:pk>/delete/', views.delete_program, name='delete_program'),  # Delete Program URL
    path('api/clients/<int:pk>/', views.ClientProfileAPIView.as_view(), name='client_profile_api'),  # API url

]





from django.urls import path
from . import views
from .views import login_view, ticket_form, get_mobile, ticket_reports, update_ticket_status

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_agent, name='create_agent'),
    path('agent_created/', views.agent_created, name='agent_created'),
    path('account-details/', views.email_template, name='account_details'),
    path('login/', login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('register/', views.register_user, name='register_user'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('signin/', login_view, name='signin'),
    path('ticket/', ticket_form, name='ticket_form'),
    path('ticket/success/', views.ticket_success, name='ticket_success'),
    path('get_mobile/', get_mobile, name='get_mobile'),
    path('ticket-reports/', ticket_reports, name='ticket_reports'),
    path('tickets/', views.ticket_listing, name='ticket_listing'),
    path('tickets/<int:ticket_id>/update_status/', update_ticket_status, name='update_ticket_status'),


]




from django.conf.urls import url
from django.urls import path 
from myhealth import views

app_name = 'myhealth'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_profile/', views.patient_profile, name='patient_profile'),

    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),

    path('admin_register/', views.admin_register, name='admin_register'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),

    path('patient_list/', views.patient_list, name='patient_list'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),

    path('create_record/', views.create_record, name= 'create_record'),
    path('record_list/', views.allowed_records, name='record_list'),
    path('record_list/record/<int:pk>/', views.get_record, name='record_detail'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('appointment/<int:id>/delete/', views.appointment_delete,name='appointment_delete'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),   
    path('book_appointment/<int:id>/', views.appointment_book,name='appointment_book'), 
    path('patient_appointment/', views.patient_appointment,name='patient_appointment'),
    path('doctor_appointment/', views.doctor_appointment,name='doctor_appointment'),
    path('appointments/', views.appointments,name='appointments'),
    path('appointments/<int:id>/delete/', views.appointments_delete, name='appointments_delete'),

    path('forum/', views.forum, name='forum'),
    path('search/', views.search, name='search'),
    path('create_post/', views.post_create, name='post_create'),
    path('post/<int:id>/', views.post, name='post_detail'),
    path('post/<int:id>/update/', views.post_update, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),




    # path('appointment/<int:id>/update/', views.appointment_update,name='appointment_update'),


]
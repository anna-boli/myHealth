"""myhealth_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from myhealth import views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# for MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('myhealth/', include('myhealth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='myhealth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myhealth/logout.html'), name='logout'),

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
    path('appointments/<int:id>/delete/', views.appointments_delete,name='appointments_delete'),
    
    path('forum/', views.forum, name='forum'),
    path('search/', views.search, name='search'),
    path('create_post/', views.post_create, name='post_create'),
    path('post/<int:id>/', views.post, name='post_detail'),
    path('post/<int:id>/update/', views.post_update, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),



    # path('appointment/<int:id>/update/', views.appointment_update,name='appointment_update'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

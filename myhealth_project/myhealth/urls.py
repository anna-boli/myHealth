from django.urls import path
from myhealth import views

app_name = "myhealth"

urlpatterns = [
    path("", views.index, name="index"),
    path("forum/", views.forum, name="forum"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    
]

from django.conf.urls import url
from django.urls import path 
from myhealth import views
# from myhealth.views import ForumView
# from myhealth.views import QuestionDetailView
# from myhealth.views import QuestionCreateView
# from myhealth.views import QuestionUpdateView
# from myhealth.views import QuestionDeleteView

app_name = 'myhealth'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_profile/', views.patient_profile, name='patient_profile'),
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
    path('create_record/', views.create_record, name= 'create_record'),
    path('record_list/', views.allowed_records, name='record_list'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),   
    path('update/<int:id>/', views.appointment_book,name='appointment_update'), 
    path('patient_appointment/', views.patient_appointment,name='patient_appointment'),
    path('doctor_appointment/', views.doctor_appointment,name='doctor_appointment'),
    path('forum/', views.forum, name='forum'),
    path('search/', views.search, name='search'),
    path('create_post/', views.post_create, name='post_create'),
    path('post/<int:id>/', views.post, name='post_detail'),
    path('post/<int:id>/update/', views.post_update, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),



    # path('forum/', ForumView.as_view(), name='forum'),
    # path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    # path('question/new/', QuestionCreateView.as_view(), name='create_question'),
    # path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question_update'),
    # path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    # path('reply/<int:question_id>/', views.post_reply, name='post_reply'),
]
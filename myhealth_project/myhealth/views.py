from django.http import HttpResponse
from django.urls import reverse
from django.utils import formats
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from myhealth.forms import PatientForm, PatientProfileForm
from myhealth.forms import DoctorForm, DoctorProfileForm
from myhealth.forms import UserUpadteForm
from myhealth.models import PatientProfile, DoctorProfile
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import settings
from myhealth.models import User
from myhealth.models import Record
from myhealth.forms import RecordCreationForm
from myhealth.models import Appointment
from myhealth.forms import AppointCreationForm
from myhealth.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from myhealth.forms import PostForm, ReplyForm
# from django.views.generic import ListView
# from django.views.generic import DetailView
# from django.views.generic import CreateView
# from django.views.generic import UpdateView
# from django.views.generic import DeleteView
# from myhealth.models import Question
# from myhealth.forms import PostQuestionForm
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import UserPassesTestMixin
# from myhealth.forms import ReplyForm


# home page for all users
def home(request):
    context_dict={}
    return render(request, 'myhealth/home.html', context=context_dict)



# patient registration
def patient_register(request):
# A boolean value for telling the template whether the registration was successful.
# Set to False initially. 
# Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        user_form = PatientForm(request.POST)
        profile_form = PatientProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            email = user_form.cleaned_data.get('email')
            messages.success(request, f'The account has been created and you can login now.')
            # go to login page 
            return redirect('login')
    else:
        user_form = PatientForm()
        profile_form = PatientProfileForm()
    return render(request, "myhealth/patientRegister.html", {'user_form': user_form, 'profile_form': profile_form})



# doctor registration
def doctor_register(request):

    registered = False

    if request.method == 'POST':
        user_form = DoctorForm(request.POST)
        profile_form = DoctorProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            email = user_form.cleaned_data.get('email')
            messages.success(request, f'The account has been created and you can login now.')
            return redirect('login')
    else:
        user_form = DoctorForm()
        profile_form = DoctorProfileForm()
    return render(request, "myhealth/doctorRegister.html", {'user_form': user_form, 'profile_form': profile_form})



# the patient profile page after login for updating the information
@login_required
def patient_profile(request):
    if request.method == 'POST':
        u_form = UserUpadteForm(request.POST, instance=request.user)
        p_form = PatientProfileForm(request.POST, request.FILES, instance=request.user.patientprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'The account has been updated.')
            return redirect('patient_profile')

    else:
        u_form = UserUpadteForm(instance=request.user)
        p_form = PatientProfileForm(instance=request.user.patientprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'myhealth/patientProfile.html',context)



# the doctor profile page after login for updating the information
@login_required
def doctor_profile(request):
    if request.method == 'POST':
        u_form = UserUpadteForm(request.POST, instance=request.user)
        p_form = DoctorProfileForm(request.POST, request.FILES, instance=request.user.doctorprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'The account has been updated.')
            return redirect('doctor_profile')

    else:
        u_form = UserUpadteForm(instance=request.user)
        p_form = DoctorProfileForm(instance=request.user.doctorprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'myhealth/doctorProfile.html',context)


 
# doctors to create records
@login_required
def create_record(request):   
    context_dict = {}
    patients= PatientProfile.objects.all()
    context_dict['patientinfo'] = patients
    context_dict['record_form'] = RecordCreationForm()

    if request.method == 'POST':
        record_form = RecordCreationForm(request.POST)

        if record_form.is_valid():
            record = record_form.save(commit=False)
            record.patient = User.objects.get(GPNO=record_form.cleaned_data['GPNO'])
            record.creator = DoctorProfile.objects.get(staffID=request.user.doctorprofile.staffID)
            record.doctor_email =User.objects.get(email=request.user.email)
            record.save()
            record.allowed_users.add(User.objects.get(GPNO=record_form.cleaned_data['GPNO']))
            record.allowed_users.add(User.objects.get(email=request.user.email))
            record.save()

            messages.success(request, f'This patient record has created.')
            return redirect("record_list")
    else:
        record_form = RecordCreationForm()

    return render(request, "myhealth/createRecord.html", context=context_dict)



# show the records history to allowed users
@login_required
def allowed_records(request):
    return render(request,"myhealth/recordList.html")



# show all the patients
@login_required
def patient_list(request):
    context_dict = {
        'patientlists': PatientProfile.objects.all()
    }
    return render(request, "myhealth/patientList.html", context=context_dict)



# show all the doctors
@login_required
def doctor_list(request):
    context_dict = {
        'doctorlists': DoctorProfile.objects.all()
    }
    return render(request, "myhealth/doctorList.html", context=context_dict)



#  doctors create valid appointment for patient to select
@login_required
def create_appointment(request):
    context_dict = {}
    appoints= Appointment.objects.all().filter(user=request.user)
    context_dict['appoints'] = appoints
    context_dict['appointment_form'] = AppointCreationForm()
    if request.method == 'POST':
        appointment_form = AppointCreationForm(request.POST)

        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = User.objects.get(email=request.user.email)
            appointment.date = request.POST['date']
            appointment.time_start = request.POST['time_start']
            appointment.time_end = request.POST['time_end']
            appointment.save()

            messages.success(request, f'This appointment has created.')
            return redirect("create_appointment")
    else:
        appointment_form = AppointCreationForm()


    return render(request, "myhealth/createAppointment.html", context=context_dict)



# patients select/make an appointment
@login_required 
def make_appointment(request):
    context_dict = {}
    appointment_list= Appointment.objects.all()
    context_dict['appoints'] = appointment_list
    return render(request, "myhealth/makeAppointment.html", context=context_dict )



# get appointment id for patient to book
@login_required
def appointment_book(request, id):#activate after clicking book now button
    name=request.user.get_user()
    single_appointment= Appointment.objects.get(id=id)
    form = single_appointment
    form.appointment_with=name
    form.save()
    messages.success(request, f'You have booked successfully.')
    return redirect("patient_appointment")

# display all the appointments made by this patient
@login_required
def patient_appointment(request):
    context_dict = {}
    name=request.user.get_user()
    appointment_list = Appointment.objects.all().order_by("-id").filter(appointment_with=name)
    context_dict['appoints'] = appointment_list
    return render(request, "myhealth/patientAppointment.html", context=context_dict )


# display all booked appointments for the doctor
@login_required
def doctor_appointment(request):
    context_dict = {}
    name=request.user.get_user()
    appointment_list = Appointment.objects.all().order_by("-id").filter(user=request.user)
    context_dict['appoints'] = appointment_list
    return render(request, "myhealth/doctorAppointment.html", context=context_dict )


# quick search the target post
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, "myhealth/searchPost.html", context)


# forum for doctor-customer communication
def forum(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,4)
    page_request_var ='page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset':paginated_queryset,
        'page_request_var':page_request_var
    }
    return render(request, "myhealth/forum.html", context)


# post and reply with the forum
def post(request, id):
    post = get_object_or_404(Post, id=id)
    reply_form = ReplyForm(request.POST or None)
    if request.method =='POST':
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.post =post
            reply.save()
            return redirect(reverse("post_detail", kwargs={
                'id':post.pk
            }))
    
    context ={
        'reply_form':reply_form,
        'post':post
    }

    return render(request,"myhealth/postDetail.html",context)


# create a post for patient to ask question
def post_create(request):
    title ='Create'
    post_form = PostForm(request.POST or None)
    if request.method =='POST':
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.featured = True
            post.save()
            return redirect(reverse("post_detail", kwargs={
                'id':post_form.instance.id
            }))

    context ={
        'title':title,
        'post_form':post_form
    }

    return render(request, "myhealth/createPost.html", context)


# update the post
def post_update(request,id):
    title ='Update'
    post = get_object_or_404(Post, id=id)
    post_form = PostForm(request.POST or None, instance=post)
    if request.method =='POST':
        if post_form.is_valid():
            post_form.instance.author = request.user
            post.save()
            return redirect(reverse("post_detail", kwargs={
                'id':post_form.instance.id
            }))

    context ={
        'title':title,
        'post_form':post_form
    }

    return render(request, "myhealth/createPost.html", context)


# delete the post
def post_delete(request,id):
    title ='Delete'
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        post.delete()
        messages.success(request, f'This post has been delete.')
        return redirect(reverse("forum"))
    context ={
        'title':title,
        'object':post
    }
    
    return render(request, "myhealth/deletePost.html", context)

#  post = get_object_or_404(Post, id=id)
#  post.delete()
#  return redirect(reverse("forum"))

from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from myhealth.models import Question
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from myhealth.forms import UserRegisterForm


# Index with short discription and buttons
def index(request):
    context_dict = {}
    return render(request, "myhealth/index.html", context=context_dict)

def forum(request):
    context_dict = {
        'title': 'forum',
        'questions': Question.objects.all()
    }
    return render(request, "myhealth/forum.html", context=context_dict)

def register(request):
# A boolean value for telling the template whether the registration was successful.
# Set to False initially. 
# Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
            username = form.cleaned_data.get('username')
            messages.success(request, f'The account has been created and you can login now.')
            return redirect(reverse("login"))
    else:
        form = UserRegisterForm()
    return render(request, "myhealth/register.html", {'form': form, 'title': 'register'})

@login_required
def profile(request):

    return render(request, 'myhealth/profile.html')
    



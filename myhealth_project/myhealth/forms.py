from django import forms
from django.contrib.auth.forms import UserCreationForm
from myhealth.models import PatientProfile, DoctorProfile, AdminProfile
from django.contrib.auth import get_user_model
from myhealth.models import Record
from myhealth.models import Appointment
from myhealth.models import Post
from myhealth.models import Reply


#  patient registration form
class PatientForm(UserCreationForm):
    email = forms.EmailField(required=True)
    GPNO = forms.CharField(label='GP number',help_text='Please enter the vaild number', max_length=10,required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email','password1','password2','GPNO','first_name','last_name',)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)


#  doctor registration form
class DoctorForm(UserCreationForm):
    email = forms.EmailField(required=True)
    GPNO = forms.CharField(label='GP number',help_text='Please enter the vaild number', max_length=10,required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email','password1','password2','GPNO','first_name','last_name',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)


#  administrator registration form
class AdminForm(UserCreationForm):
    email = forms.EmailField(required=True)
    GPNO = forms.CharField(label='GP number',help_text='Please enter the vaild number', max_length=10,required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email','password1','password2','GPNO','first_name','last_name',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)


#  user update information
class UserUpadteForm(forms.ModelForm):
    email = forms.EmailField()
    GPNO = forms.CharField(label='GP number', max_length=10,required=True, widget = forms.TextInput(attrs={'readonly':'readonly'}))
    first_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'readonly':'readonly'}))
    last_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = get_user_model()
        fields = ('email','GPNO','first_name','last_name',)


#  update the patient's profile form
class PatientProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        (0, '------------'),
        (1, 'female'),
        (2, 'male'),

    )
    gender = forms.IntegerField(widget=forms.Select(choices=GENDER_CHOICES))
    birth = forms.DateField(label='D.O.B', input_formats=['%Y-%m-%d'], help_text='Please enter the format with "YYYY-MM-DD"')
    address = forms.CharField(label='Address',max_length=255, help_text='Please enter a valid address')
    tel = forms.CharField(max_length=20, label='Telephone', help_text='Please enter a valid phone number')

    class Meta:
        model = PatientProfile
        fields = ('gender','birth','address','tel','image',)


#  update the doctor's profile form
class DoctorProfileForm(forms.ModelForm):
    staffID = forms.CharField(label='ID',help_text='Please enter the vaild number', max_length=10)

    GENDER_CHOICES = (
        (0, '------------'),
        (1, 'female'),
        (2, 'male'),

    )
    gender = forms.IntegerField(widget=forms.Select(choices=GENDER_CHOICES))
    birth = forms.DateField(label='D.O.B', input_formats=['%Y-%m-%d'], help_text='Please enter the format with "YYYY-MM-DD"')
    address = forms.CharField(label='Personal Address',max_length=255, help_text='Please enter the personal address')
    work_address = forms.CharField(label='Work Address', max_length=255, help_text='Please enter the work address')
    tel = forms.CharField(max_length=20, label='Telephone', help_text='Please enter an valid phone number')
    direction = forms.CharField(max_length=255, label='Main direction', help_text='Please enter your main direction')
    description = forms.CharField(max_length=255, label='Personal description', help_text='Please enter short self description')

    class Meta:
        model = DoctorProfile
        fields = ('staffID','gender','birth','address','work_address','tel','direction','description','image',)



#  update the administrator's profile form
class AdminProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        (0, '------------'),
        (1, 'female'),
        (2, 'male'),

    )
    gender = forms.IntegerField(widget=forms.Select(choices=GENDER_CHOICES))
    birth = forms.DateField(label='D.O.B', input_formats=['%Y-%m-%d'], help_text='Please enter the format with "YYYY-MM-DD"')
    address = forms.CharField(label='Personal Address',max_length=255, help_text='Please enter the personal address')
    work_address = forms.CharField(label='Work Address', max_length=255, help_text='Please enter the work address')
    tel = forms.CharField(max_length=20, label='Telephone', help_text='Please enter an valid phone number')

    class Meta:
        model = AdminProfile
        fields = ('gender','birth','address','work_address','tel','image',)


#  patient record form
class RecordCreationForm(forms.ModelForm):
    GPNO = forms.CharField(label='Patient GPNO',help_text='Please enter this patient GP number', max_length=10)
    sympton = forms.CharField(max_length=500, widget=forms.Textarea())
    treatment = forms.CharField(max_length=500, widget=forms.Textarea())
    prescription = forms.CharField(max_length=500, widget=forms.Textarea())
    
    class Meta:
        model = Record
        fields = ('GPNO','sympton','treatment','prescription',)


#  appointment creation by doctor
class AppointCreationForm(forms.ModelForm):
    
    class Meta:
        model=Appointment
        fields=("date","time_start","time_end",)


#  post a question
class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ("title","content",)

#  reply
class ReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type your reply',
        'rows':'4'
    }))

    class Meta:
        model = Reply
        fields = ("content",)
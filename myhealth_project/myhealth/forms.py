from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Form for user registration
class UserRegisterForm(UserCreationForm):
    USERTYPE = (
        ('0', '----------'),
        ('1', 'Patient'),
        ('2', 'Doctor'),
        ('3', 'Administrator'),
        ('4', 'IT staff')
    )

    GENDER = (
        ('0', '----------'),
        ('1', 'Male'),
        ('2', 'Female')
    )

    
    email = forms.EmailField(label='Email')
    usertype = forms.ChoiceField(label='User Type', widget=forms.Select(), choices=USERTYPE,initial=USERTYPE[0]) 
    GPNo = forms.IntegerField(label='GP Number')
    firstname = forms.CharField(label='First Name', max_length=30)
    secondname = forms.CharField(label='Second Name', max_length=30)
    gender = forms.ChoiceField(label='Gender', widget=forms.Select(), choices=GENDER, initial=GENDER[0]) 
    birth = forms.DateField(label='Date of Birth', widget = forms.SelectDateWidget(years = range(2020, 1930, -1)))
    address = forms.CharField(label='Address', max_length=255)
    telephone = forms.IntegerField(label='Telephone')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'usertype',
            'GPNo',
            'firstname',
            'secondname',
            'gender',
            'birth',
            'address',
            'telephone'
        ]


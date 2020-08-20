from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse


# custom manage user model
class UserManager(BaseUserManager):

    def _create_user(self, email, password, GPNO, first_name, last_name, is_staff, is_superuser, is_patient, is_doctor, is_admin, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            GPNO=GPNO,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_patient=is_patient,
            is_doctor=is_doctor,
            is_admin=is_admin,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, GPNO=None, first_name=None, last_name=None, **extra_fields):
        return self._create_user(email, password, GPNO, first_name, last_name, False, False, False, False, False, **extra_fields)

    def create_superuser(self, email, password, GPNO, first_name, last_name, **extra_fields):
        user = self._create_user(email, password, GPNO, first_name, last_name, True, True, False, False, False, **extra_fields)
        user.save(using=self._db)
        return user


# custom user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    GPNO = models.CharField(max_length=10, default='', unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['GPNO','first_name','last_name']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email

    def get_gpno(self):
        return self.GPNO

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def get_user(self):
        return self.first_name +"  "+self.last_name+" (GPNO: " +self.GPNO + ")"

    def get_patient_type(self):
        return self.is_patient
    
    def get_doctor_type(self):
        return self.is_doctor


# information about patients' profile
class PatientProfile(models.Model):
    # This line is required. Links profile to a User model instance.
    user = models.OneToOneField(get_user_model(), related_name='patientprofile', on_delete=models.CASCADE)

    GENDER_CHOICES = (
        (0, '------------'),
        (1, 'female'),
        (2, 'male'),

    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user


# information about doctors' profile
class DoctorProfile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='doctorprofile', on_delete=models.CASCADE)
    staffID = models.CharField(max_length=10, default='', unique=True)

    GENDER_CHOICES = (
        (0, '------------'),
        (1, 'female'),
        (2, 'male'),

    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    work_address = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.staffID

# information about administrators' profile
class AdminProfile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='adminprofile', on_delete=models.CASCADE)

    GENDER_CHOICES = (
        (0, '------------'),
        (1, 'female'),
        (2, 'male'),

    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    work_address = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.tel

# doctor can create patient record
class Record(models.Model):
    patient = models.ForeignKey(get_user_model(), related_name='record_patient_gpno', on_delete=models.CASCADE)
    creator = models.ForeignKey(DoctorProfile, related_name='record_doctor_id', on_delete=models.CASCADE)
    doctor_email = models.ForeignKey(get_user_model(), related_name='doctor_email', on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=60,blank=True)
    doctor_name=models.CharField(max_length=60,blank=True)
    sympton = models.TextField(null=True)
    treatment = models.TextField(null=True)
    prescription = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    allowed_users = models.ManyToManyField(get_user_model(),related_name='allowed_users')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.sympton
    
    def __str__(self):
        return self.treatment

    def __str__(self):
        return self.prescription

    def get_absolute_url(self):
        return reverse('record_detail',kwargs={
            'id':self.id
        })


# doctor-patient appointment
class Appointment(models.Model):
    user = models.ForeignKey(get_user_model(),blank=True, null=True,on_delete=models.DO_NOTHING)
    date = models.CharField(max_length=50)
    time_start = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    appointment_with=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.appointment_with


# information about patients' questions
class Post(models.Model):
    title = models.CharField(max_length=50)     
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={
            'id':self.id
        })

    def get_update_url(self):
        return reverse('post_update',kwargs={
            'id':self.id
        })

    def get_delete_url(self):
        return reverse('post_delete',kwargs={
            'id':self.id
        })

    @property
    def get_replys(self):
        return self.replys.all().order_by('-timestamp')


class Reply(models.Model):
    user = models.ForeignKey(get_user_model(),blank=True, null=True,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='replys', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    


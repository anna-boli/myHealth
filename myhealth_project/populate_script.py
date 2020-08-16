import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'myhealth_project.settings')
import django
django.setup()

import requests

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from myhealth.models import User, PatientProfile, DoctorProfile, Record, Appointment


def populate():


# Start execution here!
# populate() keeps tabs on categories that are created.
if __name__ =='__main__':
    print('Starting Myhealth population script...')
    populate()
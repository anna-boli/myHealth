from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myhealth.views import home, patient_register, doctor_register, admin_register
from myhealth.views import patient_profile, doctor_profile, admin_profile
from myhealth.views import create_record, allowed_records, get_record
from myhealth.views import patient_list, doctor_list
from myhealth.views import doctor_appointment, create_appointment, appointment_delete
from myhealth.views import patient_appointment, make_appointment, appointment_book
from myhealth.views import appointments, appointments_delete
from myhealth.views import forum, search, post, post_create, post_update, post_delete
from django.contrib.auth import views as auth_views
from myhealth.models import User
from myhealth.models import PatientProfile, DoctorProfile, AdminProfile
from myhealth.models import Record
from myhealth.models import Appointment
from myhealth.models import Post
from myhealth.models import Reply


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_patient_register_url_is_resolves(self):
        url = reverse('patient_register')
        self.assertEquals(resolve(url).func, patient_register)

    def test_doctor_register_url_is_resolves(self):
        url = reverse('doctor_register')
        self.assertEquals(resolve(url).func, doctor_register)

    def test_admin_register_url_is_resolves(self):
        url = reverse('admin_register')
        self.assertEquals(resolve(url).func, admin_register)

    def test_patient_profile_url_is_resolves(self):
        url = reverse('patient_profile')
        self.assertEquals(resolve(url).func, patient_profile)

    def test_doctor_profile_url_is_resolves(self):
        url = reverse('doctor_profile')
        self.assertEquals(resolve(url).func, doctor_profile)

    def test_admin_profile_url_is_resolves(self):
        url = reverse('admin_profile')
        self.assertEquals(resolve(url).func, admin_profile)

    def test_patient_list_url_is_resolves(self):
        url = reverse('patient_list')
        self.assertEquals(resolve(url).func, patient_list)

    def test_doctor_list_url_is_resolves(self):
        url = reverse('doctor_list')
        self.assertEquals(resolve(url).func, doctor_list)

    def test_create_record_url_is_resolves(self):
        url = reverse('create_record')
        self.assertEquals(resolve(url).func, create_record)

    def test_record_list_url_is_resolves(self):
        url = reverse('record_list')
        self.assertEquals(resolve(url).func, allowed_records)

    def test_record_detail_url_is_resolves(self):
        url = reverse('record_detail', kwargs={'id':1})
        self.assertEquals(resolve(url).func, get_record)

    def test_patient_appointment_url_is_resolves(self):
        url = reverse('patient_appointment')
        self.assertEquals(resolve(url).func, patient_appointment)

    def test_make_appointment_url_is_resolves(self):
        url = reverse('make_appointment')
        self.assertEquals(resolve(url).func, make_appointment)

    def test_doctor_appointment_url_is_resolves(self):
        url = reverse('doctor_appointment')
        self.assertEquals(resolve(url).func, doctor_appointment)

    def test_create_appointment_url_is_resolves(self):
        url = reverse('create_appointment')
        self.assertEquals(resolve(url).func, create_appointment)

    def test_appointment_delete_url_is_resolves(self):
        url = reverse('appointment_delete', kwargs={'id':1})
        self.assertEquals(resolve(url).func, appointment_delete)

    def test_appointments_url_is_resolves(self):
        url = reverse('appointments')
        self.assertEquals(resolve(url).func, appointments)

    def test_appointments_delete_url_is_resolves(self):
        url = reverse('appointments_delete', kwargs={'id':1})
        self.assertEquals(resolve(url).func, appointments_delete)

    def test_forum_url_is_resolves(self):
        url = reverse('forum')
        self.assertEquals(resolve(url).func, forum)

    def test_search_url_is_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_post_create_url_is_resolves(self):
        url = reverse('post_create')
        self.assertEquals(resolve(url).func, post_create)

    def test_post_url_is_resolves(self):
        url = reverse('post_detail', kwargs={'id':1})
        self.assertEquals(resolve(url).func, post)

    def test_post_update_url_is_resolves(self):
        url = reverse('post_update', kwargs={'id':1})
        self.assertEquals(resolve(url).func, post_update)

    def test_post_delete_url_is_resolves(self):
        url = reverse('post_delete', kwargs={'id':1})
        self.assertEquals(resolve(url).func, post_delete)

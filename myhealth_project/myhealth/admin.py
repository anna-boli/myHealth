from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myhealth.models import User, user_type
from myhealth.models import PatientProfile,DoctorProfile,AdminProfile
from myhealth.models import Record
from myhealth.models import Appointment
from myhealth.models import Post
from myhealth.models import Reply

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('GPNO','email', 'password', 'first_name', 'last_name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_patient',
            'is_doctor',
            'is_admin',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('GPNO','email', 'first_name', 'last_name', 'is_staff','is_superuser', 'is_patient', 'is_doctor', 'is_admin', 'last_login')
    list_filter = ('is_staff', 'is_superuser','is_patient', 'is_doctor', 'is_admin', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birth', 'address', 'tel', 'image')
admin.site.register(PatientProfile,PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'staffID', 'gender', 'birth', 'address', 'work_address', 'tel', 'direction', 'description', 'image')
admin.site.register(DoctorProfile,DoctorAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birth', 'address', 'work_address', 'tel', 'image')
admin.site.register(AdminProfile,AdminAdmin)

admin.site.register(user_type)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('patient','creator','sympton', 'treatment', 'prescription', 'date_created')
admin.site.register(Record, RecordAdmin)

class AppointAdmin(admin.ModelAdmin):
    list_display = ('user','date', 'time_start','time_end','appointment_with')
admin.site.register(Appointment, AppointAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','timestamp','author','featured')
admin.site.register(Post, PostAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'content','timestamp','post')
admin.site.register(Reply, ReplyAdmin)



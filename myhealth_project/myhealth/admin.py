from django.contrib import admin
from myhealth.models import Question
from myhealth.models import Profile

# Register all models to admin
admin.site.register(Question)
admin.site.register(Profile)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Information about patients' questions
class Question(models.Model):
    CHAR_MAX_LENGTH = 100
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=CHAR_MAX_LENGTH)
    content = models.TextField()

    def __str__(self):
        return self.title

# Information about patients' profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    


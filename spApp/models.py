from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
class All_App(models.Model):
 class Meta:
    verbose_name_plural ='All_App'
 def __str__(self):
    return self.All_App
 

fs = FileSystemStorage(location='uploads/') 
from django.contrib.auth.models import User

class CourseTbl(models.Model):
    # Your existing course model fields
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=40)
    overview = models.TextField(default=' ')
    content = models.TextField(default=' ')
    duration = models.TextField(default=' ')
    instructor = models.TextField(default=' ')
    level = models.TextField(default=' ')
    rate = models.IntegerField(default=0)
    mediaFile = models.FileField(upload_to='courseVideos/')
    image = models.ImageField(upload_to='courseImages/', storage=fs)
    user = models.TextField(default='')

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseTbl, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} - {self.course.name}'


class CourseContent(models.Model):
    course = models.ForeignKey(CourseTbl, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    content_file = models.FileField(upload_to='coursesContent/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.course.name} - {self.title}'
   




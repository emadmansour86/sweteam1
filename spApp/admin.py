from django.contrib import admin

# Register your models here.
from .models import *
#admin.site.register(All_App)
#admin.site.register(CourseTbl)


class CourseContentInline(admin.TabularInline):
    model = CourseContent
    extra = 1

class CourseTblAdmin(admin.ModelAdmin):
    inlines = [CourseContentInline]

admin.site.register(CourseTbl, CourseTblAdmin)
admin.site.register(Subscription)
admin.site.register(CourseContent)

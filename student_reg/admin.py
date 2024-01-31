from django.contrib import admin
from .models import student

# Register your models here.


class adminname(admin.ModelAdmin):
    list_display=('firstname',)
admin.site.register(student,adminname)
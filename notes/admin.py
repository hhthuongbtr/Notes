from django.contrib import admin

# Register your models here.
from .models import Subject, Note

admin.site.register(Subject)
admin.site.register(Note)


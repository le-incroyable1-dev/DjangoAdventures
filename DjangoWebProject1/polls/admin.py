from django.contrib import admin
# Register your models here.

from .models import Question

admin.site.register(Question)
# indicate that the model "Question" requires an admin interface


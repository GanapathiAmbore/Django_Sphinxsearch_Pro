from django.contrib import admin
from sphinxapp.models import Student,Question,Answer

models=[Student,Question,Answer]

admin.site.register(models)
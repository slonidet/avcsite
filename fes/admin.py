from django.contrib import admin

# Register your models here.
from .models import Experts,Materials

admin.site.register(Experts)
admin.site.register(Materials)
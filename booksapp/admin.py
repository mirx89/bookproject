from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Country)  # Admin page show Country model
admin.site.register(Language)  # Admin page show Language model
admin.site.register(Author)  # Admin page show Author model
admin.site.register(Book)  # Admin page show Book model


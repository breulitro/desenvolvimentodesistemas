from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Address)
admin.site.register(AccessCounter)

from django.contrib import admin
from .models import AdminLoginDetails, StaffDetails

# Register your models here.
admin.site.register(AdminLoginDetails)
admin.site.register(StaffDetails)
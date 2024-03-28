from django.contrib import admin
from .models import Place


# Register your models here.

admin.site.register(Place) # Admin console model
#access admin console in browser by typing '127.0.0.1:8000/admin/auth/user/'

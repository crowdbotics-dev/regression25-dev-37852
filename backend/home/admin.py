from django.contrib import admin
from .models import Addeddata, Himanshutest, Test, Usertest

admin.site.register(Test)
admin.site.register(Himanshutest)
admin.site.register(Usertest)
admin.site.register(Addeddata)

# Register your models here.

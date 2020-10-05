from django.contrib import admin
from myfirstapp.models import signup, property_type, address, Register # myfirstapp.models is models.py in myfirstapp folder. sigup, property_type, address, ... are classes (tables) in models.py

# Register your models here to see the changes on the admin portal.
admin.site.register(signup)
admin.site.register(property_type)
admin.site.register(address)
admin.site.register(Register)
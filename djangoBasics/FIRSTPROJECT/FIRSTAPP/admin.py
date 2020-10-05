from django.contrib import admin
from FIRSTAPP.models import People, ContactInfo,CallInfo

# Register your models here.
admin.site.register(People)
admin.site.register(ContactInfo)
admin.site.register(CallInfo)
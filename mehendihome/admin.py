from django.contrib import admin

# Register your models here.
from mehendihome.models import mehendi,appoinment,rangoli
admin.site.register(mehendi)
admin.site.register(rangoli)
admin.site.register(appoinment)
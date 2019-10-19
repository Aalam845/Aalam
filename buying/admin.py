from django.contrib import admin

# Register your models here.

from .models import car,house

admin.site.register(car)
admin.site.register(house)

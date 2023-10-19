from django.contrib import admin
from .models import Entry

# Register your models here.

admin.site.register(Entry) # must register to see this on the django admin site

from django.contrib import admin
from apps.translation.models import Person


# Register your models here.

# PERSON:
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

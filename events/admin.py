from django.contrib import admin
from .models import Category, Event, Participant

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Participant)
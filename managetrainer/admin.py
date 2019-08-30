from django.contrib import admin
from . models import Trainer
from .models import Batches

admin.site.register(Trainer)
admin.site.register(Batches)
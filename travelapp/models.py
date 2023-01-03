from django.db import models
from django.contrib import admin
# Create your models here.

class Materials(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField( upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class AdminMaterials(admin.ModelAdmin):
    list_display = ['name','desc']

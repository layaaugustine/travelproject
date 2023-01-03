from django.contrib import admin
from . models import Materials,AdminMaterials
# Register your models here.

admin.site.register(Materials,AdminMaterials)
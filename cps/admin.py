from django.contrib import admin
from .models import FinishGood
from .models import Componente
from .models import BOM

# Register your models here.
admin.site.register(FinishGood)
admin.site.register(BOM)
admin.site.register(Componente)
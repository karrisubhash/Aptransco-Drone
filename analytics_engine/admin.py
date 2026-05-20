from django.contrib import admin

from .models import (
    Tower,
    Inspection,
    Defect,
    Prediction
)

admin.site.register(Tower)
admin.site.register(Inspection)
admin.site.register(Defect)
admin.site.register(Prediction)
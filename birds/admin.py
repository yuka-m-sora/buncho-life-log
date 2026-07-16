from django.contrib import admin
from .models import Bird, WeightRecord, BehaviorRecord

admin.site.register(Bird)
admin.site.register(WeightRecord)
admin.site.register(BehaviorRecord)
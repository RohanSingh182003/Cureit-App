from django.contrib import admin
from .models import UserDetail , WellBeing , Psychologyadjustment  , Stress , Anxiety

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(WellBeing)
admin.site.register(Psychologyadjustment)
admin.site.register(Stress)
admin.site.register(Anxiety)


from django.contrib import admin
from .models import Letter,Recommender,Statistic,TempLetter
# Register your models here.
admin.site.register(Letter)
admin.site.register(Recommender)
admin.site.register(Statistic)
admin.site.register(TempLetter)
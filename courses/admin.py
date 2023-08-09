from django.contrib import admin
from .models import *

admin.site.register(Learner)
admin.site.register(Educator)
admin.site.register(Course)
admin.site.register(Enrollment)


from django.contrib import admin

from .models import Creator
from .models import Project
from .models import Areas


admin.site.register(Areas)
admin.site.register(Creator)
admin.site.register(Project)

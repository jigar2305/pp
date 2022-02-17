from django.contrib import admin
from .models import bugdetail,role,project,users
# Register your models here.

admin.site.register(role)
admin.site.register(users)
admin.site.register(project)
admin.site.register(bugdetail)

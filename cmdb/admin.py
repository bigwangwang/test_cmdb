from django.contrib import admin
from cmdb import models
# Register your models here.

admin.site.register(models.Host)
admin.site.register(models.Users)
admin.site.register(models.Disk)
admin.site.register(models.GroupHost)


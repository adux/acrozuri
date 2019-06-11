from django.contrib import admin
from .models import (
    Member,
    News,
    Class,
)

admin.site.register(Member)
admin.site.register(News)
admin.site.register(Class)

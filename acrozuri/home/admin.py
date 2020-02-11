from django.contrib import admin
from .models import (
    Member,
    News,
    Class,
)


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "address",
        "city",
        "phone",
        "email",
        "created",
        "paid_period"
    )


admin.site.register(Member, MemberAdmin)
admin.site.register(News)
admin.site.register(Class)

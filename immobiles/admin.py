from django.contrib import admin
from immobiles.models import Immobile

class ImmobileAdmin(admin.ModelAdmin):
    list_display = ('title', 'gender', 'kind', 'user', 'approved')
    list_filter = ('approved', 'gender', 'kind', 'user')
    ordering = ('approved',)
    search_fields = ('title', 'user__username', 'contact', 'details')


admin.site.register(Immobile, ImmobileAdmin)

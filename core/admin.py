from django.contrib import admin
from core.models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'creation_date', 'decripption')
    list_filter = ('user', 'event_date','creation_date',)


admin.site.register(Evento, EventoAdmin)
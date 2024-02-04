from django.contrib import admin
from core.models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'creation_date', 'decripption')



admin.site.register(Evento, EventoAdmin)
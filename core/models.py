from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    title = models.CharField(max_length=100)
    decripption = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.title
    
    def get_event_data(self):
        return self.event_date.strftime('%d/%m/%Y as %H: %M Hrs')
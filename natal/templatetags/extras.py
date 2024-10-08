
from django import template
register = template.Library()

@register.filter(name='ajeitaHora')
def ajeitaHora(obj):

        from datetime import time, timedelta        
        from django.utils.timezone import localtime        
        import pytz

        local_tz = pytz.timezone('Etc/GMT+1')
        
        time_str = localtime(obj.replace(tzinfo=local_tz)).strftime("%H:%M")

        return time_str


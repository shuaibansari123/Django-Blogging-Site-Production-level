
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'

    def ready(self):
        import blogapp.signals
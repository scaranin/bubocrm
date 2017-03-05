from django.apps import AppConfig
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class CustomerConfig(AppConfig):
    name = 'customer'
    verbose_name = _('Клиенты')
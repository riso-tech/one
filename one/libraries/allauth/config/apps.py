from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AllauthConfigsConfig(AppConfig):
    name = "one.libraries.allauth.config"
    verbose_name = _("Extended Allauth configs")

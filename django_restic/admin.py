from django.contrib import admin
from django.urls import path
from django.db import models

from . import views

class tcptraceroute(object):
    param1: str = "hello world"

class CustomAdminSite(admin.AdminSite):
    # def __init__(self):
    #     super().__init__()
    #     breakpoint()
    #     self._registry = admin.site._registry

    def get_urls(self):
        self._registry = admin.site._registry
        admin_urls = super().get_urls()
        custom_urls = [
            path('django_restic/', views.Restic.as_view(admin=self), name="restic_home"),
        ]
        return custom_urls + admin_urls # custom urls must be at the beginning

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": "Django Restic",
                "app_label": "django_restic",
                # "app_url": "/admin/test_view",
                "models": [
                    {
                        "name": "django_restic",
                        "object_name": "django_restic",
                        "admin_url": "/admin/django_restic/",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list

site = CustomAdminSite()



# you can register your models on this site object as usual, if needed
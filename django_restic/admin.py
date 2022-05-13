from django.contrib import admin
from django.urls import path

from . import views

class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        custom_urls = [
            path('preferences/', self.admin_view(views.my_view)),
        ]

        return custom_urls + admin.site.urls[0] # custom urls must be at the beginning


site = CustomAdminSite()



# you can register your models on this site object as usual, if needed
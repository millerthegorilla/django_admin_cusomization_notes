#import restic
from django import views
from django.shortcuts import render
from django.contrib.auth import mixins
from django.contrib.admin.views.decorators import staff_member_required

class BaseReadOnlyAdminMixin:
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

class Restic(views.generic.ListView):
    admin = {}
    def get(self, request):
        ctx = dict(self.admin.each_context(request), title='Django Restic',)
        return render(request, 'admin/restic/restic.html', ctx)

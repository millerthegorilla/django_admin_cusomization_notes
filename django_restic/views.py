import restic

from django import views, conf
from django.contrib import messages
from django.shortcuts import render, redirect

from . import restic_installer


class Restic(views.generic.ListView):
    admin = {}
    def get(self, request):
        if not restic_installer.restic_check():
            messages.add_message(request, messages.ERROR, 'Restic is not installed!.')
            return redirect('admin/')
        else:
            messages.add_message(request, messages.INFO, 'Restic is installed!.')

        try:
            repos = conf.settings.RESTIC_REPOS
        except AttributeError:
            messages.add_message(request, messages.WARNING, 'No repos are defined in settings.py')
        if not len(repos):
            messages.add_message(request, messages.WARNING, 'No repos are defined - settings.RESTIC_REPOS is empty')
        else:
            repos={}
            for repo in conf.settings.RESTIC_REPOS:
                restic.repository
                restic.snapshot
        ctx = dict(self.admin.each_context(request), title='Django Restic',)
        return render(request, 'admin/restic/restic.html', ctx)

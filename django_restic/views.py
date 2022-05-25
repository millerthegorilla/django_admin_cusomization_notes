import io, json, restic, os

from django import views, conf
from django.contrib import messages
from django.shortcuts import render, redirect

from . import restic_installer
from . import forms as restic_forms

class Restic(views.generic.ListView):
    admin = {}
    def get(self, request):
        repos = []
        repos_ctx = {}
        if not restic_installer.restic_check():
            messages.add_message(request, messages.ERROR, 'Restic is not installed!.')
            return redirect('admin/')
        else:
            messages.add_message(request, messages.INFO, 'Restic is installed!.')

        try:
            repos = conf.settings.RESTIC_REPOS
        except AttributeError:
            pass
        if not len(repos):
            messages.add_message(request, messages.WARNING, 'No repos are defined - settings.RESTIC_REPOS is empty')
        else:
            for repo in repos:
                restic.repository = repo['path']
                #restic.password_file = io.StringIO(repo['password'])
                os.environ["RESTIC_PASSWORD"] = repo['password']
                if restic.check() == None:
                    restic.init()
                    repos_ctx[repo['path']] = None
                else:
                    repos_ctx[repo['path']] = restic.snapshots(group_by='host')
                    repos_form = restic_forms.Restic(repos=repos_ctx)    
            
        ctx = dict(self.admin.each_context(request), title='Django Restic', form=repos_form)
        return render(request, 'admin/restic/restic.html', ctx)

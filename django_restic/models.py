from django.db import models


class Repos(models.Model):
	path: models.CharField = models.CharField('repo path', max_length=30, blank=True)


class Backups(models.Model):
	path: models.CharField = models.CharField('backup path', max_length=30, blank=True)
	repo: models.ForeignKey('Repos', on_delete=models.CASCADE)

	

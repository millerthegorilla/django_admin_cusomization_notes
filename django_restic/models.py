from django.db import models

# Create your models here.

class Repos(models.Model):
	repo: models.CharField = models.CharField('repo path', max_length=30, blank=True)
		
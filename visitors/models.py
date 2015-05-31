from django.db import models
from common.models import Organisation

# Create your models here.

class Annual(models.Model):
	year = models.IntegerField()
	visitors = models.IntegerField()
	organisation = models.ForeignKey('common.Organisation')

class Monthly(models.Model):
	year = models.IntegerField()
	month = models.IntegerField()
	visitors = models.IntegerField()
	organisation = models.ForeignKey('common.Organisation')

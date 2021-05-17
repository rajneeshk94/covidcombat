from django.db import models

class Examine(models.Model):
	Name = models.CharField(max_length=20, null=True, unique=True)
	temperature = models.IntegerField()
	dry_cough = models.BooleanField()
	taste = models.BooleanField()
	breathless = models.BooleanField()

	def __str__(self):
		return self.Name 

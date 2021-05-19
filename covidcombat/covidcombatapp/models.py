from django.db import models

class Examine(models.Model):
	Name = models.CharField(max_length=20, null=True, unique=True)
	temperature = models.IntegerField()
	dry_cough = models.BooleanField()
	taste = models.BooleanField()
	breathless = models.BooleanField()

	def __str__(self):
		return self.Name 


RESULT = [
		('Positive', 'Positive'),
        ('Negative', 'Negative')
    ]

OXYGEN = [
	('95 or above', '95 or above'),
    ('Below 95', 'Below 95')
]


class FinalTest(models.Model):
    
	Name = models.CharField(max_length=20, null=True, unique=True)
	test_result = models.CharField(max_length=20, null=True, choices=RESULT)
	oxygen_level = models.CharField(max_length=20, null=True, choices=OXYGEN)

	def __str__(self):
		return self.Name

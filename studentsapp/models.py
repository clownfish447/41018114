from django.db import models

class student(models.Model):
	cPhone = models.CharField(max_length=50, blank=True, default='')
	cName = models.CharField(max_length=20, null=False)
	
	def __str__(self):
		return self.cName


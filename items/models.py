from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=20, decimal_places=2)
	summary = models.TextField(default='This is cool!')
		
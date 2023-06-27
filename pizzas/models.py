from django.db import models

class Topic(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		"""Return the strign representation of the model."""
		return self.name
	
class Entry(models.Model):
	pizza = models.ForeignKey(Topic, on_delete=models.CASCADE) 
	name = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True) 

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name


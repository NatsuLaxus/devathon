from django.db import models

class VehicleStatus(models.Model):
	name = models.CharField(max_length = 128)
	vehicle_num = models.CharField(max_length = 128)
	status = models.IntegerField()

	def __str__(self):
		return self.name

class VehicleType(models.Model):
	name = models.CharField(max_length = 128)
	vehicle_num = models.CharField(max_length = 128)
	vehicle_type = models.IntegerField()
	entry_time = models.DateTimeField(null = True)
	exit_time = models.DateTimeField(null = True)

	def __str__(self):
		return self.name

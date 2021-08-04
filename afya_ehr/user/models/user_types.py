from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Practice(models.Model):
	name = models.CharField(max_length=100)
	owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
	# state


class Patient(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	practice = models.ForeignKey(Practice, on_delete=models.CASCADE)

	class Meta:
		# We can have a single patient in multiple practices
		models.UniqueConstraint(fields = ['user', 'practice'], name = 'patient_constraint')


class Relationship(models.Model):
	name = models.CharField(max_length=20)


class EmergencyContact(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=200)
	relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20)
	# One user can have up to 3 emergency contacts
	# validate this from back end


class Provider(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	npi = models.CharField(max_length=15)  # NPI is a ten digit number, validate from back end
	practice = models.ForeignKey(Practice, on_delete=models.CASCADE)

	class Meta:
		# We can have a single provider in multiple practices
		models.UniqueConstraint(fields = ['user', 'npi', 'practice'], name = 'provider_constraint')

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Sex(models.Model):
	name = models.CharField(max_length=30)


class MaritalStatus(models.Model):
	name = models.CharField(max_length=30)


class Ethnicity(models.Model):
	name = models.CharField(max_length=100)


class PersonalInformation(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
	birthdate = models.DateTimeField()
	ssn = models.CharField(max_length=15, unique=True) # social security number is 9 digits, validate from backend code
	martial_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
	ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE)


class Country(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=10)


class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=10)


class Contact(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField(max_length=345, unique=True)
	phone = models.CharField(max_length=20, unique=True)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	address_line_1 = models.CharField(max_length=100)
	address_line_2 = models.CharField(max_length=100)
	address_line_3 = models.CharField(max_length=100)

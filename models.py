from django.core.exceptions import ValidationError
import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length = 100)
	active = models.BooleanField(default=True)
	website_url = models.URLField(blank=True)
	birthday = models.DateField(blank=True, null=True)

	def clean(self):
		today = datetime.date.today()
		if self.birthday and self.birthday > today:
			raise ValidationError("Birthday cannot be in the future")

	def _unicode_(self):
		return "'{0} {1}' <{2}>".format(
			self.first_name,
			self.last_name,
			self.email
		)
	def useful_email(self):
		return '<a href="mailto:{0}">{0}</a>'.format(self.email)
	useful_email.allow_tags = True
	useful_email.admin_order_field = 'email'	
class Note(models.Model):
	contact = models.ForeignKey(Contact, related_name='notes')
	content = models.TextField()
class Phone(models.Model):
	contact = models.ForeignKey(Contact, related_name='phone')
	PHONE_CHOICE =(
		('h', 'Home_phone',),
			('m', 'Mobile_phone',),
			('o', 'Other_phone',),
			('f', 'Fax',),
			)
	choice = models.CharField(max_length=15, choices=PHONE_CHOICE)
	phone = models.CharField(max_length=10, blank=True, null=True)


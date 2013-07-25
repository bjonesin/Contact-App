from django.test import TestCase
from django.core.urlresolvers import  reverse
from .models import Contact, Note, Phone
import datetime
from django.core.exceptions import ValidationError
class ContactTests(TestCase):

	def test_list_view(self):
		response = self.client.get(reverse("contact-list"))
		self.assertEqual(response.status_code,200)
		self.assertEqual(len(response.context['contacts']), 0)

	def test_useful_email(self):
		c = Contact.objects.create(
			first_name='Bob',
			last_name="Smith",
			email='bob@smith.com',
		)
		self.assertEqual(
			c.useful_email(),
			'<a href="mailto:{0}">{0}</a>'.format(c.email)
			)
	def test_valid_birthday(self):
		today = datetime.date.today()
		last_week = today - datetime.timedelta(weeks=1)
		c = Contact.objects.create(
			first_name ="John",
			last_name='Smith',
			email='john@smith.com',
			birthday=last_week
		)
	def test_invalid_birthday(self):
		today = datetime.date.today()
		next_week = today +datetime.timedelta(weeks=1)

		with self.assertRaises(ValidationError):
			c = Contact(
				first_name='Frank',
				last_name='Smith',
				email='frank@smith.com',
				birthday=next_week,
			)
			c.clean()
	def test_list_view_active(self):
		c1 = Contact.objects.create(
			first_name='Good', last_name='Smith',
			email='good@smith.com'
		)
		c2 = Contact.objects.create(
			first_name='Bad', last_name='Smith',
			email='bad@smtih.com',
			active=False,
		)

		response = self.client.get(reverse('contact-list'))
		self.assertTrue(c1 in response.context['contacts'])
		self.assertFalse(c2 in response.context['contacts'])

	def test_detail(self):
		c = Contact.objects.create(
			first_name='Abraham',
			last_name="Lincoln",
			email='president@whitehouse.gov',
		)
		detail_url = reverse('contact-detail', kwargs={'pk':c.pk})
		response= self.client.get(detail_url)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['contact'],c)
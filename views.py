# Create your views here.
from .models import Contact

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ContactForm

@login_required
def contact_add(request):
	template_name = 'contacts/add.html'
	saved = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			saved = True
	else:
		form = ContactForm()
	return render(request, template_name, {
		'form': form,
		'saved' : saved,
		})

def my_view(request):
	#just display a template
	template_name = 'my_view.html'

	return render(request, template_name,{})

def contact_list(request):
	template_name = 'contacts/list.html'
	my_contacts = Contact.objects.filter(active=True)

	return render(request, template_name, {'contacts': my_contacts})

def contact_detail(request, pk):
	template_name = 'contacts/detail.html'
	this_contact = Contact.objects.get(pk=pk)

	return render(request, template_name, {'contact': this_contact})

	pass
	
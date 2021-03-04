from django.shortcuts import render, redirect
from .models import Contact
from django.shortcuts import get_object_or_404
from .forms import ContactForm


def contactsList(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list.html', {'contacts': contacts})


def contactsViews(request, id):
    contact = get_object_or_404(Contact, pk=id)
    return render(request, 'contacts/contacts.html', {'contact': contact})


def newContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect('/')
    else:
        form = ContactForm()
        return render(request, 'contacts/addcontact.html', {'form': form})


def editContact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact.save()
            return redirect('/')
        else:
            return render(request, 'contacts/editcontact.html', {'form': form, 'contact': contact})
    else:
        return render(request, 'contacts/editcontact.html', {'form': form, 'contact': contact})
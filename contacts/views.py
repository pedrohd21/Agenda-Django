from django.shortcuts import render, redirect
from .models import Contact
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def contactsList(request):
    search = request.GET.get('search')
    if search:
        contacts = Contact.objects.filter(name__icontains=search, user=request.user)
    else:
        contacts_list = Contact.objects.all().order_by('name').filter(user=request.user)
        paginator = Paginator(contacts_list, 10)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
    
    return render(request, 'contacts/list.html', {'contacts': contacts})


@login_required
def contactsViews(request, id):
    contact = get_object_or_404(Contact, pk=id)
    return render(request, 'contacts/contacts.html', {'contact': contact})


@login_required
def newContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('/')
    else:
        form = ContactForm()
        return render(request, 'contacts/addcontact.html', {'form': form})


@login_required
def editContact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact.save()
            messages.info(request, 'Contato editado com sucesso.')
            return redirect('/')
        else:
            return render(request, 'contacts/editcontact.html', {'form': form, 'contact': contact})
    else:
        return render(request, 'contacts/editcontact.html', {'form': form, 'contact': contact})


@login_required
def deleteContact(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact.delete()
    messages.info(request, 'Contato deletado com sucesso.')
    return redirect('/')
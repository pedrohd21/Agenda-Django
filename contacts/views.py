from django.shortcuts import render



def contactsList(request):
    return render(request, 'contacts/list.html')
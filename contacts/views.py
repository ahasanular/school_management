from django.shortcuts import render

def contactList(request):
    return render(request, 'contactList.html')
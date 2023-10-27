from django.shortcuts import render
from .models import Person

# Create your views here.

def person_list(request):
    people = Person.objects.all()
    return render(request, 'list.html', {'people': people})
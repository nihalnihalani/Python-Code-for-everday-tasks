from django.shortcuts import render

def index(request):
    return render(request, 'my_template.html')

import random
from .models import Name, ID, Contact, Address

def populate(request):
    for i in range(30):
        Name.objects.create(name='Name {}'.format(i))
        ID.objects.create(id=random.randint(1000, 9999))
        Contact.objects.create(phone_number='555-555-{}'.format(random.randint(1000, 9999)), email='user{}@example.com'.format(i))
        Address.objects.create(street_address='{} Main St
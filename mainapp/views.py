from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import random
from mainapp.models import Numbers
@login_required



def index(request):
    _num = random.randint(1,12)
    num = str(_num)
    context = {
        'page_title': 'случайный вывод числа на страницу',
        'num': num.replace(' ', ''),
    }
    return render(request, 'mainapp/index.html', context)

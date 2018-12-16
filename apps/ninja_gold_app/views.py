from django.shortcuts import render, redirect
from random import randint
from time import strftime, gmtime

datetime_format = "%b %d, %Y %I:%M %p"
def index(request):
    if 'total_gold' and 'farm_gold' and 'cave_gold' and 'house_gold' and 'casino_gold' and 'activities' not in request.session:
        request.session['total_gold']= 0,
        request.session['farm_gold']= 0,
        request.session['cave_gold']= 0,
        request.session['house_gold']= 0,
        request.session['casino_gold']= 0,
        request.session['activities']= []

    context = {
        'gold': request.session['total_gold'],
        'activities' : request.session['activities'],
        'loc_info': [
            {
                'name':'farm',
                'earn': '10 to 20',
                },
            {
                'name':'cave',
                'earn': '5 to 10',
                },
            {
                'name':'house',
                'earn': '2 to 5',
                },
            {
                'name':'casino',
                'earn': '/loses 0 to 50',
                }
            ]
    }
    return render(request, 'ninja_gold_app/index.html', context)


def process(request):
    if request.method == 'POST':
        if request.POST['location'] == 'farm':
            request.session['total_gold'] = 0
            request.session['farm_gold'] = randint(10, 20)
            request.session['total_gold'] += request.session['farm_gold']
            request.session['activities'].append(f"Earned {request.session['farm_gold']} gold from the farm!. {strftime(datetime_format,gmtime())}")
    
        elif request.POST['location'] == 'cave':
            request.session['cave_gold'] = randint(5, 10)
            request.session['total_gold'] += request.session['cave_gold']
            request.session['activities'].append(f"Earned {request.session['cave_gold']} gold from the cave!. {strftime(datetime_format,gmtime())}")
    
        elif request.POST['location'] == 'house':
            request.session['house_gold'] = randint(2, 5)
            request.session['total_gold'] += request.session['house_gold']
            request.session['activities'].append(f"Earned {request.session['house_gold']} gold from the house!. {strftime(datetime_format,gmtime())}")

        elif request.POST['location'] == 'casino':
            request.session['casino_gold'] = randint(-50, 50)
            request.session['total_gold'] += request.session['casino_gold']
            request.session['activities'].append(f"Earned {request.session['casino_gold']} gold from the casino!. {strftime(datetime_format,gmtime())}")
        else:
            return redirect('/')
    return redirect('/')


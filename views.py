from django.shortcuts import render
import json


def home(request):
    with open('data/core.json') as f:
        core_data = json.load(f)
    return render(request, 'home.html', context={
        'data': core_data
    })


def assess(request):
    url = request.POST.get('url')
    weights = [('_'.join(k.split('_')[1:]), float(v))
               for k, v in request.POST.items()
               if k.startswith('weight_') and v != '0']
    print(url, weights)

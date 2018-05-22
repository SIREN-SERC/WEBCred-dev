from django.shortcuts import render
import json


def home(request):
    with open('data/core.json') as f:
        core_data = json.load(f)
    return render(request, 'home.html', context={
        'data': core_data
    })

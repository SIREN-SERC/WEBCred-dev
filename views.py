import json
import inspect
from django.shortcuts import render
from django.http import JsonResponse
from multiprocessing import Process, Manager

import features


def home(request):
    with open('data/core.json') as f:
        core_data = json.load(f)
    return render(request, 'home.html', context={
        'data': core_data
    })


def assess(request):
    f_weights = {
        ('_'.join(k.split('_')[1:])): float(v)
        for k, v in request.POST.items()
        if k.startswith('weight_') and v != '0'
    }

    f_functions = [
        f[1] for f in inspect.getmembers(features)
        if f[0] in f_weights.keys()
    ]

    manager = Manager()
    f_values = manager.dict()

    f_processes = [
        Process(target=func, args=(request.data, f_values))
        for func in f_functions
    ]

    for proc in f_processes:
        proc.start()

    for proc in f_processes:
        proc.join()

    result = f_values.copy()

    return JsonResponse(result)

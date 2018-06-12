import json
import inspect
from django.http import JsonResponse
from multiprocessing import Process, Manager
from django.shortcuts import render

from webcred import features
from webcred.models import Record


def home(request):
    with open('webcred/data/core.json') as f:
        core_data = json.load(f)
    return render(request, 'home.html', context={
        'data': core_data
    })


def assess(request):

    manager = Manager()
    f_values = manager.dict()
    features.modified_date_time(request.data, f_values)

    record = Record.objects.filter(url=request.data['url'],
                                   modified_time=f_values.get(
                                       'modified_date_time'
                                   )).first()
    if record is not None:
        return JsonResponse(record.dump)

    # extract weights from POST data
    f_weights = {
        ('_'.join(k.split('_')[1:])): float(v)
        for k, v in request.POST.items()
        if k.startswith('weight_') and v != '0'
    }

    # map function objects for all features
    f_functions = [
        f[1] for f in inspect.getmembers(features)
        if f[0] in f_weights.keys()
    ]

    # create Process objects for all features
    f_processes = [
        Process(target=func, args=(request.data, f_values))
        for func in f_functions
    ]

    for proc in f_processes:
        proc.start()

    for proc in f_processes:
        proc.join()

    result = f_values.copy()
    Record.objects.create(
        url=request.data['url'],
        modified_time=f_values['modified_date_time'],
        dump=result
    )

    return JsonResponse(result)

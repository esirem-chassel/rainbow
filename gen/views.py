from django.http import HttpResponse
from django.shortcuts import render

from gen.models import Record, Flavor

def index(request):
    res = []
    search = ''
    if request.POST and request.POST['hash']:
        search = request.POST['hash']
        res = Record.objects.filter(res=search)
    context = {'cnt': Record.objects.count(), 'results': res, 'search': search }
    return render(request, 'gen/index.html', context)

def add(request):
    context = {'flavors': Flavor.objects.all(), 'algos': ['md5', 'sha1'], 'errors': [] }
    if request.POST and request.POST['name'] and request.POST['algo'] and request.POST['maxlen']:
        try:
            name = request.POST['name']
            algo = request.POST['algo']
            salt = request.POST['salt'] or ''
            maxlen = max(1, min(12, int(request.POST['maxlen'])))
            if algo in context['algos']:
                f = Flavor()
                f.algo = algo
                f.salt = salt
                f.name = name
                f.maxlen = maxlen
                f.save()
                context['flavors'].append(f)
            else:
                context['errors'].append(f'Unknown algo "{algo}"')
        except Exception as e:
            context['errors'].append(e)
    return render(request, 'gen/add.html', context)

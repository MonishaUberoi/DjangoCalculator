from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
arr=['Java', 'C++', 'C', 'Python', 'Pearl', 'Javascript', 'PHP', 'Swift', 'SQL', 'DotNET', 'Ruby', 'GoLang', 'Delphi', 'C#', 'Objective-C', 'R', 'MATLAB', 'VisualBasic' ]
globalcnt=dict()
def index(request):
    mydictionary={
        'arr':arr
    }
    return render(request, 'index.html', context=mydictionary)
def getquery(request):
    q=request.GET['languages']
    if q in globalcnt:
        globalcnt[q]+=1
    else:
        globalcnt[q]=1
    mydictionary={
        'arr':arr,
        'globalcnt':globalcnt
    }
    return render(request, 'index.html', context=mydictionary)
def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(), key=lambda x:x[1], reverse=True))
    mydictionary={
        'arr':arr,
        'globalcnt':globalcnt
    }
    return render(request, 'index.html', context=mydictionary)


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('''Home <br><a href="http://127.0.0.1:8000/remove">remove</a><br><a href="http://127.0.0.1:8000/capital">capital first</a><br><a href="http://127.0.0.1:8000/spaceremove">spaceremove</a><br>''')
    return render(request,'index.html')

def analyze(request):
    text=request.POST.get('text','default')
    remove=request.POST.get('remove','off')
    cap = request.POST.get('cap','off')
    new = request.POST.get('new','off')
    space = request.POST.get('space','off')

    if remove=='on':
        punc = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        a=""
        for c in text:
            if c not in punc:
                a=a+c
        params = {'purpose':'Remove punc','analyzed_text':a}
        text=a
        # return render(request,'analyze.html',params)

    if(cap=='on'):
        a=""
        for c in text:
            a=a+c.upper()
        params = {'purpose':'Change TO Uppercase','analyzed_text':a}
        # return render(request,'analyze.html',params)
        text=a

    if(new=='on'):
        a=""
        for c in text:
            if c != "\n" and c != '\r':
               a=a+c

        params = {'purpose':'Removed New Line','analyzed_text':a}
        # return render(request,'analyze.html',params)
        text=a

    if(space=='on'):
        a=""
        for c in text:
            if c != " ":
               a=a+c

        params = {'purpose':'Space Removed','analyzed_text':a}
        text=a

    # else:
    #     return HttpResponse("Error")
    return render(request,'analyze.html',params)

# def capital(request):
#     return HttpResponse('''capital first<br> <a href="http://127.0.0.1:8000/">home</a>''')

# def lineremove(request):
#     return HttpResponse('''New Line Remove<br> <a href="http://127.0.0.1:8000/">home</a>''')

# def spaceremove(request):
#     return HttpResponse('''Spaceremove<br> <a href="http://127.0.0.1:8000/">home</a>''')

# def charcount(request):
#     return HttpResponse('''Charcount <br><a href="http://127.0.0.1:8000/">home</a>''')

